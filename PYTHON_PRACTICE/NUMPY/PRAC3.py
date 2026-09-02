# # ============================================
# # NUMPY PRACTICE - PHASE 1-3 REVIEW
# # Topics: ndarray, array creation, dtype,
# # indexing/slicing, boolean indexing,
# # arithmetic, comparison, aggregation
# # (mean, median, std, var, argmin, argmax)
# # Integrated with: OOP, Pandas
# # ============================================

import numpy as np
import pandas as pd

# # ============================================
# # QUESTION 1 - Array Creation + Multi-dim Indexing
# # No class needed - pure fundamentals

# # Create a 2D array of shape (5, 4) representing
# # 5 trains x 4 stations, with random delay minutes
# # between 0 and 90 (use np.random.randint, seed=10)

# # Then:
# # a) Print ndim, shape, size, dtype
# # b) Slice out only the last 2 columns (last 2 stations)
# # c) Slice out only the first 3 rows (first 3 trains)
# # d) Get the delay of train index 2 at station index 3
# #    using 2D indexing (not chained indexing)
# # e) Reverse the row order using slicing (no loops)

# # YOUR CODE HERE:
# np.random.seed(10)

# delays = np.random.randint(0,91,size=(5,4))
# print("\nTHE ARRAY GENERATED IS : \n" ,delays)


# print("NDIM OF THE ARRAY ",delays.ndim)
# print("SHAPE OF THE ARRAY ",delays.shape)
# print("SIZE OF THE ARRAY ", delays.size)
# print("DTYPE OF THE ARRAY ", delays.dtype)

# print("\nTHE LAST TWO COLUMNS OF THE ARRAY :\n" , delays[:,-2:])
# print("\nTHE FIRST THREE ROWS OF THE ARRAY ARE :\n",delays[:3,:])
# print("\n THE DELAY OF TRAIN INDEX 2 AT STATION INDEX 3 IS : \n" , delays[2,3])
# print("\nTHE REVERSED ORDER OF THE MATRIX IS : \n", delays[::-1 , :])
# ============================================
# QUESTION 2 - Boolean Indexing + Conditional Selection
# A dispatcher wants to filter trains by delay severity.

delay = np.array([12, 0, 45, 78, 5, 90, 33, 0, 60, 22])
train_ids = np.array(["T1","T2","T3","T4","T5",
                       "T6","T7","T8","T9","T10"])

# Build a class DelayFilter with:
# - Method on_time() that:
#       returns train_ids where delay == 0
# - Method moderate_to_severe() that:
#       returns train_ids where delay is between
#       30 and 90 (inclusive) using a combined
#       boolean condition (logical AND, not two steps)
# - Method not_on_time_or_severe() that:
#       returns train_ids where delay != 0
#       AND delay < 90, using logical NOT / comparison
#       operators (~, !=) — no plain Python if/else
# - Method summary() that:
#       prints count of trains in each category above

# YOUR CODE HERE:
class DelayFilter:

    def __init__(self, train_ids, delay):
        self.train_ids = train_ids
        self.delay = delay

    def on_time(self):
        return self.train_ids[self.delay == 0]

    def moderate_to_severe(self):
        return self.train_ids[(self.delay >= 30) & (self.delay <= 90)]

    def not_on_time_or_severe(self):
        return self.train_ids[(self.delay != 0) & (self.delay < 90)]

    def summary(self):
        on_time_count = np.sum(self.delay == 0)

        moderate_to_severe_count = np.sum(
            (self.delay >= 30) & (self.delay <= 90)
        )

        not_on_time_or_severe_count = np.sum(
            (self.delay != 0) & (self.delay < 90)
        )

        print("On-time trains:", on_time_count)
        print("Moderate to severe:", moderate_to_severe_count)
        print("Not on-time and delay < 90:", not_on_time_or_severe_count)


filter_obj = DelayFilter(train_ids, delay)

print(filter_obj.on_time())
print(filter_obj.moderate_to_severe())
print(filter_obj.not_on_time_or_severe())

filter_obj.summary()
# ============================================
# QUESTION 3 - Arithmetic + Aggregation Stats
# Compare scheduled vs actual arrival times.

scheduled = np.array([600, 630, 700, 730, 800, 830])
actual    = np.array([605, 630, 715, 725, 850, 828])
train_no  = np.array(["12301","12302","12303",
                       "12304","12305","12306"])

