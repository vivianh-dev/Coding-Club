AVAILABLE_SEAT = "A"
OCCUPIED_SEAT = "X"

class SeatSection:
    def __init__(self, min_row, max_row):
        self.min_row = min_row
        self.max_row = max_row
        self.seats = [AVAILABLE_SEAT] * (max_row - min_row + 1)

    def reserve_seat(self, seat_number):
        """
        Reserve a seat within the section.

        Args:
            seat_number (int): The seat number to reserve.

        Returns:
            bool: True if the seat was successfully reserved, False otherwise.
        """
        if seat_number < self.min_row or seat_number > self.max_row:
            print(f"Invalid seat number. Please select a seat between {self.min_row} and {self.max_row}.")
            return False

        if self.seats[seat_number - self.min_row] == OCCUPIED_SEAT:
            print("Seat already occupied. Please select another seat.")
            return False

        self.seats[seat_number - self.min_row] = OCCUPIED_SEAT
        print("Seat reserved successfully.")
        return True

    def is_full(self):
        """
        Check if the section is fully occupied.

        Returns:
            bool: True if all seats are occupied, False otherwise.
        """
        return all(seat == OCCUPIED_SEAT for seat in self.seats)


class Airplane:
    def __init__(self):
        self.first_class = SeatSection(1, 5)
        self.economy = SeatSection(6, 10)

    def menu(self):
        """
        Display the menu and seating chart.

        Returns:
            None
        """
        print("\nMenu:")
        print(f"1. First Class\t\t(Rows: {self.first_class.min_row} to {self.first_class.max_row})"
              f"{'Full' if self.first_class.is_full() else ''}")
        print(f"2. Economy\t\t(Rows: {self.economy.min_row} to {self.economy.max_row})"
              f"{'Full' if self.economy.is_full() else ''}")
        print("3. Exit")
        print()
        print("Seating chart: ", self.get_seating_chart())

    def get_seating_chart(self):
        """
        Get the current seating chart.

        Returns:
            list: A list representing the current seating chart.
        """
        return self.first_class.seats + self.economy.seats

    def reserve_seat(self, section, seat_number):
        """
        Reserve a seat in the specified section.

        Args:
            section (str): The section to reserve the seat in ('1' for First Class, '2' for Economy).
            seat_number (int): The seat number to reserve.

        Returns:
            None
        """
        if section == "1":
            success = self.first_class.reserve_seat(seat_number)
            if not success:
                print("Failed to reserve seat.")
        elif section == "2":
            success = self.economy.reserve_seat(seat_number)
            if not success:
                print("Failed to reserve seat.")
        else:
            print("Invalid section. Please select again.")


def main():
    """
    Main program loop.

    Returns:
        None
    """
    airplane = Airplane()
    while True:
        airplane.menu()
        choice = input("Select an option: ")
        if choice in {"1", "2"}:
            section = "First Class" if choice == "1" else "Economy"
            if getattr(airplane, f"{section.lower().replace(' ', '_')}").is_full():
                print(f"{section} is full.")
                continue
            seat_number = int(input(f"Select a seat in {section}: "))
            airplane.reserve_seat(choice, seat_number)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please select again.")


if __name__ == "__main__":
    main()
