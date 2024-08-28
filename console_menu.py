from config.postgres_connection import connect
from booking.booking_manager import create_booking_details
from booking.booking_operation import save_booking
from flight.flight_operation import find_all_flight
from flight.flight_manager import update_flight_details


def console_menu():
    print("-"*30)
    print("Please choose an option:")
    print("1. Create a new flight")
    print("2. Create a new booking")
    print("3. Get all bookings")
    print("4. get all flight")
    print("5. update fligt")
    choice = input("Enter your choice: ")
    return choice


def main():
    print("Welcome to the Booking App!")
    choice = console_menu()
    conn=connect()
    while choice != '4':
        if choice == '1':
            pass
        elif choice == '2':
            booking=create_booking_details()
            save_booking(booking,conn)
        elif choice == '3':
            pass
        elif choice == '4':
            flight=find_all_flight(conn)
            print(flight)
        elif choice =='5':
            update_flight_details(conn)
        else:
            print("Invalid choice. Please try again.")
        choice = console_menu()
    print("Exiting the Booking App. Goodbye!")