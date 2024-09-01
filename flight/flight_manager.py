
def create_flight_details():
    flight_details={}
    flight_details["id"] = input("Enter flight ID: ")
    flight_details["flight_number"] = input("Enter flight number : ")
    flight_details["date"] = input("Enter a date: ")
    flight_details["time"] = input("Enter a time: ")
    flight_details["origin"] = input("Enter origin: ")
    flight_details["destination"] = input("Enter a destination: ")
    flight_details["seats"] = input("Enter seats: ")
    return flight_details

def flight_update_details():
     flight_update_details = {}
     flight_update_details["flight_number"] = input("Update flight number: ")
     flight_update_details["date"] = input("Update a date: ")
     flight_update_details["time"] = input("Update time: ")
     flight_update_details["origin"] = input("Update origin: ")
     flight_update_details["destination"] = input("Update destination: ")
     flight_update_details["seats"] = input("Update seats: ")
     return flight_update_details
