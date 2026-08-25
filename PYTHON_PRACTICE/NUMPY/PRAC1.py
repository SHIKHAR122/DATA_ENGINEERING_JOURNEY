# ============================================
# NUMPY PRACTICE - DAY 1
# Date: 20 August 2026
# Topics: ndarray, array, ndim, shape, size,
# dtype, array creation, data types
# Integrated with: OOP, Pandas, Exception Handling
# ============================================

import numpy as np
import pandas as pd

# ============================================
# QUESTION 1 - Array Inspection Drill
# No class needed - pure NumPy fundamentals
#
# Create the following arrays:
# a) 1D array of train delay minutes:
#    [25, 0, 45, 10, 55, 0, 30, 15, 60, 5]
# b) 2D array of shape (3, 4) filled with zeros
#    representing 3 stations, 4 time slots
# c) Array of 8 evenly spaced values between 0 and 24
#    representing hours of the day
# d) Random integer array of shape (5, 3)
#    values between 0 and 120 (delay range)
#
# For EACH array print:
# - the array itself
# - ndim, shape, size, dtype
# - memory usage in bytes using .nbytes
#
# Then answer in comments:
# - Why does array (b) default to float64 not int?
# - What is the step size in array (c)?
# - How much memory does array (d) use and why?

# YOUR CODE HERE:
arr_1d=np.array([25, 0, 45, 10, 55, 0, 30, 15, 60, 5])
print(arr_1d)
stations = np.zeros((3,4))
print(stations)
arr2=np.linspace(0,24,num=8)
print(arr2)
ran_arr = np.random.randint(0,121, size=(5,3))
print(ran_arr)

# ============================================
# QUESTION 2 - dtype Conversion + Memory
# A railway pipeline receives delay data as strings
# from an API response. You need to convert and
# optimize for memory before loading into PostgreSQL.

raw_api_data = {
    "train_no": ["12301", "12302", "12303", "12304", "12305"],
    "delay_minutes": ["25", "0", "45", "10", "55"],
    "speed_kmph": ["120.5", "80.0", "95.3", "110.2", "75.8"],
    "is_late": ["True", "False", "True", "False", "True"]
}

# Build a class DataTypeOptimizer with:
# - Method convert() that:
#       converts delay_minutes to np.int32
#       converts speed_kmph to np.float32
#       converts is_late to np.bool_
#       returns a dict of converted numpy arrays
# - Method memory_report() that:
#       prints dtype and nbytes for each converted array
#       prints total memory used across all arrays
# - Method validate() that:
#       raises ValueError if any delay is negative
#       raises ValueError if any speed is zero or negative
#       prints "Data validated" if all checks pass

# YOUR CODE HERE:
import numpy as np

raw_api_data = {
    "train_no": ["12301", "12302", "12303", "12304", "12305"],
    "delay_minutes": ["25", "0", "45", "10", "55"],
    "speed_kmph": ["120.5", "80.0", "95.3", "110.2", "75.8"],
    "is_late": ["True", "False", "True", "False", "True"]
}


class DataTypeOptimizer:
    def __init__(self, data):
        self.data = data
        self.converted_data = {}

    def convert(self):

        self.converted_data["delay_minutes"] = np.array(  self.data["delay_minutes"], dtype=np.int32)
        self.converted_data["speed_kmph"] = np.array( self.data["speed_kmph"], dtype=np.float32)
        self.converted_data["is_late"] = np.array( [value == "True" for value in self.data["is_late"]], dtype=np.bool_)

        return self.converted_data

    def memory_report(self):
        if not self.converted_data:
            self.convert()
        total_memory = 0

        for name, array in self.converted_data.items():
            print(f"{name} → dtype: {array.dtype}, "f"memory: {array.nbytes} bytes")
            total_memory += array.nbytes
        print(f"Total memory used: {total_memory} bytes")

    def validate(self):
        if not self.converted_data:
            self.convert()
        delay = self.converted_data["delay_minutes"]
        speed = self.converted_data["speed_kmph"]
        if np.any(delay < 0):
            raise ValueError("Delay cannot be negative")
        if np.any(speed <= 0):
            raise ValueError("Speed must be greater than zero")
        print("Data validated")

