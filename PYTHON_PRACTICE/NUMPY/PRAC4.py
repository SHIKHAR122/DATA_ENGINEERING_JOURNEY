# ============================================
# NUMPY PRACTICE - RESHAPE, FLATTEN, RAVEL,
# TRANSPOSE, BROADCASTING, COPY vs VIEW
# Integrated with: OOP, Pandas
# ============================================

import numpy as np
import pandas as pd

# ============================================
# QUESTION 1 - Reshape + Flatten + Ravel basics
# No class needed - pure fundamentals

# You have delay data for 12 train-station readings,
# currently as a flat 1D array:
delays_flat = np.array([10, 0, 25, 40, 5, 60, 15, 0, 30, 45, 20, 50])

# a) Reshape it into a (3, 4) array — 3 trains, 4 stations
# b) Reshape that same (3,4) array into (4, 3) instead
# c) Flatten the (3,4) array back to 1D using .flatten()
# d) Ravel the (3,4) array back to 1D using .ravel()
# e) Modify element [0] of the raveled array to 999,
#    then print the ORIGINAL (3,4) array —
#    did it change? Now do the same with .flatten()'s
#    output — did THAT change the original?
#    Explain in a comment WHY they behave differently.

# YOUR CODE HERE:
reshaped_arr = delays_flat.reshape(3,4)
print("\n THE RESHAPED ARRAY IS : \n" , reshaped_arr)

reshaped2 = reshaped_arr.reshape(4,3)
print("\n THE RESHAPED ARRAY AFTER AGAIN BEEN RESHAPED GIVES THIS ARRAY - \n" , reshaped2)

flat_arr = reshaped_arr.flatten()
print("THE FLATTENED 2D MATRIX IS : " , flat_arr)

ravelled_arr = reshaped_arr.ravel()
print("THE 2D ARRAY AFTER BEEN RAVELLED IS : ",  ravelled_arr)

ravelled_arr[0]=999
print(ravelled_arr)

flat_arr[0]=999
print(flat_arr)
# ============================================
# QUESTION 2 - Transpose + Copy vs View
# A dispatcher has a (4, 3) matrix: 4 trains x 3 metrics
# (columns: delay_minutes, platform, passengers)

matrix = np.array([
    [10, 1, 200],
    [0,  2, 150],
    [45, 1, 300],
    [20, 3, 180]
])

# Build a class MatrixInspector with:
# - Method transpose_matrix() that:
#       returns matrix.T (now 3 trains-worth of metrics
#       become 3 rows, 4 columns)
# - Method is_view_check() that:
#       creates a slice: subset = self.matrix[:2, :]
#       modifies subset[0,0] = -1
#       returns BOTH the subset AND self.matrix

# - Method safe_copy() that:
#       creates a copy: subset_copy = self.matrix[:2, :].copy()
#       modifies subset_copy[0,0] = -999
#       returns BOTH subset_copy AND self.matrix
#       explain in a comment: did modifying subset_copy
#       change the original matrix this time? Why?

# YOUR CODE HERE:
class MatrixInspector:
    def __init__(self , matrix):
        self.matrix= matrix

    def transpose_matrix(self):
        return matrix.T

    def is_view_check(self):
        subset=self.matrix[:2 , :]
        subset[0,0]=-1
        return self.matrix , subset

    def safe_copy(self):
        subset_copy= self.matrix[:2 , :].copy()
        subset_copy[0,0]=999
        return self.matrix ,subset_copy

mi= MatrixInspector(matrix)
print(mi.transpose_matrix())
print(mi.is_view_check())
print(mi.safe_copy())

# ============================================
# QUESTION 3 - Broadcasting Rules
# A pipeline needs to normalize delay data across
# multiple stations, each with a different baseline.

station_delays = np.array([
    [10, 20, 30, 40],   # Train 1's delay at 4 stations
    [15, 25, 35, 45],   # Train 2's delay at 4 stations
    [5,  10, 15, 20]    # Train 3's delay at 4 stations
])

