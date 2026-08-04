# ============================================
# PANDAS PHASE 4 — DateTime Deep Dive
# Date: 30 July 2026
# Integrated with: OOP, merge, groupby, apply
# ============================================

import pandas as pd
import numpy as np

# ============================================
# QUESTION 1 — Date Differences and Durations
# A logistics company tracks shipment data.

shipments = pd.DataFrame({
    "shipment_id": [1, 2, 3, 4, 5, 6, 7],
    "order_date": ["2026-01-05", "2026-01-12", "2026-02-01",
                  "2026-02-15", "2026-03-10", "2026-03-22", "2026-04-01"],
    "delivery_date": ["2026-01-08", "2026-01-20", "2026-02-05",
                     "2026-02-18", "2026-03-15", "2026-04-01", "2026-04-10"],
    "courier": ["BlueDart", "Delhivery", "BlueDart",
               "Ekart", "Delhivery", "BlueDart", "Ekart"],
    "amount": [5000, 3000, 8000, 2500, 6000, 4500, 7000]
})

# Build a class ShipmentAnalyzer with:
# - Method process() that:
#       converts order_date and delivery_date to datetime
#       adds "delivery_days" = delivery_date - order_date
#       extracts just the integer number of days
#       adds "order_month" and "order_weekday"
# - Method avg_delivery_by_courier() that:
#       returns average delivery days per courier
# - Method late_shipments(threshold_days) that:
#       returns shipments that took more than
#       threshold_days to deliver
# - Method monthly_shipment_count() that:
#       returns number of shipments per month
# - Method run()

# YOUR CODE HERE:
df=pd.DataFrame(shipments)
class ShipmentAnalyzer:

    def __init__(self, df):
        self.df = df

    def process(self):

        self.df["order_date"] = pd.to_datetime(self.df["order_date"])
        self.df["delivery_date"] = pd.to_datetime(self.df["delivery_date"])
        self.df["delivery_days"] = (self.df["delivery_date"] - self.df["order_date"]).dt.days
        self.df["order_month"] = self.df["order_date"].dt.month
        self.df["order_weekday"] = self.df["order_date"].dt.weekday
        return self.df

    def avg_delivery_by_courier(self):
        self.process()      
        self.df["average_delivery_days"] = (  self.df.groupby("courier")["delivery_days"] .transform("mean"))
        return self.df

    def delivered_after(self, date):
        df = self.process()
        date = pd.to_datetime(date)
        return df[df["delivery_date"] > date]


    
sa=ShipmentAnalyzer(df)
print("\nTHE DATA AFTER PROCESSING IS : \n",sa.process())
print("\n THE AVERAGE DELIVERY DAYS PER COURIER IS : \n" ,sa.avg_delivery_by_courier())
print("\n THE DETAILS OF DELIVERY THAT TOOK PART AFTER THE THRESHOLD DATE IS :\n" ,sa.delivered_after("2026-02-28"))
# ============================================
# QUESTION 2 — resample() Advanced
dates = pd.date_range(start="2026-01-01", end="2026-06-30", freq="B")
n = len(dates)
stock_data = pd.DataFrame({
    "date": dates,
    "stock": np.random.choice(["RELIANCE", "TCS", "INFOSYS"], size=n),
    "open_price": np.random.randint(1000, 5000, size=n),
    "close_price": np.random.randint(1000, 5000, size=n),
    "volume": np.random.randint(100000, 1000000, size=n)
})

# Build a class StockAnalyzer with:
# - Method daily_return() that:
#       adds "daily_return" column:
#       ((close_price - open_price) / open_price) * 100
#       rounded to 2 decimal places
# - Method weekly_summary() that:
#       resamples to weekly frequency using "W"
#       returns mean close_price and sum volume per week
# - Method monthly_summary() that:
#       resamples to monthly using "ME"
#       returns mean open, mean close, sum volume
# - Method best_trading_day() that:
#       returns the date with highest volume

# YOUR CODE HERE:
df2=pd.DataFrame(stock_data)

class StockAnalyzer:
    def __init__(self,df2):
        self.df2=df2


    def daily_returns(self):
        df2["daily_return"]=((df2["close_price"]-df2["open_price"]/df2["open_price"])*100)
        return df2


    def weekly_summary(self):
        weekly_dataframe=df2.resample("W", on="date").agg({"open_price":"mean","close_price":"mean" , "volume":"sum"})
        return weekly_dataframe


    def monthly_summary(self):
        monthly_dataframe=df2.resample("ME",on="date").agg({"open_price":"mean","close_price":"mean" , "volume":"sum"})
        return monthly_dataframe

    def best_trading_day(self):
        best_day=df2["volume"].idxmax()

        return df2.loc[best_day]

sa=StockAnalyzer(df2)
print("\nTHE DAILY RETURN FOR THE GIVEN STOCK DATA IS: \n",sa.daily_returns())
print("\n THE WEEKLY REPORT FOR THE GIVEN STOCK DATA IS :\n",sa.weekly_summary())
print("\n THE MONTHLY REPORT FOR THE GIVEN STOCK DATA IS :\n",sa.monthly_summary())
print("\n THE BEST TO TRADE IS :\n",sa.best_trading_day())
# ============================================
# QUESTION 3 — DateTime Filtering + Merging
# An e-commerce platform has order and
# customer data with time-based analysis needed.

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "customer_id": [101, 102, 101, 103, 102, 104, 101, 103, 104, 102],
    "amount": [5000, 3000, 8000, 2000, 6000, 4000, 7000, 3500, 5500, 2500],
    "order_date": ["2026-01-10", "2026-01-25", "2026-02-05",
                  "2026-02-20", "2026-03-01", "2026-03-15",
                  "2026-04-10", "2026-04-22", "2026-05-05", "2026-05-18"]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "name": ["Shikhar", "Rahul", "Priya", "Aditya"],
    "city": ["Delhi", "Mumbai", "Delhi", "Kanpur"],
    "signup_date": ["2025-12-01", "2025-11-15",
                   "2026-01-01", "2025-10-20"]
})


