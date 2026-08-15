from main import engine
from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM stations"))

    for row in result:
        print(row)