station_baseline = np.array([5, 10, 15, 20])  # per-station baseline, shape (4,)

# Build a class DelayNormalizer with:
# - Method subtract_baseline() that:
#       subtracts station_baseline from EVERY row of
#       station_delays using broadcasting (no loops)
#       explain in a comment WHY shape (3,4) and (4,)
#       are compatible for broadcasting — what's the rule?
# - Method add_train_bonus(self, bonus_per_train) that:
#       bonus_per_train is a 1D array of shape (3,)
#       one value per train — add it so EACH TRAIN'S
#       bonus applies to all 4 of its stations
#       hint: you'll need to reshape bonus_per_train
#       to (3,1) first — explain why in a comment
# - Method scale_all(self, factor) that:
#       multiplies the entire station_delays array
#       by a single scalar (simplest broadcasting case)

# YOUR CODE HERE:
class DelayeNormalizer:
    def __init__(self, station_delays, station_baseline):
        self.station_delays = station_delays
        self.station_baseline = station_baseline

    def subtract_baseline(self):
        return self.station_delays - self.station_baseline

    def add_train_bonus(self, bonus_per_train):
        bonus_per_train = np.array(bonus_per_train).reshape(-1, 1)
        return self.station_delays + bonus_per_train

    def scale_all(self, factor):
        return self.station_delays * factor

dn = DelayeNormalizer(station_delays, station_baseline)
print(dn.subtract_baseline())
print(dn.add_train_bonus(np.array([1, 2, 3])))
print(dn.scale_all(4))
# ============================================
# QUESTION 4 - HARDEST - Full Integration
# Combine reshape/transpose/broadcasting/copy-view
# with Pandas, simulating a real reporting pipeline.

report_data = pd.DataFrame({
    "train_no": ["T1","T2","T3","T4","T5","T6"],
    "monday_delay": [10, 0, 45, 20, 5, 60],
    "tuesday_delay": [15, 5, 30, 25, 0, 55],
    "wednesday_delay": [20, 10, 50, 15, 10, 40]
})

# Build a class WeeklyDelayReport with:
# - Method get_matrix() that:
#       extracts monday/tuesday/wednesday columns as
#       a NumPy array of shape (6, 3) — 6 trains x 3 days
# - Method transpose_to_daywise(self) that:
#       returns the SAME data transposed to shape (3, 6)
#       — now organized as 3 days x 6 trains
#       explain in a comment: is this a copy or a view?
#       (check using .base attribute — if arr.base is
#       not None, it's a view)
# - Method flatten_for_export(self) that:
#       flattens the (6,3) matrix to 1D using .flatten()
#       (deliberately NOT .ravel() — explain in a comment
#       why flatten() is the SAFER choice when the result
#       will be modified independently, e.g. for export)
# - Method apply_day_weights(self, weights) that:
#       weights is shape (3,) — one weight per day
#       (e.g. [1.0, 1.0, 1.5] to weight Wednesday higher)
#       use broadcasting to multiply each day's column
#       by its weight — figure out what reshape is needed
#       and explain why in a comment

# YOUR CODE HERE:

class WeeklyDelayReporter:
    def __init__(self, report_data):
        self.report_data = report_data

    def get_matrix(self):
        return self.report_data[
            ["monday_delay", "tuesday_delay", "wednesday_delay"]
        ].to_numpy()

    def transpose_to_daywise(self):
        return self.get_matrix().T

    def flatten_for_export(self):
        return self.get_matrix().flatten()

    def apply_day_weights(self, weights):
        weights = np.array(weights)
        return self.get_matrix() * weights


wk = WeeklyDelayReporter(report_data=report_data)

print(wk.get_matrix())
print(wk.transpose_to_daywise())
print(wk.flatten_for_export())
print(wk.apply_day_weights(np.array([1.0, 1.0, 1.5])))