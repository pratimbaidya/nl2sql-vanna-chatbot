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
|--------|----------------|
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
SELECT city, COUNT(*) AS patient_count FROM patients GROUP BY city ORDER BY patient_count DESC LIMIT 1
```
- **Result Summary**:

The city with the highest number of patients is Kolkata, with 41 patients.


### 12. List patients who visited more than 3 times
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT p.first_name, p.last_name, COUNT(a.id) AS visit_count FROM patients p JOIN appointments a ON p.id = a.patient_id GROUP BY p.id HAVING visit_count > 3
```
- **Result Summary**:

Here are the patients who have visited the clinic more than three times:

| First Name | Last Name | Visit Count |
|------------|-----------|-------------|
| Amit | Gupta | 5 |
| David | Brown | 7 |
| Sarah | Doe | 5 |
| Emma | Sharma | 6 |
| Sarah | Jones | 5 |
| Michael | Sharma | 4 |
| Neha | Johnson | 4 |
| Jane | Doe | 4 |
| Jane | Williams | 4 |
| Jane | Smith | 4 |
| John | Patel | 4 |
| Michael | Williams | 4 |
| Amit | Sharma | 5 |
| Neha | Smith | 4 |
| David | Doe | 5 |
| Amit | Patel | 4 |
| Neha | Smith | 5 |
| Neha | Smith | 6 |
| David | Smith | 4 |
| Priya | Doe | 4 |
| Amit | Singh | 5 |
| Priya | Doe | 4 |
| Jane | Doe | 4 |
| Sarah | Gupta | 4 |
| Emma | Williams | 5 |
| Rahul | Williams | 4 |
| Michael | Patel | 4 |
| David | Sharma | 6 |
| Michael | Sharma | 4 |
| Michael | Doe | 4 |
| David | Brown | 5 |
| Jane | Gupta | 4 |
| Amit | Jones | 4 |
| Neha | Doe | 4 |
| Neha | Gupta | 4 |
| John | Jones | 5 |
| Jane | Patel | 4 |
| Rahul | Williams | 4 |
| John | Sharma | 5 |
| Michael | Williams | 4 |
| David | Williams | 5 |
| Jane | Johnson | 4 |
| Emma | Sharma | 4 |
| David | Johnson | 4 |
| Emma | Jones | 5 |
| Jane | Patel | 5 |
| Michael | Williams | 6 |
| Sarah | Smith | 4 |
| Neha | Patel | 4 |
| Michael | Patel | 7 |

(These results are derived from the `patients` and `appointments` tables, counting each appointment per patient.)


