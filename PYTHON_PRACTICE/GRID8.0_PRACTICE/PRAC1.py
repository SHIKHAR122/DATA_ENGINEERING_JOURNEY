"""
==================================================================
PROBLEM: Employee Bonus Eligibility
CATEGORY: Multi-table dict-join + validation + aggregation
DIFFICULTY: Medium (GRiD Round 2 style - "Data Frame Coding" pattern)
==================================================================

DATA STRUCTURES:

employees = [
    {"employeeId": str, "employeeName": str, "department": str},
    ...
]

attendance = [
    {
        "recordId": str,
        "employeeId": str,
        "month": str,
        "daysPresent": int,
        "totalDays": int,
        "status": str   # "VALID" or "CANCELLED"
    },
    ...
]

------------------------------------------------------------------
VALID RECORD RULES (an attendance record counts ONLY if ALL hold):
------------------------------------------------------------------
1. employeeId exists in the employees table
2. status == "VALID"
3. 0 <= daysPresent <= totalDays

------------------------------------------------------------------
TASK:
------------------------------------------------------------------
For every employee with AT LEAST ONE valid attendance record, compute:

    attendancePercentage = ( sum(daysPresent) / sum(totalDays) )
                            across that employee's valid records
                            * 100, rounded to nearest whole number

Employees with attendancePercentage >= 85 qualify for a bonus.

------------------------------------------------------------------
OUTPUT FORMAT:
------------------------------------------------------------------
Print each qualifying employee as:
    employeeId-employeeName-percentage

Join multiple entries with '#'.

Sort order:
    1. percentage descending
    2. if tied, employeeId ascending

Print 'NA' if no employee qualifies.

------------------------------------------------------------------
CONSTRAINTS:
------------------------------------------------------------------
i.   1 <= number of employees <= 100000
ii.  0 <= number of attendance records <= 200000
iii. 0 <= daysPresent <= totalDays
iv.  totalDays >= 0

------------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------------
employees = [
    {"employeeId": "E1", "employeeName": "Ravi", "department": "Sales"},
    {"employeeId": "E2", "employeeName": "Meena", "department": "Ops"},
    {"employeeId": "E3", "employeeName": "Sam", "department": "IT"}
]

attendance = [
    {"recordId": "A1", "employeeId": "E1", "month": "Jan", "daysPresent": 28, "totalDays": 30, "status": "VALID"},
    {"recordId": "A2", "employeeId": "E1", "month": "Feb", "daysPresent": 27, "totalDays": 28, "status": "VALID"},
    {"recordId": "A3", "employeeId": "E2", "month": "Jan", "daysPresent": 20, "totalDays": 30, "status": "VALID"},
    {"recordId": "A4", "employeeId": "E3", "month": "Jan", "daysPresent": 25, "totalDays": 30, "status": "CANCELLED"}
]

------------------------------------------------------------------
EXPECTED OUTPUT:
------------------------------------------------------------------
E1-Ravi-95#E2-Meena-67 is WRONG -- E2 is only 67%, below 85, excluded.

Correct output: "E1-Ravi-95"
(E1: (28+27)/(30+28) * 100 = 94.8 -> rounds to 95 -> qualifies
 E2: 20/30 * 100 = 66.7 -> rounds to 67 -> below 85, excluded
 E3: only CANCELLED record, no valid marks, excluded)

==================================================================
YOUR TASK: Write solve(employees, attendance) that returns the
final formatted string (or 'NA').
==================================================================
"""
def solve(employees, attendance):
    emp={}
    for e in employees:
        emp[e["employeeId"]]=e
    
    present={}
    total={}

    for a in attendance:
          if a["employeeId"] not in emp:
               continue
          if  a["status"]!="VALID":
               continue
          if a["daysPresent"]<0 or a["totalDays"]<a["dayPresent"]:
               continue
          
          employee_id=a["employeeId"]

          if employee_id not in present:
               present[employee_id]=0
               total[employee_id]=0

          present[employee_id]+=a["dayPresent"]
          total[employee_id]+=a["totalDays"]

    ans=[]


    for employee_id in present :
         percentage=round(present[employee_id]/total[employee_id]*100)

    
         if percentage>=85:
          name=emp[employee_id]["employeeName"]
          ans.append((employee_id,name,percentage))


         if len(ans)==0:
             return "NA"


    ans.sort(key=lambda x : (x[-2],x[0]))

    result=[]

    for employee_id , name , percentage in ans:
        result.append(f"{employee_id}-{name}-{percentage}")

    
    return "#".join(result)