# Fractional Knapsack using Greedy

items = [
    (60, 10),
    (100, 20),
    (120, 30)
]

capacity = 50

# Sort by value/weight ratio
items.sort(key=lambda x: x[0] / x[1], reverse=True)

total_value = 0

for value, weight in items:
    if capacity >= weight:
        capacity -= weight
        total_value += value
    else:
        fraction = capacity / weight
        total_value += value * fraction
        break

print("Maximum Value =", total_value)