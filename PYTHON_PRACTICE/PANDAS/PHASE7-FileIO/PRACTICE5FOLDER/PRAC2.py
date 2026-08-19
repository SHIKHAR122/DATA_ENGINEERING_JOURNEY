# ============================================================
# EXERCISE 1 — Read all rows from a different table
# ============================================================
# TASK: Using engine.connect(), select ALL rows from the
#       `trains` table (not stations this time) and print
#       each row.
#
# GOAL: Prove you can repeat the connect -> execute -> loop
#       pattern without copying test_connection.py blindly.
# ============================================================
# --- write your code here ---
import pandas as pd
from main import engine 
from sqlalchemy import text


with engine.begin() as conn:
    conn.execute(text("""
        INSERT INTO trains (train_number, origin, destination, delay_minutes)
        VALUES (:num, :origin, :dest, :delay)
    """), [
        {"num": "12345", "origin": "Delhi", "dest": "Kanpur", "delay": 15},
        {"num": "54321", "origin": "Mumbai", "dest": "Lucknow", "delay": 40},
    ])

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM trains"))
    for row in result:
        print(row)

# ===========================================================
# EXERCISE 2 — Filtered read with a parameterized query
# ============================================================
# TASK: Select only `station_name` and `city` (not all columns)
#       from `stations` where state = 'UP'.
#       Use a PARAMETER (:state) — do NOT hardcode 'UP'
#       directly into the SQL string.
#
# HINT shape:
#   text("SELECT station_name, city FROM stations WHERE state = :state")
#   conn.execute(query, {"state": "UP"})
#
# GOAL: Apply Topic 6 (parameterized queries) for real,
#       not just recognize the syntax.
# ============================================================
# --- write your code here ---
with engine.connect() as conn:
    query = text("SELECT station_name, city FROM stations WHERE state = :state")
    df = pd.read_sql(query, engine, params={"state": "UP"})
    print(df)
# ============================================================
# EXERCISE 3 — fetchone() vs fetchall()
# ============================================================
# TASK: Run "SELECT * FROM stations" TWICE in this script:
#   (a) once calling result.fetchone() twice in a row
#   (b) once (separate connection/execute) calling .fetchall()
#
# GOAL: Understand that a Result can only be consumed once,
#       and fetchone() moves through rows one at a time.
# ============================================================


# --- write your code here ---
with engine.connect() as conn :
    query=conn.execute(text("SELECT * FROM stations"))
    df=pd.DataFrame(query.fetchall(), columns=query.keys())
    print(df)

with engine.connect() as conn:
    query2=conn.execute(text("SELECT * FROM stations"))
    df2=pd.DataFrame([query2.fetchone()] , columns = query2.keys())
    print(df2)


# ============================================================
# EXERCISE 4 — Insert using engine.begin()
# ============================================================
# TASK: Using engine.begin() (NOT connect()), insert one new
#       row into `stations` of your choice.
#
# VERIFY: After running this script, switch to SQLTools and
#         run: SELECT * FROM stations;
#         Confirm your new row is actually there.
#
# GOAL: See that begin() auto-commits on success — no
#       explicit conn.commit() needed.
# ============================================================

# --- write your code here ---
with engine.begin() as conn:
    conn.execute(text("""INSERT  INTO stations (station_name , city)VALUES (:station_name , :city)"""),{"station_name":"central_station" , "city":"Kanpur"})
    print("VALUES ADDED SUCCESSFULLY")

with engine.connect() as conn:
    query3=conn.execute(text("SELECT * FROM stations"))
    df3=pd.DataFrame(query3.fetchall() , columns=query3.keys())
    print(df3)

