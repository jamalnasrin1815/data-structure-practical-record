# Movie Ticket Booking System
# Quick Sort by Ticket ID

bookings = [
    [105, "Nasrin", "Avengers", 2],
    [102, "liya", "Avatar", 3],
    [104, "afrin", "Batman", 1],
    [101, "jamal", "Avengers", 4]
]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x[0] <= pivot[0]]
    right = [x for x in arr[1:] if x[0] > pivot[0]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = quick_sort(bookings)

print("Bookings sorted by Ticket ID:")

for booking in bookings:
    print(booking)