class Star_Cinema:
    _hall_list = []

    def entry_hall(self, hall):
        self._hall_list.append(hall)


class Hall(Star_Cinema):

    def __init__(self, hall_no, rows, cols):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[show_id] = [
            [0 for _ in range(self._cols)] for _ in range(self._rows)
        ]

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            raise ValueError("Invalid show id")

        for seat in seat_list:
            row, col = seat
            if not (0 <= row < self._rows and 0 <= col < self._cols):
                print(f"Invalid seat: Row {row}, Col {col} is already booked.")
                continue

            if self._seats[show_id][row][col] == 1:
                print(f"Seat is already booked")
            else:
                self._seats[show_id][row][col] = 1
                print(f"Seat booked : Row {row}, Col {col}")
            print("\n")

    def view_show_list(self):
        print("Show List\n")

        for show_id, movie_name, time in self._show_list:
            print(f"Show ID : {show_id}, Movie = {movie_name}, Time = {time}")
        print("\n")

    def view_available_seats(self, show_id):
        print("\n")

        if show_id not in self._seats:
            raise ValueError("Invalid show_id\n")

        for _ in self._seats[show_id]:
            print(list(_))
        print("\n")


def void():
    hall1 = Hall(hall_no=1, rows=7, cols=7)
    hall1.entry_show(show_id=1, movie_name="Death Note", time=" 9.00AM")
    hall1.entry_show(show_id=2, movie_name="Extraction", time=" 11.30AM")
    hall1.entry_show(show_id=3, movie_name="IP Man", time=" 3.00PM")
    hall1.entry_show(show_id=4, movie_name="RRR", time=" 6.00PM")
    hall1.entry_show(show_id=5, movie_name="Tufan", time=" 9.00PM")

    while True:
        print("1. View all shows")
        print("2. View available seats")
        print("3. Book tickets")
        print("4. Exit")

        try:
            option = int(input("Enter Option: "))
            if option == 4:
                break

            elif option == 1:
                hall1.view_show_list()

            elif option == 2:
                show_id = int(input("Enter Show ID: "))
                hall1.view_available_seats(show_id)

            elif option == 3:
                show_id = int(input("Enter Show ID: "))
                num_tickets = int(input("Enter Number of Tickets: "))
                seat_list = []
                i = 1

                for _ in range(num_tickets):
                    row, col = map(int, input(f"{i}. Enter Row and Column: ").split())
                    seat_list.append((row, col))
                    i = i + 1

                hall1.book_seats(show_id, seat_list)

            else:
                print("Invalid Option")

        except ValueError:
            print("Invalid input! Please enter a number.")


void()