### 13. Show unpaid invoices
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT id, patient_id, total_amount, invoice_date FROM invoices WHERE status = 'Pending' OR status = 'Overdue'
```
- **Result Summary**:

|index|id|patient\_id|total\_amount|invoice\_date|
|---|---|---|---|---|
|0|1|27|964\.7|2025-11-12|
|1|2|135|4175\.09|2026-03-26|
|2|3|125|2914\.02|2025-12-28|
|3|4|177|1167\.84|2025-08-13|
|4|6|81|1739\.18|2025-09-30|
|5|7|63|5011\.88|2025-06-15|
|6|8|11|5743\.58|2025-06-22|
|7|9|166|4764\.89|2025-08-16|
|8|10|197|3634\.0|2025-04-28|
|9|12|169|261\.82|2025-12-12|
|10|13|80|918\.43|2025-07-04|
|11|14|121|4933\.32|2025-11-30|
|12|15|1|2176\.88|2026-02-15|
|13|16|56|610\.48|2025-11-01|
|14|17|133|105\.37|2025-11-07|
|15|18|119|5329\.93|2025-05-17|
|16|19|63|3364\.36|2025-09-08|
|17|20|61|699\.44|2025-05-30|
|18|21|195|1281\.48|2025-09-18|
|19|22|181|918\.43|2025-05-20|
|20|23|17|4257\.09|2026-01-01|
|21|24|175|587\.76|2025-09-02|
|22|25|98|4460\.35|2025-10-19|
|23|26|54|2952\.14|2026-03-29|
|24|27|41|1919\.42|2025-11-23|
|25|28|125|4718\.03|2025-04-17|
|26|29|181|1581\.1|2026-01-03|
|27|32|184|4491\.41|2025-07-14|
|28|34|71|2544\.94|2025-06-10|
|29|35|64|414\.97|2025-04-04|
|30|36|20|1670\.6|2026-03-18|
|31|38|148|5442\.93|2025-07-01|
|32|39|165|1603\.29|2025-12-22|
|33|40|84|5054\.05|2026-03-11|
|34|41|143|4751\.97|2025-10-19|
|35|42|48|5646\.34|2025-05-06|
|36|44|106|5783\.98|2026-01-27|
|37|45|46|5427\.42|2025-07-17|
|38|46|185|1856\.79|2025-07-26|
|39|51|87|4562\.93|2026-03-18|
|40|52|159|708\.05|2026-02-21|
|41|55|31|1964\.09|2026-01-26|
|42|59|89|4206\.41|2025-05-18|
|43|60|148|4727\.27|2025-12-23|
|44|61|144|4839\.77|2025-05-11|
|45|63|78|2989\.9|2025-12-14|
|46|64|197|1741\.51|2025-10-13|
|47|65|141|3958\.87|2025-07-12|
|48|67|172|495\.96|2025-04-04|
|49|69|33|1832\.73|2025-12-26|
|50|71|110|1758\.94|2025-12-04|
|51|72|108|1981\.0|2025-09-17|
|52|73|16|3284\.14|2025-10-06|
|53|74|169|5322\.86|2026-03-17|
|54|75|67|2248\.57|2025-08-15|
|55|76|23|1829\.74|2025-11-13|
|56|77|150|1127\.6|2025-08-10|
|57|78|195|2394\.87|2025-07-15|
|58|80|128|2104\.45|2025-08-15|
|59|81|188|1920\.01|2025-07-07|
|60|82|48|550\.65|2025-06-02|
|61|83|55|965\.55|2026-02-09|
|62|84|14|3791\.7|2025-08-11|
|63|86|119|4303\.97|2026-04-03|
|64|89|132|3893\.45|2026-03-04|
|65|90|13|1547\.55|2026-03-30|
|66|92|88|3876\.87|2025-04-27|
|67|93|70|4166\.53|2025-08-31|
|68|95|103|4029\.57|2025-11-28|
|69|96|177|4907\.23|2025-07-09|
|70|98|84|1907\.32|2026-02-28|
|71|99|63|1028\.91|2026-03-08|
|72|103|53|2003\.22|2025-11-01|
|73|105|161|1317\.53|2026-01-28|
|74|109|51|1364\.92|2025-06-20|
|75|111|44|1532\.07|2026-02-19|
|76|112|136|1038\.1|2026-03-03|
|77|113|32|1319\.8|2026-02-06|
|78|114|89|5838\.89|2025-09-02|
|79|115|186|4919\.04|2025-10-14|
|80|116|15|1083\.58|2025-06-22|
|81|117|90|2704\.56|2025-08-08|
|82|118|98|278\.12|2025-05-01|
|83|119|98|5543\.57|2025-09-12|
|84|120|32|955\.5|2026-01-23|
|85|121|168|3163\.93|2026-01-20|
|86|122|106|4140\.27|2025-09-22|
|87|123|158|3047\.52|2025-11-14|
|88|124|19|4211\.14|2026-03-14|
|89|127|197|763\.12|2026-01-25|
|90|128|25|2403\.22|2025-12-31|
|91|130|109|1411\.19|2025-09-22|
|92|133|92|5937\.51|2025-11-01|
|93|134|128|3067\.37|2025-05-15|
|94|136|3|1257\.3|2025-11-10|
|95|138|119|5805\.96|2025-04-23|
|96|139|192|3958\.25|2025-04-30|
|97|140|4|5386\.51|2025-04-16|
|98|141|106|894\.31|2026-03-18|
|99|142|83|4019\.49|2026-03-01|
|100|144|68|1363\.78|2026-03-19|
|101|146|11|5060\.96|2025-05-24|
|102|147|35|5171\.88|2026-03-05|
|103|148|88|5376\.05|2026-03-21|
|104|150|66|5709\.97|2026-02-14|
|105|151|152|2089\.82|2025-07-17|
|106|154|136|3671\.64|2025-09-12|
|107|157|112|3913\.19|2025-04-14|
|108|159|131|3219\.74|2025-12-07|
|109|161|69|1294\.25|2025-10-12|
|110|162|160|5204\.96|2025-11-04|
|111|163|86|3608\.96|2025-05-05|
|112|164|69|3255\.44|2026-02-27|
|113|165|80|1087\.53|2025-05-11|
|114|168|133|796\.29|2026-02-11|
|115|170|124|1892\.54|2026-02-28|
|116|171|143|4687\.07|2025-07-02|
|117|172|48|3485\.74|2025-12-26|
|118|174|121|1446\.47|2025-04-07|
|119|175|3|3365\.81|2026-03-26|
|120|177|144|4247\.6|2026-03-06|
|121|179|154|2542\.49|2025-09-12|
|122|180|116|516\.91|2026-01-09|
|123|182|46|1917\.19|2025-09-26|
|124|183|174|1845\.46|2025-07-14|
|125|184|114|2063\.94|2025-12-18|
|126|185|179|1717\.57|2025-10-11|
|127|187|194|2022\.43|2025-04-24|
|128|189|179|2742\.45|2026-04-03|
|129|190|164|5399\.13|2025-07-09|
|130|192|132|3244\.37|2025-06-28|
|131|193|78|3588\.22|2025-10-07|
|132|195|109|5791\.03|2025-09-30|
|133|197|153|2429\.85|2025-09-26|
|134|198|13|5317\.3|2025-10-14|
|135|199|178|5750\.06|2025-07-03|
|136|200|71|4146\.29|2025-11-19|
|137|202|70|276\.77|2025-07-04|
|138|205|95|460\.43|2025-10-05|
|139|206|160|3186\.19|2026-02-15|
|140|207|57|4639\.99|2025-07-17|
|141|209|3|1377\.93|2025-10-10|
|142|210|41|4695\.95|2025-10-04|
|143|212|166|580\.43|2025-06-20|
|144|213|56|4115\.08|2025-08-13|
|145|214|156|5750\.99|2026-01-22|
|146|216|88|4813\.54|2025-12-28|
|147|217|43|682\.28|2025-12-22|
|148|218|74|1093\.67|2025-05-26|
|149|219|193|4218\.38|2026-03-14|
|150|220|126|3696\.18|2025-08-02|
|151|223|156|5326\.96|2025-07-16|
|152|224|172|4945\.34|2025-08-12|
|153|225|83|2270\.87|2026-02-12|
|154|226|138|588\.07|2025-12-24|
|155|227|22|812\.2|2025-10-19|
|156|228|127|1877\.68|2025-07-14|
|157|229|7|5398\.31|2025-09-17|
|158|230|184|3545\.6|2026-02-17|
|159|232|43|4962\.56|2025-06-24|
|160|233|169|2772\.56|2025-11-21|
|161|235|185|3072\.33|2025-09-08|
|162|236|93|5712\.85|2025-07-25|
|163|237|195|469\.05|2026-03-09|
|164|238|189|3416\.88|2026-03-29|
|165|239|69|606\.51|2026-03-11|
|166|240|29|1190\.28|2025-10-05|
|167|241|141|5884\.92|2025-09-03|
|168|242|81|5174\.03|2025-04-23|
|169|243|163|2468\.7|2025-08-17|
|170|244|57|5283\.12|2025-07-01|
|171|246|110|1814\.38|2025-10-17|
|172|247|111|3880\.71|2025-09-07|
|173|249|48|4809\.14|2025-08-19|
|174|252|95|4449\.67|2025-05-25|
|175|253|138|3941\.84|2026-03-12|
|176|254|56|1789\.73|2026-02-27|
|177|256|137|4974\.23|2025-04-25|
|178|257|196|363\.62|2025-11-24|
|179|258|172|4676\.83|2025-08-07|
|180|259|139|4745\.73|2025-11-08|
|181|260|37|3998\.1|2025-06-14|
|182|261|29|3265\.19|2026-01-22|
|183|263|162|5165\.9|2025-07-18|
|184|267|164|3461\.94|2025-06-21|
|185|270|93|1768\.57|2025-11-17|
|186|271|171|147\.77|2025-06-06|
|187|275|28|929\.66|2025-04-25|
|188|276|135|284\.14|2025-09-18|
|189|278|71|2554\.22|2025-08-20|
|190|279|112|2555\.97|2025-05-09|
|191|280|46|2472\.24|2025-09-28|
|192|283|78|5524\.03|2025-12-27|
|193|284|4|2554\.36|2025-08-23|
|194|285|184|1234\.38|2026-01-21|
|195|286|148|4575\.87|2025-08-18|
|196|287|20|2334\.6|2026-02-24|
|197|288|178|2159\.66|2025-12-13|
|198|289|191|1831\.93|2025-12-26|
|199|290|31|658\.87|2025-08-29|
|200|292|138|554\.82|2025-09-19|
|201|296|44|862\.77|2025-10-30|
|202|297|2|2581\.94|2025-08-06|
|203|298|192|1888\.71|2025-12-24|


### 14. What percentage of appointments are no-shows?
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT (CAST(SUM(CASE WHEN status = 'No-Show' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*)) * 100 AS no_show_percentage FROM appointments
```
- **Result Summary**:

