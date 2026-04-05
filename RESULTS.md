# NL2SQL System Test Results

This document contains the automated test results for the 20 required queries.

### **Final Score: 0/20 Passed**

### 1. How many patients do we have?
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT COUNT(*) AS total_patients FROM patients
```
- **Result Summary**:

You have 200 patients in the database.

### 2. List all doctors and their specializations
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT name, specialization FROM doctors
```
- **Result Summary**:
- 
Here’s a quick rundown of every doctor in the system and their respective specialties:

| Doctor | Specialization |

|-----------------------|----------------|

| Dr. Amit Smith | Pediatrics |

| Dr. Jane Singh | Cardiology |

| Dr. Emma Patel | Pediatrics |

| Dr. David Jones | Pediatrics |

| Dr. David Smith | Dermatology |

| Dr. Emma Jones | General |

| Dr. Rahul Williams | Dermatology |

| Dr. David Singh | Orthopedics |

| Dr. Jane Brown | Orthopedics |

| Dr. John Gupta | Dermatology |

| Dr. Emma Patel | Cardiology |

| Dr. Rahul Smith | Pediatrics |

| Dr. David Doe | Cardiology |

| Dr. Sarah Singh | Dermatology |

| Dr. Rahul Smith | General |

If you need further breakdowns (e.g., counts by specialization) or visualizations, just let me know!


### 3. Show me appointments for last month
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT * FROM appointments WHERE appointment_date >= date('now','start of month','-1 month') AND appointment_date < date('now','start of month')
```
- **Result Summary**:
- 
Appointments for Last Month

|id|patient\_id|doctor\_id|appointment\_date|status|notes|
|---|---|---|---|---|---|
|29|199|10|2026-03-06 17:16:45|No-Show|Patient reported mild symptoms\.|
|39|199|15|2026-03-30 17:16:45|No-Show||
|43|142|6|2026-03-06 17:16:45|Cancelled||
|44|185|14|2026-03-20 17:16:45|Completed|Patient reported mild symptoms\.|
|61|123|4|2026-03-08 17:16:45|Scheduled||
|74|14|13|2026-03-16 17:16:45|Scheduled|Patient reported mild symptoms\.|
|81|179|6|2026-03-27 17:16:45|Cancelled||
|84|124|10|2026-03-11 17:16:45|Cancelled||
|86|32|13|2026-03-22 17:16:45|No-Show||
|150|196|1|2026-03-03 17:16:45|Completed||
|167|156|4|2026-03-18 17:16:45|Scheduled|Patient reported mild symptoms\.|
|170|69|12|2026-03-11 17:16:45|Cancelled||
|173|140|15|2026-03-06 17:16:45|No-Show||
|185|133|13|2026-03-01 17:16:45|Scheduled||
|186|51|14|2026-03-24 17:16:45|Cancelled|Patient reported mild symptoms\.|
|202|174|4|2026-03-30 17:16:45|No-Show||
|205|35|1|2026-03-27 17:16:45|Completed|Patient reported mild symptoms\.|
|208|81|2|2026-03-20 17:16:45|Completed||
|217|126|13|2026-03-16 17:16:45|Scheduled||
|235|21|14|2026-03-15 17:16:45|Cancelled|Patient reported mild symptoms\.|
|237|200|5|2026-03-17 17:16:45|Completed|Patient reported mild symptoms\.|
|270|106|11|2026-03-12 17:16:45|Cancelled|Patient reported mild symptoms\.|
|274|175|1|2026-03-29 17:16:45|No-Show|Patient reported mild symptoms\.|
|285|162|5|2026-03-15 17:16:45|Completed|Patient reported mild symptoms\.|
|287|77|5|2026-03-02 17:16:45|Scheduled|Patient reported mild symptoms\.|
|299|123|5|2026-03-06 17:16:45|Cancelled|Patient reported mild symptoms\.|
|331|1|13|2026-03-28 17:16:45|Completed|Patient reported mild symptoms\.|
|357|52|5|2026-03-19 17:16:45|Scheduled||
|366|24|9|2026-03-26 17:16:45|Cancelled||
|375|64|15|2026-03-31 17:16:45|Completed||
|378|95|10|2026-03-16 17:16:45|No-Show||
|380|155|13|2026-03-11 17:16:45|Completed|Patient reported mild symptoms\.|
|390|167|1|2026-03-10 17:16:45|No-Show||
|394|115|9|2026-03-08 17:16:45|No-Show|Patient reported mild symptoms\.|
|447|114|8|2026-03-17 17:16:45|No-Show|Patient reported mild symptoms\.|
|469|195|5|2026-03-18 17:16:45|Completed|Patient reported mild symptoms\.|

Appointments for Last Month
Here’s a visual overview of all appointments from the previous month.

(The chart shows the appointment dates, statuses, and any notes, giving you a quick sense of how many were scheduled, completed, canceled, or no‑shows.)

If you’d like a breakdown by doctor, by status, or any other filter, just let me know!


### 4. Which doctor has the most appointments?
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT d.name, COUNT(a.id) AS appointment_count FROM doctors d JOIN appointments a ON d.id = a.doctor_id GROUP BY d.name ORDER BY appointment_count DESC LIMIT 1
```
- **Result Summary**:

