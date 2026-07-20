"""
==================================================================
PROBLEM: Course Completion Certificates
CATEGORY: Multi-table dict-join + validation (NO aggregation)
DIFFICULTY: Medium (GRiD Round 2 style - "Data Frame Coding" pattern)
==================================================================

DATA STRUCTURES:

students = [
    {"studentId": str, "studentName": str},
    ...
]

courses = [
    {"courseId": str, "courseName": str, "totalModules": int},
    ...
]

progress = [
    {
        "progressId": str,
        "studentId": str,
        "courseId": str,
        "modulesCompleted": int,
        "status": str      # "VALID" or "DROPPED"
    },
    ...
]

------------------------------------------------------------------
VALID RECORD RULES (a progress record counts ONLY if ALL hold):
------------------------------------------------------------------
1. studentId exists in the students table
2. courseId exists in the courses table
3. status == "VALID"
4. 0 <= modulesCompleted <= totalModules

------------------------------------------------------------------
TASK:
------------------------------------------------------------------
For every VALID (student, course) progress record, compute:

    completionPercentage = (modulesCompleted / totalModules) * 100
                            rounded to nearest whole number

IMPORTANT DIFFERENCE FROM PREVIOUS PROBLEMS:
    There is NO summing or averaging across multiple records here.
    Each valid progress record is judged completely on its own.
    A student can appear multiple times in the output — once per
    course they've fully completed. Do NOT accumulate anything
    into a running total per student like the earlier problems.

If completionPercentage == 100, that student earns a certificate
for that specific course.

------------------------------------------------------------------
OUTPUT FORMAT:
------------------------------------------------------------------
Print each certificate as:
    studentId-courseId-courseName

Join multiple entries with '#'.

Sort order:
    1. studentId ascending
    2. if tied, courseId ascending

Print 'NA' if no certificates are earned.

------------------------------------------------------------------
CONSTRAINTS:
------------------------------------------------------------------
i.   1 <= number of students <= 100000
ii.  1 <= number of courses <= 1000
iii. 0 <= number of progress records <= 200000
iv.  0 <= modulesCompleted <= totalModules

------------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------------
students = [
    {"studentId": "S1", "studentName": "Ira"},
    {"studentId": "S2", "studentName": "Vihaan"}
]

courses = [
    {"courseId": "C1", "courseName": "Python Basics", "totalModules": 10},
    {"courseId": "C2", "courseName": "SQL Foundations", "totalModules": 8}
]

progress = [
    {"progressId": "P1", "studentId": "S1", "courseId": "C1", "modulesCompleted": 10, "status": "VALID"},  # 100% -> cert
    {"progressId": "P2", "studentId": "S1", "courseId": "C2", "modulesCompleted": 6,  "status": "VALID"},  # 75% -> no cert
    {"progressId": "P3", "studentId": "S2", "courseId": "C1", "modulesCompleted": 10, "status": "DROPPED"},# excluded: DROPPED
    {"progressId": "P4", "studentId": "S2", "courseId": "C2", "modulesCompleted": 8,  "status": "VALID"},  # 100% -> cert
    {"progressId": "P5", "studentId": "S9", "courseId": "C1", "modulesCompleted": 10, "status": "VALID"}   # excluded: S9 doesn't exist
]

------------------------------------------------------------------
EXPECTED OUTPUT WALKTHROUGH:
------------------------------------------------------------------
P1: S1, C1, 10/10 = 100% -> certificate earned
P2: S1, C2, 6/8 = 75% -> no certificate
P3: S2, DROPPED -> excluded entirely, doesn't matter that modules match
P4: S2, C2, 8/8 = 100% -> certificate earned
P5: S9 doesn't exist -> excluded

Certificates sorted by studentId asc, then courseId asc:
S1-C1 before S2-C2

Correct output: "S1-C1-Python Basics#S2-C2-SQL Foundations"

==================================================================
YOUR TASK: Write solve(students, courses, progress) that returns
the final formatted string (or 'NA').
==================================================================
"""
students = [
    {"studentId": "S1", "studentName": "Ira"},
    {"studentId": "S2", "studentName": "Vihaan"}
]

courses = [
    {"courseId": "C1", "courseName": "Python Basics", "totalModules": 10},
    {"courseId": "C2", "courseName": "SQL Foundations", "totalModules": 8}
]

progress = [
    {"progressId": "P1", "studentId": "S1", "courseId": "C1", "modulesCompleted": 10, "status": "VALID"},  # 100% -> cert
    {"progressId": "P2", "studentId": "S1", "courseId": "C2", "modulesCompleted": 6,  "status": "VALID"},  # 75% -> no cert
    {"progressId": "P3", "studentId": "S2", "courseId": "C1", "modulesCompleted": 10, "status": "DROPPED"},# excluded: DROPPED
    {"progressId": "P4", "studentId": "S2", "courseId": "C2", "modulesCompleted": 8,  "status": "VALID"},  # 100% -> cert
    {"progressId": "P5", "studentId": "S9", "courseId": "C1", "modulesCompleted": 10, "status": "VALID"}   # excluded: S9 doesn't exist
]


def solve(students, courses, progress):
    student={}
    course={}


    for s in students:
        student[s["studentId"]]=s

    for c in courses:
        course[c["courseId"]]=c

    result=[]

    for p in progress:
        student_id=p["studentId"]
        course_id=p["courseId"]    

        if student_id not in student:
            continue

        if course_id not in course:
            continue

        if p["status"]!="VALID":
            continue

        total_modules= course[course_id]["totalModules"]
        completed=p["modulesCompleted"]
        if p["modulesCompleted"]<0 or p["modulesCompleted"]>total_modules:
            continue

        percentage= round((completed / total_modules)* 100)


        if percentage ==100:
            result.append((student_id , course_id , course[course_id]["courseName"]))


         

        if len(result)==0:
            return "NA"


        result.sort(key=lambda x: (x[0], x[1]))
        output=[]


    for student_id , course_id  , course_name in result:
        output.append((f"{student_id}-{course_id}-{course_name}"))


    return "#".join(output)


print(solve(students,courses,progress))

