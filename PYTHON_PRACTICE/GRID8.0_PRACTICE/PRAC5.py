# ============================================
# PRACTICE — Data Pipeline + Churn Scoring
# Based on Flipkart Grid Style Question
# Date: 20 July 2026
# ============================================

# This is a simplified version of the exact question
# you faced. Build it step by step.

# INPUT DATA
customers = [
    {"customer_id": 1, "customer_name": "Shikhar", "segment": "Premium"},
    {"customer_id": 2, "customer_name": "Rahul", "segment": "Standard"},
    {"customer_id": 3, "customer_name": "Priya", "segment": "Premium"},
    {"customer_id": 4, "customer_name": "Aditya", "segment": "Standard"},
    {"customer_id": 5, "customer_name": "Sneha", "segment": "Budget"},
]

orders = [
    {"order_id": 101, "customer_id": 1, "order_date": "2021-01-15",
     "status": "completed", "amount": 5000},
    {"order_id": 102, "customer_id": 1, "order_date": "2021-03-20",
     "status": "returned", "amount": 2000},
    {"order_id": 103, "customer_id": 2, "order_date": "2021-02-10",
     "status": "completed", "amount": 3000},
    {"order_id": 104, "customer_id": 2, "order_date": "2020-12-01",
     "status": "completed", "amount": 1500},
    {"order_id": 105, "customer_id": 3, "order_date": "2021-04-05",
     "status": "completed", "amount": 8000},
    {"order_id": 106, "customer_id": 99, "order_date": "2021-01-10",
     "status": "completed", "amount": 4000},  # invalid — customer doesn't exist
    {"order_id": 107, "customer_id": 4, "order_date": "2021-01-20",
     "status": "cancelled", "amount": 2500},  # invalid — bad status
    {"order_id": 108, "customer_id": 4, "order_date": "2021-02-15",
     "status": "returned", "amount": -100},   # invalid — negative amount
    {"order_id": 109, "customer_id": 5, "order_date": "2021-01-08",
     "status": "returned", "amount": 1000},
    {"order_id": 110, "customer_id": 5, "order_date": "2021-01-08",
     "status": "returned", "amount": 1000},   # duplicate — count separately
]

tickets = [
    {"ticket_id": 201, "customer_id": 1, "priority": "high"},
    {"ticket_id": 202, "customer_id": 1, "priority": "low"},
    {"ticket_id": 203, "customer_id": 2, "priority": "medium"},
    {"ticket_id": 204, "customer_id": 99, "priority": "high"},  # invalid
    {"ticket_id": 205, "customer_id": 3, "priority": "urgent"}, # invalid
    {"ticket_id": 206, "customer_id": 5, "priority": "low"},
]

REFERENCE_DATE = "2021-04-30"
START_DATE = "2021-01-01"

# ============================================
# YOUR TASK — Build this in stages, in order.
# Do NOT jump to stage 3 before stage 1 is done.
#
# STAGE 1 — Validation
# Write a function validate_orders() that returns
# only valid orders based on these rules:
# - customer_id must exist in customers list
# - status must be "completed" or "returned"
# - order_date must be between START_DATE and
#   REFERENCE_DATE inclusive
# - amount must be greater than 0
# - duplicates are kept — count each separately
#
# Write a function validate_tickets() that returns
# only valid tickets:
# - customer_id must exist in customers list
# - priority must be "low", "medium", or "high"
#
# Print how many valid orders and tickets remain
# after validation.
#
# ============================================
# STAGE 2 — Per Customer Metrics
# Write a function calculate_customer_metrics()
# that takes valid_orders and valid_tickets and
# returns a dict for each customer containing:
# - completed_order_count
# - returned_order_count
# - valid_order_count
# - completed_spend
# - latest_completed_order_date (None if no completed orders)
# - inactive_days (reference_date - latest_completed_order_date)
#   if no completed orders: inactive_days = reference_date_days + 1
#   hint: use datetime to subtract dates
# - return_percentage (returned / valid * 100), 0 if no valid orders
# - support_ticket_count
# - support_ticket_weight (low=1, medium=2, high=3)
#
# ============================================
# STAGE 3 — Segment Metrics
# Write a function calculate_segment_metrics()
# that takes customer_metrics and returns
# segment_average_spend for each segment.
# Include ALL customers in segment even those
# with zero completed_spend.
#
# Then add to each customer:
# - segment_average_spend
# - is_low_spend (True if completed_spend 
#   segment_average_spend, False if equal or greater)
#
# ============================================
# STAGE 4 — Churn Score
# Write a function calculate_churn_score()
# that adds to each customer:
# - inactive_score: 5 if inactive_days >= 90 else 0
# - no_order_score: 3 if completed_order_count == 0
# - return_score: 4 if return_percentage >= 40
# - low_spend_score: 3 if is_low_spend
# - ticket_score: inactive_days if inactive_days >= 90 else 0
# - total_risk_score: sum of all above
# - risk_level: "High" if >= 8, "Medium" if 5-7, "Low" if < 5
#
# ============================================
# STAGE 5 — Final Report
# Print a clean report for each customer showing:
# customer_name | segment | completed_spend |
# inactive_days | risk_score | risk_level
#
# YOUR CODE HERE — build stage by stage: