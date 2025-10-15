class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name: str):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
peeps = ["Harry", "Eddy", "john", "another"]
for person in peeps:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to the flight")
    else:
        print("Passenger limit reached.")
