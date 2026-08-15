"""
============================================================
SQLAlchemy CORE — Practice Exercises 1-7
============================================================
Do these ONE AT A TIME. Write the code yourself, run it,
check the result in SQLTools before moving to the next.
Don't skip the "predict before running" steps — that's
where the actual learning happens, not in the typing.
============================================================
"""

from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:yourpassword@localhost:5432/practice")


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
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:ssvtforever%402205@localhost:5432/practice")

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
    res=conn.execute(text(""""SELECT * FROM trains WHERE state"""))

# ============================================================
# EXERCISE 3 — fetchone() vs fetchall()
# ============================================================
# TASK: Run "SELECT * FROM stations" TWICE in this script:
#   (a) once calling result.fetchone() twice in a row
#   (b) once (separate connection/execute) calling .fetchall()
#
# BEFORE YOU RUN: write down in a comment what you EXPECT
# each call to return. Then run it and compare.
#
# GOAL: Understand that a Result can only be consumed once,
#       and fetchone() moves through rows one at a time.
# ============================================================

# my prediction: _______________________

# --- write your code here ---


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


# ============================================================
# EXERCISE 5 — Insert using engine.connect() with NO commit
# ============================================================
# TASK: Same kind of insert as Exercise 4, but this time use
#       engine.connect() and do NOT call conn.commit().
#
# VERIFY: Check SQLTools afterward. Is the row there or not?
#         Write down what you find in a comment below.
#
# GOAL: See the difference between connect() and begin()
#       directly, not just read about it.
# ============================================================

# result after checking SQLTools: _______________________

# --- write your code here ---


# ============================================================
# EXERCISE 6 — Transaction rollback (the important one)
# ============================================================
# TASK: Using engine.begin(), inside ONE block:
#   1. Insert one valid, correct station row.
#   2. Immediately after, run a query with an intentional
#      mistake (e.g. misspell a column name, like "ciy"
#      instead of "city") so it throws an error.
#
# VERIFY: Check SQLTools. Did EITHER row get saved, or did
#         BOTH get rolled back together?
#
# GOAL: Prove to yourself that engine.begin() treats
#       everything inside the block as one all-or-nothing unit.
# ============================================================

# what happened: _______________________

# --- write your code here ---


# ============================================================
# EXERCISE 7 — Join trains and stations (stretch goal)
# ============================================================
# NOTE: This one is slightly ahead of what we've formally
# covered. Your `trains` table doesn't have a foreign key to
# `stations` yet, so you'll need to add one first:
#
#   ALTER TABLE trains ADD COLUMN origin_station_id INTEGER
#   REFERENCES stations(station_id);
#
# Then update a row or two by hand in SQLTools to link them.
#
# TASK: Write a query joining trains to stations on that
#       foreign key, so you can print each train's actual
#       origin station name (not just an ID number).
#
# It's fine to skip this one for now and come back to it
# once we've properly covered ForeignKey in the ORM section.
# ============================================================

# --- write your code here ---