from booking import booking_manager
from config import postgres_connection
from config.postgres_connection import sql 
import sqlite3


def save_booking(booking_details,conn):
    insert_query = """
    INSERT INTO public.bookings(id, passenger_name, flight_id, seat_count)
    VALUES (%s, %s, %s, %s)
    """
    with conn.cursor() as curr:
        try:
            curr.execute(insert_query, (
                booking_details['id'],
                booking_details['passenger_name'],
                booking_details['flight_id'],
                booking_details['seat_count']
            ))
            conn.commit()
            print("Succesful booking")
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()

def find_all_booking(conn):
    insert_query = """
    SELECT * FROM bookings;
    """
    try:
        curr=conn.cursor()
        curr.execute(insert_query)
        results = curr.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print(f"Error: {e}")
    

def find_id_booking(booking_id,conn):
    insert_query = '''
    SELECT * FROM bookings
    WHERE id = %s
    '''
    try:
        with conn.cursor() as curr:
            curr.execute(insert_query,(booking_id,))
            result = curr.fetchone()  
            print(result)
    except Exception as e:
        print(f"Error: {e}")

def delete_booking(booking_id, conn):
 delete_query = """
 DELETE FROM bookings
 WHERE id = %s;
 """
 select_query = """
 SELECT COUNT(*) FROM bookings
 WHERE id = %s;
 """
 cursorr = conn.cursor()
 try:     
  cursorr.execute(select_query, (booking_id,))
  result = cursorr.fetchone()
  
  if result:
      count = int(result[0])  
  else:
      count = 0
  if count >0:
      cursorr.execute(delete_query, (booking_id,))
      conn.commit()
      print(f"FLİGHT ID {booking_id} SUCCESSFULLY DELETE!")
  else:
      conn.close()
      print("wrong id again")    
 except Exception as e:
     conn.rollback()
     print(f"Error detected: {e}")
    

def update_booking(id,booking_update_details, conn):
  update_query = """UPDATE bookings
  SET
  passenger_name = %s,
  flight_id = %s,
  seat_count = %s
  WHERE id = %s"""
  cursor = conn.cursor()
  try:
    cursor.execute(update_query, (
      booking_update_details["passenger_name"],
      booking_update_details["flight_id"],
      booking_update_details["seat_count"],
      booking_update_details["id"]
      ))
    conn.commit()
    print("Updated successfully")
  except Exception as e:
    conn.rollback()
    print(f"Error: {e}")
