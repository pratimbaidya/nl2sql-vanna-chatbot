import asyncio
import uuid
from vanna.capabilities.agent_memory import ToolMemory
from vanna.core.tool import ToolContext
from vanna.core.user import User
from vanna_setup import get_vanna_agent

async def seed_agent_memory(agent = None):
    """Seeds the agent's memory when run as a standalone script."""
    if agent is None:
        agent = get_vanna_agent()
    admin_user = User(id="admin", username="admin", email="admin@example.com", group_memberships=["admin"])
    
    # The 15 required Q&A examples
    training_examples = [
        ToolMemory(question="How many patients do we have?", tool_name="run_sql", args={"sql": "SELECT COUNT(*) AS total_patients FROM patients"}),
        ToolMemory(question="Which city has the most patients?", tool_name="run_sql", args={"sql": "SELECT city, COUNT(*) AS patient_count FROM patients GROUP BY city ORDER BY patient_count DESC LIMIT 1"}),
        ToolMemory(question="Show me all female patients from Mumbai.", tool_name="run_sql", args={"sql": "SELECT first_name, last_name, phone FROM patients WHERE gender = 'F' AND city = 'Mumbai'"}),
        ToolMemory(question="List all doctors and their specializations.", tool_name="run_sql", args={"sql": "SELECT name, specialization FROM doctors"}),
        ToolMemory(question="Which doctor has the most appointments?", tool_name="run_sql", args={"sql": "SELECT d.name, COUNT(a.id) AS appointment_count FROM doctors d JOIN appointments a ON d.id = a.doctor_id GROUP BY d.name ORDER BY appointment_count DESC LIMIT 1"}),
        ToolMemory(question="How many doctors do we have in the Cardiology department?", tool_name="run_sql", args={"sql": "SELECT COUNT(*) FROM doctors WHERE specialization = 'Cardiology'"}),
        ToolMemory(question="How many cancelled appointments last quarter?", tool_name="run_sql", args={"sql": "SELECT COUNT(*) FROM appointments WHERE status = 'Cancelled' AND appointment_date >= date('now', '-3 months')"}),
        ToolMemory(question="List patients who visited more than 3 times.", tool_name="run_sql", args={"sql": "SELECT p.first_name, p.last_name, COUNT(a.id) AS visit_count FROM patients p JOIN appointments a ON p.id = a.patient_id GROUP BY p.id HAVING visit_count > 3"}),
        ToolMemory(question="What percentage of appointments are no-shows?", tool_name="run_sql", args={"sql": "SELECT (CAST(SUM(CASE WHEN status = 'No-Show' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*)) * 100 AS no_show_percentage FROM appointments"}),
        ToolMemory(question="What is the total revenue?", tool_name="run_sql", args={"sql": "SELECT SUM(total_amount) AS total_revenue FROM invoices"}),
        ToolMemory(question="Show revenue by doctor.", tool_name="run_sql", args={"sql": "SELECT d.name, SUM(i.total_amount) AS total_revenue FROM invoices i JOIN appointments a ON a.patient_id = i.patient_id JOIN doctors d ON d.id = a.doctor_id GROUP BY d.name ORDER BY total_revenue DESC"}),
        ToolMemory(question="Show unpaid invoices.", tool_name="run_sql", args={"sql": "SELECT id, patient_id, total_amount, invoice_date FROM invoices WHERE status = 'Pending' OR status = 'Overdue'"}),
        ToolMemory(question="Show the busiest day of the week for appointments.", tool_name="run_sql", args={"sql": "SELECT strftime('%w', appointment_date) AS day_of_week, COUNT(*) AS appt_count FROM appointments GROUP BY day_of_week ORDER BY appt_count DESC LIMIT 1"}),
        ToolMemory(question="Revenue trend by month.", tool_name="run_sql", args={"sql": "SELECT strftime('%Y-%m', invoice_date) AS month, SUM(total_amount) AS monthly_revenue FROM invoices GROUP BY month ORDER BY month"}),
        ToolMemory(question="Show monthly appointment count for the past 6 months.", tool_name="run_sql", args={"sql": "SELECT strftime('%Y-%m', appointment_date) AS month, COUNT(*) as total_appointments FROM appointments WHERE appointment_date >= date('now', '-6 months') GROUP BY month ORDER BY month"})
    ]

    print("\n[System] Seeding Agent Memory...")
    for example in training_examples:
        context = ToolContext(
            user=admin_user,
            conversation_id=str(uuid.uuid4()),
            request_id=str(uuid.uuid4()),
            agent_memory=agent.agent_memory
        )
        
        await agent.agent_memory.save_tool_usage(
            question=example.question,
            tool_name=example.tool_name,
            args=example.args,
            context=context,
            success=True
        )
    print(f"[System] Successfully loaded {len(training_examples)} training examples into memory.\n")

if __name__ == "__main__":
    asyncio.run(seed_agent_memory())