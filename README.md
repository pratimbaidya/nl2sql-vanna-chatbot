# Clinic NL2SQL AI System

## Project Description
This project is an AI-powered Natural Language to SQL (NL2SQL) chatbot designed for a clinic management system. Built with **Vanna AI 2.0** and **FastAPI**, it allows users to ask plain English questions about clinic data (patients, doctors, appointments, finances) and instantly receive SQL queries, data tables, and visualizations. 

## LLM Provider
This project uses **Groq** via Vanna's OpenAI-compatibility integration.
* **Model:** `openai/gpt-oss-20b`

## Architecture Overview
The system follows a modular agentic architecture:
* **Backend Engine:** Vanna 2.0 `Agent` connected to a custom `SafeSqliteRunner`.
* **Security Layer:** All generated SQL is strictly validated *before* execution to ensure it is a `SELECT` statement and contains no dangerous keywords (e.g., `DROP`, `DELETE`, `EXEC`).
* **Memory System:** Uses Vanna's `DemoAgentMemory`, pre-seeded with 15 complex few-shot examples (covering joins, aggregations, and date math) to improve accuracy.
* **Server/UI:** Built using Option A (`VannaFastAPIServer`) to provide a robust, streaming chat interface out of the box.
* **Bonus - Structured Logging:** Implemented a custom FastAPI middleware and configured standard Python loggers to track all incoming HTTP requests, response statuses, and database query executions in the terminal.

---

## Setup Instructions

**1. Clone the repository and navigate to the project directory:**
```bash
git clone https://github.com/pratimbaidya/nl2sql-vanna-chatbot
cd nl2sql-vanna-chatbot
```

**2. Create and activate a virtual environment:**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Configure your Environment Variables:**
Create a `.env` file in the root directory and add your Groq API key:
```
GROQ_API_KEY=your_actual_api_key_here
```

---

## How to Run the Application
You can set up the database, seed the agent's memory, and start the application in one swift command:
```bash
pip install -r requirements.txt
python setup_database.py
python seed_memory.py
uvicorn main:app --port 8000
```

**What this command does:**
1. `pip install`: Installs Vanna, FastAPI, Pandas, Plotly, and the required OpenAI package for Groq routing.

2. `python setup_database.py`: Generates clinic.db and populates it with realistic dummy data spanning the last 12 months.

3. `python seed_memory.py`: Injects 15 distinct Q&A training pairs into the Vanna Agent's semantic memory.

4. `uvicorn main:app`: Starts the FastAPI web server.

---

## Usage & API Documentation
Once the server is running, you can access the system via your web browser:

1. **The Chat Interface**
**URL**: http://127.0.0.1:8000

**Description**: A full graphical interface where you can type questions like "How many patients do we have?" or "Show revenue by doctor." The system will stream back the generated SQL, a data table, and an auto-generated chart.

2. **Health Check Endpoint**
URL: http://127.0.0.1:8000/health

Method: GET

Example Response:
```json
{
  "status": "ok",
  "database": "connected",
  "agent_memory_items": 15
}
```
