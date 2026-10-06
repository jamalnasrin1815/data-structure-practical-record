# Fractional Knapsack

items = [
    (40, 5),
    (100, 10),
    (90, 20),
    (150, 30)
]

capacity = 35

items.sort(key=lambda x: x[0] / x[1], reverse=True)

total_value = 0

for value, weight in items:
    if weight <= capacity:
        capacity -= weight
        total_value += value
    else:
        total_value += value * (capacity / weight)
        break

print("Maximum Value =", total_value)