The proportion of appointments that were marked as No‑Show is 27.6 % of all scheduled appointments.


### 15. Show the busiest day of the week for appointments
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT strftime('%w', appointment_date) AS day_of_week, COUNT(*) AS appt_count FROM appointments GROUP BY day_of_week ORDER BY appt_count DESC LIMIT 1
```
- **Result Summary**:

Busiest day of the week for appointments

| Day of Week | Appointments |
|-------------|--------------|
| Sunday (0) | 87 |

The query grouped appointments by the weekday number (`0` = Sunday, `1` = Monday, …) and found that Sunday has the highest count with 87 scheduled appointments.


### 16. Revenue trend by month
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT strftime('%Y-%m', invoice_date) AS month, SUM(total_amount) AS monthly_revenue FROM invoices GROUP BY month ORDER BY month
```
- **Result Summary**:

Here’s the monthly revenue trend for the period covered in the data:

2025‑04: $75,697.69

2025‑05: $69,687.63

2025‑06: $48,084.27

2025‑07: $98,484.14

2025‑08: $93,398.41

2025‑09: $67,423.39

2025‑10: $62,490.89

2025‑11: $76,440.21

2025‑12: $72,557.00

2026‑01: $57,115.07

2026‑02: $48,879.66

2026‑03: $103,141.51