optimizer = DataTypeOptimizer(raw_api_data)
converted = optimizer.convert()
print(converted)
optimizer.memory_report()
optimizer.validate()



# ============================================
# QUESTION 3 - NumPy + Pandas Integration
# A station master wants daily statistics on
# train delays. Data comes in as a Pandas DataFrame
# but all heavy calculations must use NumPy.

delay_data = pd.DataFrame({
    "train_no": ["12301", "12302", "12303",
                "12304", "12305", "12306"],
    "delay_minutes": [25, 0, 45, 10, 55, 0],
    "platform": [1, 2, 1, 3, 2, 1],
    "passengers": [450, 320, 280, 510, 390, 260]
})

# Build a class StationStats with:
# - Method extract_arrays() that:
#       extracts delay_minutes as np.int32 array
#       extracts passengers as np.int32 array
#       returns both arrays
# - Method delay_stats() that:
#       uses np.mean(), np.median(), np.std(),
#       np.min(), np.max() on delay array
#       returns a dict of all five stats
#       rounded to 2 decimal places
# - Method flag_delayed(threshold) that:
#       uses boolean indexing on the delay array
#       returns train numbers where delay > threshold
# - Method add_stats_to_df() that:
#       adds "delay_zscore" column to the DataFrame
#       zscore = (delay - mean) / std
#       calculate mean and std using NumPy
#       positive zscore = delayed more than average
#       negative zscore = less than average
#       return the updated DataFrame

# YOUR CODE HERE:
class StationStats:
    def __init__(self , df):
        self.df=df

    def extract_arrays(self):
        delay_array= self.df["delay_minutes"].to_numpy(dtype=np.int32)
        passenger_array = self.df["passengers"].to_numpy(dtype=np.int32)
        return delay_array , passenger_array

    def delay_stats(self):
        delay_array  , _ =  self.extract_arrays()
        mean=np.mean(delay_array)
        median=np.median(delay_array)
        std=np.std(delay_array)
        minimum=np.min(delay_array)
        maximum=np.min(delay_array)


        return {
            "mean": round(mean, 2),
            "median": round(median, 2),
            "std": round(std, 2),
            "min": round(minimum, 2),
            "max": round(maximum, 2)
        }

    def flagged_delays(self , threshold):
        delay_array , _  = self.extract_arrays()
        delayed_mask = delay_array > threshold
        train_numbers = self.df["train_no"].to_numpy()
        
# ============================================
# QUESTION 4 - HARDEST - Full Pipeline Simulation
# Simulate one fetch cycle of the Railway Tracker.
# Raw data arrives, gets converted to NumPy arrays,
# analyzed, then loaded into a Pandas DataFrame
# for PostgreSQL insertion.

np.random.seed(42)
raw_trains = {
    "train_no": [f"1230{i}" for i in range(1, 11)],
    "scheduled_minutes": np.random.randint(0, 1440, size=10),
    "actual_minutes": np.random.randint(0, 1440, size=10),
    "passengers": np.random.randint(100, 600, size=10),
    "platform": np.random.randint(1, 6, size=10)
}

# Build a class FetchCyclePipeline with:
# - Method compute_delays() that:
#       calculates delay = actual_minutes - scheduled_minutes
#       stores as np.int32 array
#       negative delays treated as 0 (early arrival = no delay)
#       hint: use np.maximum(delay_array, 0)
# - Method classify_delays() that:
#       uses np.where() to classify:
#       delay == 0 -> "On Time"
#       delay <= 15 -> "Slight Delay"
#       delay <= 60 -> "Moderate Delay"
#       delay > 60 -> "Severe Delay"
#       returns array of classifications
# - Method platform_summary() that:
#       for each unique platform number
#       calculates average delay using NumPy
#       returns dict: {platform: avg_delay}
# - Method build_dataframe() that:
#       combines everything into a clean DataFrame
#       with columns: train_no, delay_minutes,
#       delay_class, platform, passengers
# - Method run() that calls all methods and
#       prints a complete fetch cycle report

# YOUR CODE HERE: