import os
import csv
filepath = os.path.join('budget_data.csv')
budget_data = []
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
for row in reader:
    budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})
total_months = len(budget_data)