2026‑04: $7,046.42

The chart visualizes these values, highlighting a significant spike in March 2026 and a sharp decline in April 2026.


### 17. Average appointment duration by doctor
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT d.name, AVG(t.duration_minutes) AS avg_duration_minutes FROM doctors d JOIN appointments a ON d.id=a.doctor_id JOIN treatments t ON a.id=t.appointment_id GROUP BY d.id, d.name ORDER BY avg_duration_minutes DESC
```
- **Result Summary**:

*My Comment*: First it generated this SQL to.

```sql
SELECT d.name, AVG(a.duration) AS avg_duration_minutes FROM doctors d JOIN appointments a ON d.id = a.doctor_id GROUP BY d.id, d.name ORDER BY avg_duration_minutes DESC
```
*My Comment*: The SQL did not work so the agent fetched the 5 rows from the `appointments` table using this SQL and generated below message:

```sql
SELECT * FROM appointments LIMIT 5
```

I’m afraid I can’t calculate the average appointment duration because the `appointments` table does not contain any duration-related columns (e.g., `start_time`, `end_time`, or a pre‑computed `duration`). All I see are:

| Column | Type |
|--------|------|
| id | integer |
| patient_id | integer |
| doctor_id | integer |
| appointment_date | datetime |
| status | text |
| notes | text |

If you have a separate table or columns that record appointment start/end times or the actual duration, please let me know and I can compute the averages per doctor. Alternatively, if you’d like an estimate based on typical appointment times, I can provide a generic calculation.

*My Comment*: Then I changed the query to this -> Average treatment duration by doctor. Then it generated perfect SQL and the table

```sql
SELECT d.name, AVG(t.duration_minutes) AS avg_duration_minutes FROM doctors d JOIN appointments a ON d.id=a.doctor_id JOIN treatments t ON a.id=t.appointment_id GROUP BY d.id, d.name ORDER BY avg_duration_minutes DESC
```

|index|name|avg\_duration\_minutes|
|---|---|---|
|0|Dr\. John Gupta|45\.535714285714285|
|1|Dr\. Rahul Smith|38\.57142857142857|
|2|Dr\. Emma Patel|38\.0|
|3|Dr\. Emma Patel|37\.77777777777778|
|4|Dr\. David Doe|37\.69230769230769|
|5|Dr\. Jane Brown|37\.241379310344826|
|6|Dr\. Jane Singh|37\.05882352941177|
|7|Dr\. David Jones|35\.714285714285715|
|8|Dr\. Rahul Williams|35\.55555555555556|
|9|Dr\. Rahul Smith|35\.45454545454545|
|10|Dr\. David Smith|34\.56521739130435|
|11|Dr\. Amit Smith|32\.142857142857146|
|12|Dr\. Sarah Singh|32\.04545454545455|
|13|Dr\. Emma Jones|31\.304347826086957|
|14|Dr\. David Singh|27\.0|



### 18. List patients with overdue invoices
- **Status**: ✅ Passed
- **Generated SQL**:
```sql
SELECT p.first_name, p.last_name, p.email, i.id AS invoice_id, i.total_amount, i.invoice_date FROM patients p JOIN invoices i ON p.id = i.patient_id WHERE i.status = 'Overdue'
```
- **Result Summary**:

Patients with Overdue Invoices

| First Name | Last Name | Email | Invoice ID | Total Amount | Invoice Date |
|------------|-----------|-------|------------|--------------|--------------|
| Jane | Patel | jane.patel@example.com | 2 | 4,175.09 | 2026‑03‑26 |
| Jane | Jones | jane.jones@example.com | 3 | 2,914.02 | 2025‑12‑28 |
| Amit | Doe | amit.doe@example.com | 4 | 1,167.84 | 2025‑08‑13 |
| Jane | Doe | – | 6 | 1,739.18 | 2025‑09‑30 |
| Priya | Doe | priya.doe@example.com | 7 | 5,011.88 | 2025‑06‑15 |
| Rahul | Sharma | – | 8 | 5,743.58 | 2025‑06‑22 |
| David | Johnson | – | 9 | 4,764.89 | 2025‑08‑16 |
| Neha | Patel | neha.patel@example.com | 12 | 261.82 | 2025‑12‑12 |
| David | Sharma | – | 16 | 610.48 | 2025‑11‑01 |
| Sarah | Patel | sarah.patel@example.com | 18 | 5,329.93 | 2025‑05‑17 |
| Priya | Doe | priya.doe@example.com | 19 | 3,364.36 | 2025‑09‑08 |
| Jane | Sharma | – | 20 | 699.44 | 2025‑05‑30 |
| John | Johnson | – | 21 | 1,281.48 | 2025‑09‑18 |
| Sarah | Jones | sarah.jones@example.com | 23 | 4,257.09 | 2026‑01‑01 |
| John | Williams | john.williams@example.com | 24 | 587.76 | 2025‑09‑02 |
| Neha | Doe | neha.doe@example.com | 29 | 1,581.10 | 2026‑01‑03 |
| John | Johnson | – | 34 | 2,544.94 | 2025‑06‑10 |
| John | Williams | john.williams@example.com | 36 | 1,670.60 | 2026‑03‑18 |
| Jane | Williams | – | 38 | 5,442.93 | 2025‑07‑01 |
| Sarah | Williams | – | 41 | 4,751.97 | 2025‑10‑19 |
| … | … | … | … | … | … |

A visual overview of these overdue invoices is available in the accompanying chart titled “Patients with Overdue Invoices.”


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

