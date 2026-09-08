# **Problem: Event Weather Risk Scoring**

# Ten upcoming outdoor events have been pulled from your API, along with 5 days of historical rainfall probability (%) leading up to each event's date, sourced from Open-Meteo.

# ```python
import numpy as np

event_names = np.array([
    "RockFest", "JazzNight", "MarathonRun", "FoodCarnival", "OpenAirCinema",
    "StadiumFinal", "ComedyLive", "BeachParty", "AutoShow", "KiteFestival"
])

# Rows = events, Columns = rainfall probability (%) for 5 days before the event
rainfall_probability = np.array([
    [20, 25, 30, 45, 60],
    [10, 12, 8, 15, 20],
    [70, 65, 80, 75, 90],
    [30, 35, 25, 20, 15],
    [5, 8, 10, 12, 15],
    [40, 45, 50, 60, 55],
    [15, 10, 5, 8, 12],
    [60, 70, 65, 80, 85],
    [25, 20, 30, 28, 22],
    [50, 55, 45, 60, 65]
])

# 1 = venue is outdoor/uncovered, 0 = indoor/covered
venue_is_outdoor = np.array([1, 0, 1, 1, 1, 0, 0, 1, 0, 1])

ticket_prices = np.array([4500, 2000, 1200, 800, 1500, 6000, 2500, 1800, 3000, 900])

# Using this data, answer the following:

# 4. Combine `venue_is_outdoor` into the risk score itself — an event with the exact same rainfall numbers should score meaningfully higher risk if it's outdoor than if it's indoor. Produce one final ranked list, from highest risk to lowest, showing event name, final risk score, and ticket price.
# 5. Sort the final output by risk score, and separately identify which single event has the highest ticket price *among only the top 3 riskiest events* — not the highest price overall.

# **Expected output:** two lists from Q1, a transposed array plus a True/False memory-sharing answer from Q2, a 10-value risk score array from Q3, a ranked table (event, risk score, price) from Q4, and one event name answering Q5.



# 1. Which events have an *average* rainfall probability above 50%, and which are at or below 50%? Produce both lists of event names.
above50= list()
below50 = list()
for i , row in enumerate(rainfall_probability):
    avg_rainfall = np.mean(row)
    if avg_rainfall>50:
        above50.append(event_names[i])
    else : 
        below50.append(event_names[i])
print("EVENTS WITH RAINFALL PROBABILITY ABOVE 50 : " , above50)
print("EVENTS WITH RAINFALL PROBABILITY BELOWE 50 : " , below50)


# 2. Reorganize the rainfall data so each event's 5-day readings appear as a single column instead of a single row (same numbers, transposed structure) — then confirm whether this new arrangement shares memory with the original array or is fully independent.
transposed_mat = rainfall_probability.T
print("THE TRANSPOSED MATRIX IS : \n" ,transposed_mat)
print(" THE SHAPE OF THE GIVEN MATRIX IS : " ,transposed_mat.shape)
print("THE RELATION BETWEEN THE ORIGINAL ARRAY AND THE TRANSPOSED MATRIX IS : " ,np.shares_memory(rainfall_probability , transposed_mat) )


# 3. Compute a single **weather risk score** per event, where the last day's rainfall probability matters more than the first day's (assume the days closer to the event should count more heavily — you decide how to weight them, and justify your choice).
risk_score=list()
for row in rainfall_probability:
    if row[len(row)-1]>0 and row[len(row)-1]<30:
        risk_score.append("LOW")
    elif row[len(row)-1]>=31 and row[len(row)-1]<=50:
        risk_score.append("MID")
    else: 
        risk_score.append("HIGH")



print(risk_score)


    