# # # Build a class CustomerOrderAnalyzer with:
# # - Method prepare() that:
# #       merges orders with customers on customer_id
# #       converts order_date and signup_date to datetime
# #       adds "days_since_signup" =
# #       order_date - signup_date as integer days
# #       adds order_month, order_quarter
# # - Method q1_orders() that:
# #       returns only orders placed in Q1 2026
# #       (January, February, March)
# # - Method customer_lifetime_spend() that:
# #       returns total spend per customer
# #       sorted descending
# # - Method monthly_city_revenue() that:
# #       returns total revenue per city per month
# #       using groupby on both city and order_month
# # - Method early_vs_late_adopters() that:
# #       customers who signed up before 2026
# #       are "Early" adopters
# #       customers who signed up in 2026 or after
# #       are "Late" adopters
# #       returns average spend per adopter type
# # - Method run()

# # YOUR CODE HERE:
class CustomerOrderAnalyzer:

    def __init__(self, customers, orders):
        self.customers = customers
        self.orders = orders

    def prepare(self):
        self.merged_df = pd.merge(  self.orders,  self.customers, on="customer_id",how="left")
        self.merged_df["order_date"] = pd.to_datetime(self.merged_df["order_date"])
        self.merged_df["signup_date"] = pd.to_datetime(self.merged_df["signup_date"])
        self.merged_df["days_since_signup"] = (self.merged_df["order_date"] - self.merged_df["signup_date"]).dt.days
        self.merged_df["month"] = self.merged_df["order_date"].dt.month
        self.merged_df["quarter"] = self.merged_df["order_date"].dt.quarter

        return self.merged_df

    def q1_orders(self):
        quarter1_orders_df = self.prepare()
        quarter1_orders_df = quarter1_orders_df[quarter1_orders_df["quarter"] == 1]
        return quarter1_orders_df

    def customer_lifetime_spend(self):
        self.data=self.q1_orders()
        self.data=self.data.groupby("customer_id")["amount"].sum().sort_values(ascending=False)
        return self.data

    def monthly_city_revenue(self):
        self.revenue=self.prepare()
        self.revenue=self.revenue.groupby(["city","month"])["amount"].sum().reset_index()
        return self.revenue

    def early_vs_late_adopters(self):
        df = self.prepare()
        df["adopter_type"] = df["signup_date"].apply( lambda x: "Early" if x.year < 2026 else "Late")
        result = ( df.groupby("adopter_type")["amount"].mean().reset_index())
        return  result 


        
coa=CustomerOrderAnalyzer(customers=customers , orders=orders)
print("\n THE MERGED DATA FRAME IS : \n",coa.prepare())
print("\n THE QUARTERLY DATA FROM THE DATA FRAME IS : \n",coa.q1_orders())
print("\n THE TOTAL SPEND PER CUSTOMER IS : \n",coa.customer_lifetime_spend())
print("\n THE REVENUE GENERATED IN EACH CITY PER MONTH IS : \n",coa.monthly_city_revenue())
print("\n THE ADOPT STYLE OF EACH CUSTOMER ALONG WITH THEIR AVERAGE IS :\n",coa.early_vs_late_adopters())
# # ============================================
# # QUESTION 4 — HARDEST — Full Time Series Pipeline
# # A SaaS company tracks user activity daily.
# # Build a complete time series analytics system.

np.random.seed(42)
user_activity = pd.DataFrame({
    "activity_id": range(1, 201),
    "user_id": np.random.choice([1001, 1002, 1003, 1004, 1005], size=200),
    "activity_date": pd.date_range(
        start="2026-01-01", periods=200, freq="D"
    )[:200],
    "activity_type": np.random.choice(
        ["login", "purchase", "support_ticket"], size=200
    ),
    "revenue": np.where(
        np.random.choice(["purchase", "other"], size=200) == "purchase",
        np.random.randint(1000, 20000, size=200),
        0
    )
})

users = pd.DataFrame({
    "user_id": [1001, 1002, 1003, 1004, 1005],
    "username": ["Shikhar", "Rahul", "Priya", "Aditya", "Sneha"],
    "plan": ["Pro", "Free", "Pro", "Enterprise", "Free"],
    "signup_date": ["2025-10-01", "2025-11-15",
                   "2025-12-01", "2025-09-01", "2026-01-01"]
})

# # Build a class SaaSAnalytics with:
# # - Method prepare() that:
# #       merges activity with users on user_id
# #       converts activity_date and signup_date to datetime
# #       adds days_active = activity_date - signup_date as int
# #       adds month, quarter, weekday_name
# # - Method activity_trend() that:
# #       resamples to monthly using "ME"
# #       returns count of each activity_type per month
# #       hint: groupby month + activity_type, then count
# # - Method revenue_by_plan() that:
# #       returns total revenue per user plan
# #       only count rows where revenue > 0
# # - Method weekly_active_users() that:
# #       resamples to weekly "W"
# #       counts unique user_ids per week
# # - Method churn_risk_flag() that:
# #       finds the last activity date per user
# #       adds "days_since_last_activity" =
# #       max(activity_date) - last_activity per user
# #       flags users as "At Risk" if
# #       days_since_last_activity > 30 else "Active"
# # - Method peak_activity_day() that:
# #       returns which weekday has the highest
# #       average number of activities
# # - Method run()

class SaaSAnalytics :
    def __init__(self , user_activity , users):
        self.users=users
        self.user_activity=user_activity


    def prepare(self):
        
 