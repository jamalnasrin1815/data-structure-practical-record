# Job Allocation using Branch and Bound

cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

n = len(cost)
best_cost = float('inf')
best_assignment = []


def branch_bound(employee, used, current_cost, assignment):
    global best_cost, best_assignment

    if employee == n:
        if current_cost < best_cost:
            best_cost = current_cost
            best_assignment = assignment.copy()
        return

    # Bound: stop if current cost is already greater
    if current_cost >= best_cost:
        return

    for task in range(n):
        if task not in used:
            assignment.append(task)
            used.add(task)

            branch_bound(
                employee + 1,
                used,
                current_cost + cost[employee][task],
                assignment
            )

            used.remove(task)
            assignment.pop()


branch_bound(0, set(), 0, [])

print("Optimal Assignment:")

for employee in range(n):
    print("Employee", employee + 1,
          "-> Task", best_assignment[employee],
          "Cost =", cost[employee][best_assignment[employee]])

print("Minimum Cost =", best_cost)