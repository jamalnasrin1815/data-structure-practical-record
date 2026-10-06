# Job Allocation using Branch and Bound

cost = [
    [10, 2, 8, 7],
    [6, 4, 3, 9],
    [5, 8, 1, 6],
    [7, 6, 9, 4]
]

n = len(cost)

best_cost = float('inf')
best_assignment = []


def solve(employee, used, total, assignment):

    global best_cost, best_assignment

    if employee == n:
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
                employee + 1,
                used,
                total + cost[employee][task],
                assignment
            )

            assignment.pop()
            used.remove(task)


solve(0, set(), 0, [])

print("Optimal Job Allocation:")

for i in range(n):
    print("Employee", i + 1,
          "-> Task", best_assignment[i] + 1,
          "Cost =", cost[i][best_assignment[i]])

print("Minimum Cost =", best_cost)