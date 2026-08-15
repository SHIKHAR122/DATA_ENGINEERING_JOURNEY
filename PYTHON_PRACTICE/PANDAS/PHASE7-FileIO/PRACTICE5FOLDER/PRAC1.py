from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:ssvtforever%402205@localhost:5432/practice")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM stations"))
    for row in result:
        print(row)