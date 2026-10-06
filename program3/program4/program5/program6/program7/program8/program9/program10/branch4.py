# Job Allocation System using Branch and Bound

n = int(input("Enter number of employees: "))

cost = []

print("Enter the cost matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

best_cost = float('inf')
best_assignment = []


def solve(employee, used, total, assignment):

    global best_cost, best_assignment

    if employee == n:

        if total < best_cost:
            best_cost = total
            best_assignment = assignment.copy()

        return

    # Branch and Bound
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

print("\nOptimal Job Allocation:")

for i in range(n):
    print(
        "Employee", i + 1,
        "-> Task", best_assignment[i] + 1,
        "Cost =", cost[i][best_assignment[i]]
    )

print("Minimum Cost =", best_cost)