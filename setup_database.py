import sqlite3
import random
from datetime import datetime, timedelta

def create_database():
    conn = sqlite3.connect('clinic.db')
    cursor = conn.cursor()

    # Table 1: patients
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT,
        phone TEXT,
        date_of_birth DATE,
        gender TEXT,
        city TEXT,
        registered_date DATE
    )
    ''')

    # Table 2: doctors
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT,
        department TEXT,
        phone TEXT
    )
    ''')

    # Table 3: appointments
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        appointment_date DATETIME,
        status TEXT,
        notes TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id),
        FOREIGN KEY(doctor_id) REFERENCES doctors(id)
    )
    ''')

    # Table 4: treatments
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS treatments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        appointment_id INTEGER,
        treatment_name TEXT,
        cost REAL,
        duration_minutes INTEGER,
        FOREIGN KEY(appointment_id) REFERENCES appointments(id)
    )
    ''')

    # Table 5: invoices
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        invoice_date DATE,
        total_amount REAL,
        paid_amount REAL,
        status TEXT,
        FOREIGN KEY(patient_id) REFERENCES patients(id)
    )
    ''')

    return conn, cursor

def generate_dummy_data(conn, cursor):
    # Data pools
    first_names = ["John", "Jane", "Amit", "Priya", "Michael", "Sarah", "Rahul", "Neha", "David", "Emma"]
    last_names = ["Smith", "Doe", "Sharma", "Patel", "Johnson", "Williams", "Gupta", "Singh", "Brown", "Jones"]
    cities = ["Kolkata", "Mumbai", "Delhi", "Bangalore", "Chennai", "Pune", "Hyderabad", "Ahmedabad"]
    genders = ["M", "F"]
    specializations = ["Dermatology", "Cardiology", "Orthopedics", "General", "Pediatrics"]
    statuses = ["Scheduled", "Completed", "Cancelled", "No-Show"]
    invoice_statuses = ["Paid", "Pending", "Overdue"]
    treatment_names = ["Consultation", "Blood Test", "X-Ray", "Physical Therapy", "Vaccination", "Checkup"]
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    def random_date(start, end):
        return start + timedelta(days=random.randint(0, int((end - start).days)))

    # 1. Insert 15 Doctors
    for i in range(15):
        spec = random.choice(specializations)
        cursor.execute("INSERT INTO doctors (name, specialization, department, phone) VALUES (?, ?, ?, ?)",
                       (f"Dr. {random.choice(first_names)} {random.choice(last_names)}", spec, f"{spec} Dept", f"555-01{i:02d}"))

    # 2. Insert 200 Patients
    for _ in range(200):
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        has_email = random.choice([True, False]) # Nullable field
        cursor.execute('''
        INSERT INTO patients (first_name, last_name, email, phone, date_of_birth, gender, city, registered_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            fname, lname, 
            f"{fname.lower()}.{lname.lower()}@example.com" if has_email else None,
            f"98765{random.randint(10000, 99999)}" if random.choice([True, False]) else None,
            random_date(datetime(1950, 1, 1), datetime(2015, 1, 1)).strftime('%Y-%m-%d'),
            random.choice(genders), random.choice(cities),
            random_date(start_date, end_date).strftime('%Y-%m-%d')
        ))

    # 3. Insert 500 Appointments
    for _ in range(500):
        status = random.choice(statuses)
        has_notes = random.choice([True, False])
        cursor.execute('''
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, notes)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            random.randint(1, 200), random.randint(1, 15),
            random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S'),
            status,
            "Patient reported mild symptoms." if has_notes else None
        ))

    # 4. Insert 350 Treatments (Linked to completed appointments mostly)
    for i in range(350):
        # We'll just link to random appointments 1-500 for simplicity
        cursor.execute('''
        INSERT INTO treatments (appointment_id, treatment_name, cost, duration_minutes)
        VALUES (?, ?, ?, ?)
        ''', (
            random.randint(1, 500), random.choice(treatment_names),
            round(random.uniform(50.0, 5000.0), 2), random.choice([15, 30, 45, 60])
        ))

    # 5. Insert 300 Invoices
    for _ in range(300):
        total = round(random.uniform(100.0, 6000.0), 2)
        status = random.choice(invoice_statuses)
        paid = total if status == "Paid" else (0.0 if status == "Pending" else round(total * random.uniform(0, 0.5), 2))
        
        cursor.execute('''
        INSERT INTO invoices (patient_id, invoice_date, total_amount, paid_amount, status)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            random.randint(1, 200), random_date(start_date, end_date).strftime('%Y-%m-%d'),
            total, paid, status
        ))

    conn.commit()
    print("Database setup complete.")
    print("Created 200 patients, 15 doctors, 500 appointments, 350 treatments, and 300 invoices.")

if __name__ == "__main__":
    conn, cursor = create_database()
    generate_dummy_data(conn, cursor)
    conn.close()