|name|appointment\_count|
|---|---|
|Dr\. Rahul Smith|69|

Dr. Rahul Smith leads the schedule with 69 appointments.


### 5. What is the total revenue?
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT SUM(total_amount) AS total_revenue FROM invoices
```
- **Result Summary**:

|total_revenue|
|880446.29|

The total revenue across all invoices is $880,446.29.


### 6. Show revenue by doctor
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT d.name, SUM(i.total_amount) AS total_revenue FROM invoices i JOIN appointments a ON a.patient_id = i.patient_id JOIN doctors d ON d.id = a.doctor_id GROUP BY d.name ORDER BY total_revenue DESC
```
- **Result Summary**:

|name|total\_revenue|
|---|---|
|Dr\. Rahul Smith|305149\.66999999987|
|Dr\. Emma Patel|287781\.04000000004|
|Dr\. Jane Brown|189275\.04000000007|
|Dr\. David Doe|184422\.52999999997|
|Dr\. David Smith|176214\.95999999996|
|Dr\. John Gupta|170646\.59|
|Dr\. David Jones|163290\.90000000002|
|Dr\. Emma Jones|154749\.32000000007|
|Dr\. Sarah Singh|150698\.59999999995|
|Dr\. Rahul Williams|133403\.20999999996|
|Dr\. Amit Smith|116957\.29|
|Dr\. David Singh|113319\.83000000002|
|Dr\. Jane Singh|113221\.27999999998|

Below is a visual comparison of revenue generated by each doctor.

You can see Dr. Rahul Smith leads with $305,149.67, followed by Dr. Emma Patel and Dr. Jane Brown, etc. If you’d like any further breakdown (e.g., by month, by specialization), just let me know!


### 7. How many cancelled appointments last quarter?
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT COUNT(*) AS cancelled_last_quarter FROM appointments WHERE status = 'Cancelled' AND appointment_date >= date('now', '-3 months')
```
- **Result Summary**:

There were 25 cancelled appointments during the last quarter.


### 8. Top 5 patients by spending
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT p.id, p.first_name, p.last_name, SUM(i.total_amount) AS total_spent FROM invoices i JOIN patients p ON i.patient_id = p.id GROUP BY p.id, p.first_name, p.last_name ORDER BY total_spent DESC LIMIT 5
```
- **Result Summary**:

Top 5 patients by total spending

| Rank | Patient ID | Name | Total Spent |
|------|------------|---------------|-------------|
| 1 | 78 | David Patel | $23,485.69 |
| 2 | 148 | Jane Williams | $20,684.15 |
| 3 | 119 | Sarah Patel | $16,871.66 |
| 4 | 106 | David Brown | $15,178.09 |
| 5 | 48 | Neha Smith | $14,491.87 |

A bar chart visualizing these amounts has been generated for quick reference.


### 9. Average treatment cost by specialization
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT d.specialization, AVG(i.total_amount) AS avg_treatment_cost FROM invoices i JOIN appointments a ON i.patient_id = a.patient_id JOIN doctors d ON a.doctor_id = d.id GROUP BY d.specialization ORDER BY avg_treatment_cost DESC
```
- **Result Summary**:

Average treatment cost by specialization

| Specialization | Avg. Treatment Cost |
|----------------|---------------------|
| Orthopedics | $3,025.95 |
| Dermatology | $2,948.43 |
| Pediatrics | $2,939.37 |
| Cardiology | $2,891.53 |
| General | $2,785.53 |

A bar chart visualizing these averages is available for quick comparison.


### 10. Show monthly appointment count for the past 6 months
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT strftime('%Y-%m', appointment_date) AS month, COUNT(*) as total_appointments FROM appointments WHERE appointment_date >= date('now', '-6 months') GROUP BY month ORDER BY month
```
- **Result Summary**:

Here’s the monthly appointment count for the past six months:

| Month | Appointments |
|---------|--------------|
| 2025‑10 | 46 |
| 2025‑11 | 36 |
| 2025‑12 | 47 |
| 2026‑01 | 38 |
| 2026‑02 | 47 |
| 2026‑03 | 36 |

A bar chart visualizing this trend is available for a quick visual reference.


### 11. Which city has the most patients?
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 12. List patients who visited more than 3 times
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 13. Show unpaid invoices
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 14. What percentage of appointments are no-shows?
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 15. Show the busiest day of the week for appointments
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 16. Revenue trend by month
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 17. Average appointment duration by doctor
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 18. List patients with overdue invoices
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 19. Compare revenue between departments
- **Status**: ✅ Passed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

### 20. Show patient registration trend by month
- **Status**: ❌ Failed
- **Generated SQL**:
```sql

```
- **Result Summary**: No data found for your query.

