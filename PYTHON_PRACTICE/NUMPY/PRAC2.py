
# --- NUMPY PRACTICE SESSION 2 (31 AUGUST 2026)

# You have sales data for 5 products across 4 days:

import numpy as np
sales = np.array([
    [120, 85, -1, 300],
    [45, -5, 60, 200],
    [999, 150, 75, -2],
    [30, 40, 55, 65],
    [-10, 200, 300, 400]
])

# Do the following, in order:

# 1. Get the sales for **product at row index 2** (all 4 days).
# 2. Get the sales for **day 1 (second column)** across all products.
# 3. Using boolean indexing, replace **all negative values** in the whole array with `np.nan` (remember what needs to happen to the array's dtype first).
# 4. Using fancy indexing, select only **rows 0, 2, and 4** (i.e. product 1, 3, and 5) into a new array.

# ---

# Write out your code for all four and I'll check it.

# CODE HERE : 

#  TO GET THE SALES FOR THE PRODUCT AT ROW INDEX 2 - 
print(sales[2])

# GET THE SALES FOR THE DAY 1 ACROSS ALL PRODUCTS



# USING BOOLEAN FILTERING , REPLACE ALL -VE VALUES
sales = np.array([
    [120, 85, -1, 300],
    [45, -5, 60, 200],
    [999, 150, 75, -2],
    [30, 40, 55, 65],
    [-10, 200, 300, 400]
], dtype=float) 
sales[sales<0]=np.nan
print(sales)  



# USING FANCY INDEXING SELECT ONLY ROW 0 , 2 AND 4 INTO A NEW ARRAY

data=sales[[0,2,4]]
print("\n THE NEW ARRAY UISNG FANCY INDEXING IS : \n" , data)





# --- NUMPY PRACTICE SESSION 2 (31 AUGUST 2026)

# You have sales data for 5 products across 4 days:

import numpy as np
sales = np.array([
    [120, 85, -1, 300],
    [45, -5, 60, 200],
    [999, 150, 75, -2],
    [30, 40, 55, 65],
    [-10, 200, 300, 400]
])

# Do the following, in order:

# 1. Get the sales for **product at row index 2** (all 4 days).
# 2. Get the sales for **day 1 (second column)** across all products.
# 3. Using boolean indexing, replace **all negative values** in the whole array with `np.nan` (remember what needs to happen to the array's dtype first).
# 4. Using fancy indexing, select only **rows 0, 2, and 4** (i.e. product 1, 3, and 5) into a new array.

# ---

# Write out your code for all four and I'll check it.

# CODE HERE : 

#  TO GET THE SALES FOR THE PRODUCT AT ROW INDEX 2 - 
print(sales[2])


# USING BOOLEAN FILTERING , REPLACE ALL -VE VALUES
sales = np.array([
    [120, 85, -1, 300],
    [45, -5, 60, 200],
    [999, 150, 75, -2],
    [30, 40, 55, 65],
    [-10, 200, 300, 400]
], dtype=float) 
sales[sales<0]=np.nan
print(sales)  



# USING FANCY INDEXING SELECT ONLY ROW 0 , 2 AND 4 INTO A NEW ARRAY

data=sales[[0,2,4]]
print("\n THE NEW ARRAY UISNG FANCY INDEXING IS : \n" , data)



# --- NUMPY PRACTICE SESSION 3 (INTERVIEW-STYLE QUESTIONS) ---

import numpy as np

# ============================================
# Q1 — Handling missing data (very common interview ask)
# ============================================
readings = np.array([23.5, np.nan, 19.2, np.nan, 25.1, 30.0])

# a) Count how many nan values are in the array.
reading_count=np.count_nonzero(readings)
print("THERE ARE {} VALUES IN THE GIVEN DATA SET".format(reading_count))

# b) Compute the mean of the array IGNORING the nan values.
mean_data= np.nanmean(readings)
print("\n THE MEAN OF THE GIVEN DATA IS {} \n".format(mean_data))

# c) Replace all nan values with the mean you just computed.
mean_val = np.nanmean(readings)      # from part (b)
readings[np.isnan(readings)] = mean_val
print("THE UPDATED DATA SET AFTER REPLACING nan WITH THE MEAN OF THE DATA SET IS : \n",readings)
# ============================================
# Q2 — Conditional business logic
# ============================================
revenue = np.array([12000, 8500, 15000, 6200, 21000, 9800, 17500])

# a) How many days had revenue above ₹10,000?
mask= revenue>10000
print("\n THERE ARE {} DAYS WHICH HAD REVENUE ABOVE 10000 ".format(np.count_nonzero(revenue[mask])) )

# b) Get the revenue values only for days above the average revenue.
average_revenue=np.average(revenue)
print("THE AVG REVENUE IN THE GIVEN DATA SET IS : " , average_revenue)
mask = revenue>average_revenue
print("\n THE REVENUE VALUES FOR THE DAYS ABOVE THE AVERAGE REVENUE ARE : \n"  , revenue[mask])
# c) Create a new array where every value below ₹10,000 is flagged as 0 (low)
#    and everything else stays unchanged — do this WITHOUT a for loop.
new_data=np.where(revenue>=10000 , revenue ,  0)
print("\n THE NEW UPDATED DATA SET IS : \n",new_data)

# ============================================
# Q3 — 2D reshaping (common "explain your thinking" question)
# ============================================
temps = np.arange(72)  # placeholder values 0-71, hourly readings over 3 days

# a) Reshape this into a (3, 24) array representing 3 days x 24 hours.


# b) Get all readings for DAY 2 only.


# c) Get the reading at HOUR 15 on DAY 1.


# d) Find the average temperature PER DAY.
#    (hint: think about which axis you're averaging over)

