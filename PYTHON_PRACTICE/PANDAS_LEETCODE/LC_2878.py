#  LC 2878 GET THE SIZE OF THE DATA FRAME

# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+
# Write a solution to calculate and display the number of rows and columns of players.

# Return the result as an array:

# [number of rows, number of columns]


# APPROACH NUMBER 1 

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    [r,c]=players.shape
    return [r,c]





# APPROACH NUMBER 2 


import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)