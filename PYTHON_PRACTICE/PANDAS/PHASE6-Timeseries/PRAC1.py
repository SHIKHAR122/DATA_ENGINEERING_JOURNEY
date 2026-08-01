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


# YOUR CODE HERE:


df=pd.DataFrame(daily_sales)
print(df.head(11))


class SalesTimeSeries:

    def __init__(self, df):
        self.df = df

    def monthly_revenue(self):
        return (self.df.resample("ME", on="date")[["revenue","orders"]].sum())

    def best_month(self):
        monthly = self.monthly_revenue()
        return monthly["revenue"].idxmax()

    def add_time_features(self):
        self.df["date"] = pd.to_datetime(self.df["date"])
        self.df["year"] = self.df["date"].dt.year
        self.df["month_name"] = self.df["date"].dt.month_name()
        self.df["weekday_name"] = self.df["date"].dt.day_name()
        self.df["weekday"] = self.df["date"].dt.weekday
        self.df["quarter"] = self.df["date"].dt.quarter

        return self.df

    def weekend_vs_weekday(self):
        df = self.add_time_features()
        df["day_type"] = df["weekday"].apply( lambda x: "Weekend" if x >= 5 else "Weekday")

        return df.groupby("day_type")["revenue"].mean()


    def date_range_filter(self, start, end):

        df = self.df.copy()
        df["date"] = pd.to_datetime(df["date"])
        filtered_df = df[(df["date"] >= start) & (df["date"] <= end)]
        return filtered_df

        


    def run(self):
        print("MONTHLY REVENUE:\n", self.monthly_revenue())
        print("BEST MONTH:", self.best_month())
        print("TIME FEATURES:\n", self.add_time_features())
        print("WEEKEND VS WEEKDAY:\n", self.weekend_vs_weekday())
        print("DATE FILTER:\n", self.date_range_filter("2026-02-01", "2026-04-30"))



sc=SalesTimeSeries(df)
print(sc.run())