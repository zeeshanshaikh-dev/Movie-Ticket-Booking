class Movie:
    def __init__(self, movie_name: str, total_seats: int, ticket_price: int):
        # Store the movie name.
        self.movie_name = movie_name

        # Validate the total number of seats.
        if total_seats <= 0:
            raise ValueError("Total seats must be greater than 0")

        # Validate the ticket price.
        if ticket_price <= 0:
            raise ValueError("Ticket price must be greater than 0")

        # Store the total number of seats.
        self.total_seats = total_seats

        # Store the price of one ticket.
        self.ticket_price = ticket_price

        # Initially, no tickets have been booked.
        self.booked_tickets = 0

    def book_tickets(self, num_of_tickets: int):
        # Make sure the number of tickets is positive.
        if num_of_tickets <= 0:
            print("Invalid number of tickets")

        # Check whether enough seats are available.
        elif num_of_tickets > self.available_seats():
            print("Sorry, not enough seats available")

        # Book the requested number of tickets.
        else:
            self.booked_tickets += num_of_tickets

            # Calculate the total cost.
            total_price = self.ticket_price * num_of_tickets

            print("\nYour tickets have been booked successfully!")
            print(f"Number of Tickets = {num_of_tickets}")
            print(f"Total Price = ₹{total_price}")

    def available_seats(self):
        # Calculate and return the number of remaining seats.
        return self.total_seats - self.booked_tickets

    def show_status(self):
        # Display the current movie booking status.
        print("\n========== MOVIE STATUS ==========")
        print(f"Movie Name = {self.movie_name}")
        print(f"Ticket Price = ₹{self.ticket_price}")
        print(f"Total Seats = {self.total_seats}")
        print(f"Seats Available = {self.available_seats()}")
        print(f"Seats Booked = {self.booked_tickets}")


# Create a movie object.
movie = Movie("Spiderman: Brand New Day", 100, 499)


# Main menu.
while True:
    print("\n========== MOVIE TICKET BOOKING SYSTEM ==========")
    print("1. Book Tickets")
    print("2. Show Movie Status")
    print("3. Exit")

    # Ask the user to select an option.
    choice = input("Enter your choice: ")

    # Book tickets.
    if choice == "1":
        num_of_tickets = int(input("Enter number of tickets: "))
        movie.book_tickets(num_of_tickets)

    # Display movie status.
    elif choice == "2":
        movie.show_status()

    # Exit the program.
    elif choice == "3":
        print("\nThank you for using the Movie Ticket Booking System!")
        break

    # Handle invalid menu choices.
    else:
        print("Invalid choice. Please select 1, 2, or 3.")