# ============================================
# PANDAS PHASE 6 — SQL + Pandas Integration
# Date: 11  August 2026
# Topics: to_sql, read_sql, chunksize,
# if_exists, text(), parameterized queries,
# engine.connect() for UPDATE/DELETE
# Integrated with: OOP, Exception Handling,
# groupby, apply, datetime
# ============================================

import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


# ============================================
# QUESTION — Railway Pre-Pipeline Simulation
#
# This question simulates exactly what your
# Railway Tracker project will do in September.
# Master this and the project becomes easy.
#
# You have raw train delay data coming in
# every 30 minutes from an API.
# Build a complete database pipeline for it.

raw_batch_1 = pd.DataFrame({
    "train_no": ["12301", "12302", "12303",
                 "12304", "12305"],
    "train_name": ["Rajdhani", "Shatabdi", "Duronto",
                   "Garib Rath", "Jan Shatabdi"],
    "source": ["Delhi", "Mumbai", "Kolkata",
               "Delhi", "Chennai"],
    "destination": ["Mumbai", "Delhi", "Delhi",
                   "Kolkata", "Delhi"],
    "scheduled_time": ["06:00", "07:30", "08:00",
                      "09:15", "10:00"],
    "actual_time": ["06:25", "07:30", "08:45",
                   "09:15", "10:55"],
    "delay_minutes": [25, 0, 45, 0, 55],
    "fetch_timestamp": [datetime.now()] * 5
})

raw_batch_2 = pd.DataFrame({
    "train_no": ["12306", "12307", "12301",
                 "12308", "12309"],
    "train_name": ["Express", "SuperFast", "Rajdhani",
                   "Mail", "Passenger"],
    "source": ["Delhi", "Pune", "Delhi",
               "Mumbai", "Kolkata"],
    "destination": ["Chennai", "Delhi", "Mumbai",
                   "Delhi", "Delhi"],
    "scheduled_time": ["11:00", "12:30", "14:00",
                      "15:15", "16:00"],
    "actual_time": ["11:00", "13:15", "14:50",
                   "16:00", "16:00"],
    "delay_minutes": [0, 45, 50, 105, 0],
    "fetch_timestamp": [datetime.now()] * 5
})

# ============================================
# BUILD A CLASS RailwayPipeline with:
#
# METHOD 1 — load(df, batch_name)
# - Writes the DataFrame to "train_delays" table
# - First batch: if_exists="replace"
# - Subsequent batches: if_exists="append"
# - Prints how many rows were loaded
# - Catches any SQLAlchemy exceptions
#
# METHOD 2 — read_all()
# - Reads entire train_delays table
# - Returns as DataFrame
#
# METHOD 3 — read_by_route(source, destination)
# - Uses parameterized query with text()
# - Returns trains on that specific route
#
# METHOD 4 — read_delayed_only(threshold_minutes)
# - Returns only trains delayed more than
#   threshold_minutes using parameterized query
#
# METHOD 5 — read_in_chunks(chunksize)
# - Reads entire table in chunks
# - Calculates average delay across all chunks
#   without loading everything into memory at once
# - Returns the final average delay
#
# METHOD 6 — update_delay(train_no, new_delay)
# - Uses engine.connect() + text() to UPDATE
#   the delay_minutes for a specific train_no
# - Commits the change
# - Prints "Updated train_no delay to new_delay mins"
#
# METHOD 7 — summary_stats()
# - Reads full table using read_sql
# - Returns using groupby:
#       average delay per source station
#       count of delayed trains per destination
#       most delayed train (highest delay_minutes)
#
# METHOD 8 — run()
# - Load batch 1 with replace
# - Load batch 2 with append
# - Print all data using read_all()
# - Read Delhi to Mumbai route
# - Read trains delayed more than 30 minutes
# - Calculate average delay using chunks
# - Update train 12301 delay to 35
# - Print summary stats
# - Print final row count

# YOUR CODE HERE:


engine = create_engine("sqlite:///phase6_practice.db")

class RailwayPipeline:
    def __init__(self,engine):
        self.engine=engine


    def load(self , df , batch_name):
        try:
            if batch_name=="batch_1":
                df.to_sql("train_delays" , self.engine , if_exists="replace" , index=False )
            else:
                df.to_sql("train_delays" , self.engine , if_exists="append" , index=False)

            print(f"{batch_name} LOADED SUCCESSFULLY !!!!")
            print(f"{len(df)} ROWS ADDED  TO THE TABLE")
        except SQLAlchemyError as e:
            print(e)



    def read_all(self):
        train_data=pd.read_sql_query("SELECT * FROM train_delays" , self.engine  )
        return train_data 



    

    def read_by_route(self, source, destination):
        query = text(""" SELECT * FROM train_delays WHERE destination = :destination AND source = :source""")
        route_df = pd.read_sql(query,self.engine,params={"destination": destination,"source": source})
        return route_df



    def read_delayed_only(self,threshold_minutes):
        query=text("""SELECT * FROM train_delays WHERE delay_minutes > :threshold_minutes""")
        delayed_only_df=pd.read_sql(query , self.engine , params={"threshold_minutes":threshold_minutes})

        return delayed_only_df


    def read_in_chunks(self , chunksize):
        avg_delay=0
        total_delays=0
        total_rows=0
        for chunk in pd.read_sql("SELECT * FROM train_delays" , self.engine , chunksize=chunksize):
                total_delays+=chunk["delay_minutes"].sum()
                total_rows+=len(chunk)
                avg_delay=total_delays / total_rows
                print(f"Average delay = {avg_delay:.2f} minutes")

        return avg_delay



    def update_delays(self , new_delay , train_no):
            query=text(""" UPDATE train_delays SET delay_minutes = :new_delay WHERE train_no =  :train_no """)
            with self.engine.connect() as comm:
                 comm.execute(query , {
                      "new_delay": new_delay , 
                      "train_no":train_no
                 })
                 comm.commit()
            print(f"UPDATED THE DELAY TIME OF TRAIN NUMBER {train_no}  TO {new_delay} MINUTES ")


    def summarise_stats(self):
         read_data=pd.read_sql("SELECT * FROM train_delays" , self.engine )
         average_df=read_data.groupby("source")["delay_minutes"].mean()
         count_df=(read_data[read_data["delay_minutes"]>0].groupby("destination")["train_no"].count())
         most_delayed=read_data.loc[read_data["delay_minutes"].idxmax()]
         return average_df , count_df  , most_delayed 

    



    def run(self):

        self.load(raw_batch_1, "batch_1")
        self.load(raw_batch_2, "batch_2")

        print("\n========== ALL TRAIN DATA ==========")
        print(self.read_all())

        print("\n========== DELHI → MUMBAI ==========")
        print(self.read_by_route("Delhi", "Mumbai"))

        print("\n========== DELAYS > 30 MINUTES ==========")
        print(self.read_delayed_only(30))

        print("\n========== UPDATING TRAIN ==========")
        self.update_delays(50 , "12309")

        print("\n========== SUMMARY STATISTICS ==========")
        average_df, count_df, most_delayed = self.summarise_stats()
        print("\n--- Average Delay by Source Station ---")
        print(average_df)
        print("\n--- Number of Delayed Trains by Destination ---")
        print(count_df)
        print("\n--- Most Delayed Train ---")
        print(most_delayed)


pipeline = RailwayPipeline(engine)
pipeline.run()




    
        