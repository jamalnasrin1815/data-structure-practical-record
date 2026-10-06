# Quick Sort by Number of Tickets

bookings = [
    [101, "Nasrin", "Avengers", 5],
    [102, "Jamal", "Avatar", 2],
    [103, "Afrin", "Batman", 4],
    [104, "Liya", "Avengers", 1]
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x[3] <= pivot[3]]
    right = [x for x in arr[1:] if x[3] > pivot[3]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = quick_sort(bookings)

print("Bookings sorted by Number of Tickets:")

for booking in bookings:
    print(booking)