# Build a class ArrivalAnalyzer with:
# - Method compute_delay() that:
#       returns actual - scheduled as a NumPy array
#       (element-wise arithmetic)
# - Method stats(self, delay_array) that:
#       returns a dict with mean, median, std, var
#       all rounded to 2 decimals
# - Method most_delayed(self, delay_array) that:
#       uses np.argmax() to find the INDEX of the
#       worst delay, then returns the train_no
#       at that index (not the delay value itself)
# - Method most_on_time(self, delay_array) that:
#       uses np.argmin() the same way to return
#       the train_no with smallest delay
#       (careful: smallest delay could be negative,
#        meaning early arrival — explain in a comment
#        what a negative delay means here)

# YOUR CODE HERE:
class ArrivalAnalyzer:
    def __init__(self , scheduled , actual , train_no ):
        self.scheduled=scheduled
        self.actual=actual
        self.train_no=train_no

    def compute_delay(self):
        delay_array=self.actual - self.scheduled
        return delay_array 

    def stats(self , delay_array):
        delay_stats = {
        "mean": round(np.mean(delay_array),2),
        "median": round(np.median(delay_array),2),
        "std": round(np.std(delay_array),2),
        "var": round(np.var(delay_array),2)
    }
        return delay_stats

    def most_delayed(self, delay_array):
        return self.train_no[np.argmax(delay_array)]

    def most_on_time(self,delay_array):
        return self.train_no[np.argmin(delay_array)]
        
    
aa=ArrivalAnalyzer(scheduled , actual , train_no)
print(aa.compute_delay())
print(aa.stats(delay_array=delay))
print("THE MOST DELAYED TRAIN IS : " , aa.most_delayed(delay_array=delay))
print("THE MOST PUNCTUAL TRAIN IS : ",aa.most_on_time(delay_array=delay))
# ============================================
# QUESTION 4 - HARDEST - NumPy + Pandas Combined
# A weekly report needs both filtering and stats,
# pulling data out of a Pandas DataFrame into NumPy
# for the actual computation.

weekly_data = pd.DataFrame({
    "train_no": ["12301","12302","12303","12304",
                 "12305","12306","12307","12308"],
    "day": ["Mon","Mon","Tue","Tue",
            "Wed","Wed","Thu","Thu"],
    "delay_minutes": [10, 0, 65, 20, 5, 90, 15, 0],
    "platform": [1, 2, 1, 3, 2, 4, 1, 3]
})

# Build a class WeeklyReport with:
# - Method get_delay_array() that:
#       extracts delay_minutes column as np.int32 array
# - Method platform_filter(self, platform_no) that:
#       uses boolean indexing on the DataFrame's
#       platform column (convert to NumPy first)
#       to return train_no values for that platform
# - Method weekly_stats() that:
#       returns mean, std, argmax train_no,
#       argmin train_no for the whole week
#       (reuse logic pattern from Question 3)
# - Method comparison_matrix() that:
#       creates a 2D boolean array comparing every
#       delay against every other delay using
#       broadcasting: delay_array[:, None] > delay_array

# YOUR CODE HERE:
class WeeklyReport:
    def __init__(self , weekly_data):
        self.weekly_data=weekly_data

    def get_delay_array(self):
        delay_minutes= self.weekly_data["delay_minutes"].to_numpy(dtype="int32")
        return delay_minutes

    def platform_filter(self,platform_no):
        platform=self.weekly_data["platform"].to_numpy(dtype="int32")
        train_no=self.weekly_data["train_no"].to_numpy(dtype="int32")

        return train_no[platform==platform_no]

    def weekly_stats(self):
        delay=self.get_delay_array()
        stats={
            "mean": np.mean(delay) , 
            "median":np.median(delay) , 
            "std":np.std(delay) , 
            "variance":np.var(delay)
        }
        return stats

    def comparison_matrix(self):
        delay_array = self.get_delay_array()
        return delay_array[:, None] > delay_array



wr=WeeklyReport(weekly_data)
print("THE DELAYED ARRAY IS :",wr.get_delay_array())
print("THE PLATFORMS FOR THE GIVEN TRAIN NUMBER ARE : " , wr.platform_filter(1))
print("\n THE WEEKLY STATS OF THE STATION IS : \n",wr.weekly_stats())
print("\n THE COMPARISON MATRIX FOR THE GIVEN DATA IS : \n" ,wr.comparison_matrix())