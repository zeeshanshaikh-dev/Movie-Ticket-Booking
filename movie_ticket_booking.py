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

            print("Your tickets have been booked successfully!")
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

# Book tickets.
movie.book_tickets(6)

# Display the current booking status.
movie.show_status()