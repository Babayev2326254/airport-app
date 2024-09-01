from config.postgres_connection import connect_database 
from booking.booking_manager import create_booking_details
from booking.booking_operation import save_booking
from flight.flight_manager import create_flight_details
from flight.flight_operation import save_fligthing
from flight.flight_operation import find_all_flights
from booking.booking_operation import find_all_booking
from flight.flight_operation import find_flight_by_id
from booking.booking_operation import find_id_booking
from flight.flight_operation import delete_flight
from booking.booking_operation import delete_booking
from flight.flight_operation import find_flights_by_origin
from flight.flight_operation import uptade_flight
from flight.flight_manager import flight_update_details
from booking.booking_manager import booking_update_details
from booking.booking_operation import update_booking


def console_menu():
    print("-"*30)
    print("Please choose an option:")
    print("1. Create a new flight")
    print("2. Create a new booking")
    print("3. get all flight")
    print("4. Get all bookings")
    print("5. fligt id find")
    print("6. booking id find")
    print("7 Delete flight")
    print("8 Delete booking")
    print("9 find origin flight")
    print("10 update flight")
    print('11 update booking')
    print("12")
    print("13")
    choice = input("Enter your choice: ")
    return choice


def main():
    print("Welcome to the Booking App!")
    choice = console_menu()
    conn=connect_database()
    while True:
        if choice == '1':
           flighting= create_flight_details()
           save_fligthing(flighting,conn)
        elif choice == '2':
            booking=create_booking_details()
            save_booking(booking,conn)
        elif choice == '3':
            find_all_flights(conn)
        elif choice == '4':
            find_all_booking(conn)
        elif choice =='5':
            flight_id = int(input("Enter id: "))
            find_flight_by_id(flight_id,conn)
        elif choice == '6':
            booking_id=int(input(("Enter id: ")))
            find_id_booking(booking_id,conn)
        elif choice == '7':
            flight_id = input("Enter id: ")
            delete_flight(flight_id,conn)
        elif choice == '8':
            booking_id = int(input("Enter id: "))
            delete_booking(booking_id,conn)
        elif choice == '9':
            origin = input("Enter origin city: ")
            find_flights_by_origin(origin, conn)
        elif choice == '10':
            uptade_details = flight_update_details()
            update_for_id = int(input("Enter update ID: "))
            uptade_flight(update_for_id, uptade_details, conn)
        elif choice == '11':
            update_details = booking_update_details()
            update_for_id = int(input("Enter update id: "))
            update_booking(update_for_id, update_details, conn)
        else:
            print("Invalid choice. Please try again.")
        choice = console_menu()
    