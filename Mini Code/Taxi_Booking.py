def show_available_taxis(taxis):
    print("------------------------")
    print("Available Taxis:")
    for taxi in taxis:
        print(f"Taxi ID: {taxi['id']}, Driver: {taxi['driver']}, Status: {taxi['status']}")

def book_taxi(taxis, pickup_points):
    taxi_id = input("Enter the Taxi ID you want to book: ")
    for taxi in taxis:
        if taxi['id'] == taxi_id and taxi['status'] == 'available':
            print("Pickup Points: ", ", ".join(pickup_points))
            pickup = input("Enter the pickup point: ")
            drop = input("Enter the drop point: ")
            if pickup in pickup_points and drop in pickup_points:
                distance = abs(pickup_points.index(pickup) - pickup_points.index(drop))
                fare = distance * 10  # Assuming fare is 10 units per distance
                taxi['status'] = 'booked'
                print(f"Taxi {taxi_id} has been booked successfully!")
                print(f"Pickup: {pickup}, Drop: {drop}, Distance: {distance}, Fare: {fare}")
                return
            else:
                print("Invalid pickup or drop point.")
                return
    print("Taxi not available or invalid Taxi ID.")

def main():
    taxis = [
        {'id': 'TX001', 'driver': 'John', 'status': 'available'},
        {'id': 'TX002', 'driver': 'Alice', 'status': 'available'},
        {'id': 'TX003', 'driver': 'Bob', 'status': 'booked'},
    ]
    pickup_points = ['A', 'B', 'C', 'D']
    is_running = True
    while is_running:
        print("------------------------")
        print("1. Check Available Taxis")
        print("2. Book a Taxi")
        print("3. Exit")
        print("------------------------")
        choice = input("Enter the number between (1 to 3): ")
        
        if choice == "1":
            show_available_taxis(taxis)
        elif choice == "2":
            book_taxi(taxis, pickup_points)
        elif choice == "3":
            is_running = False
            print("Thank you. Have a great day!")
        else:
            print("Invalid number")

if __name__ == "__main__":
    main()
