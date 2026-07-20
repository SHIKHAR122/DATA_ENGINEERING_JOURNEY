"""
==================================================================
PROBLEM: Delivery Rating Summary
CATEGORY: Multi-table dict-join + validation + aggregation
DIFFICULTY: Medium (GRiD Round 2 style - "Data Frame Coding" pattern)
==================================================================

DATA STRUCTURES:

drivers = [
    {"driverId": str, "driverName": str},
    ...
]

trips = [
    {
        "tripId": str,
        "driverId": str,
        "rating": int,      # intended range 1-5
        "status": str        # "COMPLETED" or "CANCELLED"
    },
    ...
]

------------------------------------------------------------------
VALID RECORD RULES (a trip counts ONLY if ALL hold):
------------------------------------------------------------------
1. driverId exists in the drivers table
2. status == "COMPLETED"
3. 1 <= rating <= 5

------------------------------------------------------------------
TASK:
------------------------------------------------------------------
For every driver with AT LEAST ONE valid trip, compute:

    avgRating = ( sum of rating across that driver's valid trips )
                / ( count of that driver's valid trips )
                rounded to 1 DECIMAL PLACE   <-- not whole number, watch this

Drivers with avgRating >= 4.5 qualify.

------------------------------------------------------------------
OUTPUT FORMAT:
------------------------------------------------------------------
Print each qualifying driver as:
    driverId-driverName-avgRating

Join multiple entries with '#'.

Sort order:
    1. avgRating descending
    2. if tied, driverId ascending

Print 'NA' if no driver qualifies.

NOTE ON FORMATTING: avgRating must show 1 decimal place even if it's
a whole number — e.g. 4.5 should print as "4.5", not "4" or "4.50".
Watch how round(x, 1) behaves and how you convert it to string
(e.g. round(4.0, 1) -> 4.0, but str(4.0) -> "4.0", not "4").

------------------------------------------------------------------
CONSTRAINTS:
------------------------------------------------------------------
i.   1 <= number of drivers <= 100000
ii.  0 <= number of trips <= 200000
iii. 1 <= rating <= 5 (for it to be valid)

------------------------------------------------------------------
SAMPLE INPUT:
------------------------------------------------------------------
drivers = [
    {"driverId": "D1", "driverName": "Farhan"},
    {"driverId": "D2", "driverName": "Priya"},
    {"driverId": "D3", "driverName": "Rehan"}
]

trips = [
    {"tripId": "T1", "driverId": "D1", "rating": 5, "status": "COMPLETED"},
    {"tripId": "T2", "driverId": "D1", "rating": 4, "status": "COMPLETED"},
    {"tripId": "T3", "driverId": "D2", "rating": 5, "status": "COMPLETED"},
    {"tripId": "T4", "driverId": "D2", "rating": 3, "status": "CANCELLED"},   # excluded: not COMPLETED
    {"tripId": "T5", "driverId": "D3", "rating": 2, "status": "COMPLETED"},
    {"tripId": "T6", "driverId": "D9", "rating": 5, "status": "COMPLETED"}    # excluded: D9 doesn't exist
]

------------------------------------------------------------------
EXPECTED OUTPUT WALKTHROUGH:
------------------------------------------------------------------
D1: (5 + 4) / 2 = 4.5 -> qualifies
D2: only T3 valid (T4 is CANCELLED) -> 5 / 1 = 5.0 -> qualifies
D3: 2 / 1 = 2.0 -> does not qualify
T6 ignored entirely -> D9 isn't a real driver

Qualifying drivers sorted by avgRating descending:
D2 (5.0) before D1 (4.5)

Correct output: "D2-Priya-5.0#D1-Farhan-4.5"

==================================================================
YOUR TASK: Write solve(drivers, trips) that returns the final
formatted string (or 'NA').
==================================================================
"""

def solve(drivers, trips):

    driver = {}

    for d in drivers:
        driver[d["driverId"]] = d

    total_rating = {}
    trip_count = {}

    for t in trips:

        driver_id = t["driverId"]

        if driver_id not in driver:
            continue

        if t["status"] != "COMPLETED":
            continue

        if t["rating"] < 1 or t["rating"] > 5:
            continue

        if driver_id not in total_rating:
            total_rating[driver_id] = 0
            trip_count[driver_id] = 0
        total_rating[driver_id] += t["rating"]
        trip_count[driver_id] += 1

    result = []

    for driver_id in total_rating:

        avg = round(total_rating[driver_id] / trip_count[driver_id],1)

        if avg >= 4.5:
            result.append((avg, driver_id,driver[driver_id]["driverName"]))
    if len(result) == 0:
        return "NA"


    result.sort(key=lambda x: (-x[0], x[1]))

    output = []

    for avg, driver_id, driver_name in result:
        output.append(
            f"{driver_id}-{driver_name}-{avg}"
        )

    return "#".join(output)