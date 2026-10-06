# Movie Ticket Booking System using Quick Sort

bookings = []

n = int(input("Enter number of bookings: "))

for i in range(n):
    print("\nBooking", i + 1)

    ticket_id = int(input("Enter Ticket ID: "))
    name = input("Enter Customer Name: ")
    movie = input("Enter Movie Name: ")
    tickets = int(input("Enter Number of Tickets: "))

    bookings.append([ticket_id, name, movie, tickets])


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x[0] <= pivot[0]]
    right = [x for x in arr[1:] if x[0] > pivot[0]]

    return quick_sort(left) + [pivot] + quick_sort(right)


bookings = quick_sort(bookings)

print("\nBookings Sorted by Ticket ID:")

for booking in bookings:
    print(
        "Ticket ID:", booking[0],
        "Name:", booking[1],
        "Movie:", booking[2],
        "Tickets:", booking[3]
    )