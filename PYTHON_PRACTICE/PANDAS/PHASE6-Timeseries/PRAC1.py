# ============================================
# PANDAS PHASE 4 — Time Series
# Date: 29 July 2026
# Focus: resample(), date_range(), datetime ops
# Integrated with: OOP, groupby, apply
# ============================================

import pandas as pd
import numpy as np

daily_sales = pd.DataFrame({
    "date": pd.date_range(start="2026-01-01", end="2026-06-30", freq="D"),
    "revenue": np.random.randint(5000, 50000, size=181),
    "orders": np.random.randint(10, 200, size=181),
    "category": np.random.choice(["Electronics", "Clothing", "Food"], size=181)
})

# Build a class SalesTimeSeries with:
#
# - Method monthly_revenue() that:
#       resamples daily revenue to monthly totals
#       using resample("ME", on="date")
#       returns monthly sum of revenue and orders
#
# - Method best_month() that:
#       returns the month with highest total revenue
#
# - Method add_time_features() that adds:
#       year, month_name, weekday_name, quarter
#       using dt accessor
#
# - Method weekend_vs_weekday() that:
#       adds "day_type" column:
#       "Weekend" if weekday >= 5 else "Weekday"
#       returns average revenue for each day_type
#       using groupby
#
# - Method date_range_filter(start, end) that:
#       takes two date strings like "2026-02-01"
#       returns only rows within that date range
#       using boolean filtering on the date column
#
# - Method run() that calls all methods and
#       prints a clean time series report

# YOUR CODE HERE:


class SalesTimeSeries :
    def __init__(self ,daily_sales):
        self.daily_sales=daily_sales

    def monthly_revenue(self):
        monthly=(daily_sales.resample("ME" , on="date")["revenue"].sum())


        return monthly



st=SalesTimeSeries(daily_sales)
print("\n \n" , st.monthly_revenue())