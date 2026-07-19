# Practice — Library Fine Calculator
# members: {memberId, memberName}, books: {bookId, bookName, finePerDay}, borrowRecords: {recordId, memberId, bookId, daysLate, status} (status: RETURNED or LOST)
# Rule: only count records where memberId exists, bookId exists, status is RETURNED, and daysLate >= 0.
# Task: total fine per member = sum of daysLate * finePerDay across their valid records. 
#Print members with totalFine > 500 as memberId-memberName-totalFine, sorted by totalFine descending then memberId ascending. 'NA' if none.
# (Twist: no percentage/weight — plain sum, tests if you overcomplicate a simpler aggregation.)



"""
Sample data for: Library Fine Calculator

Rule reminder: only count records where memberId exists,
bookId exists, status is "RETURNED", and daysLate >= 0.

Task: totalFine = sum of (daysLate * finePerDay) across valid records.
Print members with totalFine > 500 as memberId-memberName-totalFine,
sorted by totalFine descending, then memberId ascending. 'NA' if none.
"""

members = [
    {"memberId": "M1", "memberName": "Kabir"},
    {"memberId": "M2", "memberName": "Sana"},
    {"memberId": "M3", "memberName": "Devansh"},
]

books = [
    {"bookId": "B1", "bookName": "Clean Code", "finePerDay": 10},
    {"bookId": "B2", "bookName": "Atomic Habits", "finePerDay": 5},
    {"bookId": "B3", "bookName": "The Pragmatic Programmer", "finePerDay": 20},
]

borrowRecords = [
    {"recordId": "R1", "memberId": "M1", "bookId": "B1", "daysLate": 40, "status": "RETURNED"},   # 40*10 = 400
    {"recordId": "R2", "memberId": "M1", "bookId": "B3", "daysLate": 6,  "status": "RETURNED"},   # 6*20 = 120
    {"recordId": "R3", "memberId": "M2", "bookId": "B2", "daysLate": 30, "status": "RETURNED"},   # 30*5 = 150
    {"recordId": "R4", "memberId": "M2", "bookId": "B1", "daysLate": 25, "status": "LOST"},       # excluded, status not RETURNED
    {"recordId": "R5", "memberId": "M3", "bookId": "B2", "daysLate": 10, "status": "RETURNED"},   # 10*5 = 50
    {"recordId": "R6", "memberId": "M1", "bookId": "B9", "daysLate": 5,  "status": "RETURNED"},   # excluded, B9 doesn't exist
]


def LibraryFine(members , books , borrowRecords):
    mem={}     # lookup dictionaries
    book={}    #lookup dictionaries
    for m in members:
        mem[m["memberId"]]=m
    
    for b in books:
        book[b["bookId"]]=b


    fine={}    #acummulate dictionary


    for record in borrowRecords:
        member_id=record["memberId"]
        book_id=record["bookId"]

        if member_id not in mem:
            continue
        if book_id not in book:
            continue
        if record["status"]!="RETURNED":
            continue
        if record["daysLate"]<0:
            continue

        fine_amount=record["daysLate"]*book[book_id]["finePerDay"]

        if member_id not in fine:
            fine[member_id]=0

        fine[member_id]+=fine_amount


        result=[]


    for member_id in fine :
        if fine[member_id]>500:
            member_name=mem[member_id]["memberName"]
            result.append((member_id, member_name,fine[member_id]))



        if len(result)==0:
            return "NA"
        

    result.sort(key=lambda x : (x[-2],x[0]))


    output=[]

    for member_id , member_name , total_fine in result:
        output.append(f"{member_id}-{member_name}-{total_fine}")


    return "#".join(output)




print(LibraryFine(members, books, borrowRecords))

    

