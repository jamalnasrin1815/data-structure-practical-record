# Quick Sort by Customer Name

bookings = [
    [101, "Nasrin", "Avengers", 2],
    [102, "Jamal", "Avatar", 3],
    [103, "Afrin", "Batman", 1],
    [104, "Liya", "Avengers", 4]
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x[1] <= pivot[1]]
    right = [x for x in arr[1:] if x[1] > pivot[1]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = quick_sort(bookings)

print("Bookings sorted by Customer Name:")

for booking in bookings:
    print(booking)