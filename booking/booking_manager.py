

def create_booking_details():
    booking_details = {}
    booking_details['id'] = input("Enter Booking ID: ")
    booking_details['passenger_name'] = input("Enter Passenger Name: ")
    booking_details['flight_id'] = input("Enter Flight ID: ")
    booking_details['seat_count'] = input("Enter Number of Seats: ")

    return booking_details

def booking_update_details():
  booking_update_details = {}
  booking_update_details["id"] = input("Update booking id: ")
  booking_update_details["passenger_name"] = input("Update passenger name: ")
  booking_update_details["flight_id"] = input("Update flight id: ")
  booking_update_details["seat_count"] = input("Update seat count: ")
  return booking_update_details