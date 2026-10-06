# Job Allocation using Branch and Bound

employees = ["Arun", "Priya", "Rahul", "Meena"]

cost = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

n = len(employees)

best_cost = float('inf')
best_assignment = []


def solve(i, used, total, assignment):

    global best_cost, best_assignment

    if i == n:
        if total < best_cost:
            best_cost = total
            best_assignment = assignment.copy()
        return

    if total >= best_cost:
        return

    for task in range(n):

        if task not in used:

            used.add(task)
            assignment.append(task)

            solve(
                i + 1,
                used,
                total + cost[i][task],
                assignment
            )

            assignment.pop()
            used.remove(task)


solve(0, set(), 0, [])

print("Minimum Cost Job Allocation:\n")

for i in range(n):
    print(
        employees[i],
        "-> Task", best_assignment[i] + 1,
        "Cost =", cost[i][best_assignment[i]]
    )

print("\nMinimum Total Cost =", best_cost)