# ============================================
# NUMPY PRACTICE - SORT, ARGSORT, UNIQUE,
# CONCATENATE, DOT/MATMUL, VSTACK/HSTACK
# Integrated with: OOP, Pandas
# ============================================

import numpy as np
import pandas as pd

# ============================================
# QUESTION 1 - Full Integration
# Two stations report train delay data separately.
# You need to merge, rank, and score them.

stationA = np.array([
    ["T1", 25],
    ["T2", 0],
    ["T3", 60],
    ["T4", 15]
])

stationB = np.array([
    ["T5", 45],
    ["T6", 10],
    ["T7", 0],
    ["T8", 90]
])

# Also — a second dataset for the scoring part:
# each train's delay across 3 checkpoints (rows = trains,
# cols = checkpoints), and a weight per checkpoint.
checkpoint_delays = np.array([
    [10, 20, 5],
    [0,  15, 10],
    [30, 25, 20],
    [5,  0,  15]
])
checkpoint_weights = np.array([0.5, 0.3, 0.2])  # shape (3,)

# Build a class DelayMerger with:
#
# - Method combine_stations() that:
#       stacks station_A and station_B into ONE array
#       using np.vstack() (both have same columns:
#       train_id, delay) — return the combined array
#
# - Method sort_by_delay(self, combined) that:
#       delay values are currently strings (object dtype
#       from mixing text+numbers) — convert the delay
#       column to int first
#       use np.argsort() on the delay column to get the
#       sort ORDER (indices), then use that to reorder
#       the full combined array (both columns)
#       return the sorted array, ascending by delay
#       explain in a comment: why use argsort() instead
#       of just np.sort() directly on the delay column?
#
# - Method unique_delay_values(self, combined) that:
#       returns the unique delay values present
#       (no duplicates) using np.unique()
#       also return how many unique values there are
#
# - Method weighted_score(self) that:
#       uses checkpoint_delays and checkpoint_weights
#       compute a single weighted delay score per train
#       using np.dot() (matrix-vector multiplication:
#       shape (4,3) dot (3,) -> shape (4,))
#       return the resulting array of 4 scores
#       explain in a comment what real-world quantity
#       this weighted score represents
#
# - Method side_by_side_report(self, combined) that:
#       combined is the (8,2) train_id+delay array
#       create a new column of weighted scores using
#       checkpoint data (just use weighted_score()'s
#       result, even though it's a different train set —
#       for practice purposes, treat it as 4 trains only)
#       use np.hstack() to attach the checkpoint_delays
#       matrix (4,3) next to the weighted score column
#       (4,1) — you'll need to reshape the score first
#       return the final (4,4) combined matrix

# YOUR CODE HERE:

class DelayMerger:
    def __init__(self , stationA , stationB , checkpoint_delays , checkpoint_weights):
        self.stationA = stationA
        self.stationB=stationB 
        self.checkpoint_delays=checkpoint_delays
        self.checkpoint_weights=checkpoint_weights

    def combine_stations(self):
        combined_array =np.vstack((self.stationA,self.stationB))
        return combined_array

    def sort_by_delay(self,combined_array):
        delay = combined_array[:, 1].astype(int)
        sort_order=np.argsort(delay)

        return combined_array[sort_order]

    def unique_delay_values(self):
        value , count = np.unique(checkpoint_delays,return_counts=True)
        return value , count

    def weighted_score(self):
        result=np.dot(self.checkpoint_delays, self.checkpoint_weights)
        return result

    def side_by_side_reports(self):
        scores=self.weighted_score()
        scores=scores.reshape(-1,1)
        return np.hstack((self.checkpoint_delays, scores))


dm=DelayMerger(stationA , stationB , checkpoint_delays , checkpoint_weights)

print(dm.combine_stations())
print(dm.sort_by_delay)
print(dm.unique_delay_values())
print(dm.weighted_score())
print(dm.side_by_side_reports())