from flight import flight_manager
from config import postgres_connection
from config.postgres_connection import sql 
import sqlite3


def save_fligthing(flight_details,conn):
    insert_query = """
    INSERT INTO public.flights(id,flight_number, date, time,origin,destination,seats)
    VALUES (%s, %s, %s, %s,%s,%s,%s)
    """
    try:
        curr=conn.cursor()
        curr.execute(insert_query, (
            flight_details['id'],
            flight_details['flight_number'],
            flight_details['date'],
            flight_details['time'],
            flight_details['origin'],
            flight_details['destination'],
            flight_details['seats']
        ))
        conn.commit()
        print("Succesfull flight")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()


    
        
def find_all_flights(conn):
    insert_query = """
    SELECT * FROM flights;
    """
    try:
        curr=conn.cursor()
        curr.execute(insert_query)
        results = curr.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print(f"Error: {e}")

def find_flight_by_id(flight_id, conn):
    insert_query = '''
    SELECT * FROM flights
    WHERE id = %s
    '''
    try:
        with conn.cursor() as curr:
            curr.execute(insert_query, (flight_id,))
            result = curr.fetchone()  
            print(result)
    except Exception as e:
        print(f"Error: {e}")
    


def delete_flight(flight_id, conn):
 delete_query = """
 DELETE FROM flights
 WHERE id = %s;
 """
 select_query = """
 SELECT COUNT(*) FROM flights
 WHERE id = %s;
 """
 cursorr = conn.cursor()
 try:     
  cursorr.execute(select_query, (flight_id,))
  result = cursorr.fetchone()
  
  if result:
      count = int(result[0])  
  else:
      count = 0
  if count >0:
      cursorr.execute(delete_query, (flight_id,))
      conn.commit()
      print(f"FLİGHT ID {flight_id} SUCCESSFULLY DELETE!")
  else:
      conn.close()
      print("wrong id again")    
 except Exception as e:
  conn.rollback()
  print(f"Error detected: {e}")
  
  
  
def find_flights_by_origin(origin, conn):
    insert_query = '''
    SELECT * FROM flights
    WHERE origin = %s
    '''
    try:
        with conn.cursor() as curr:
         curr.execute(insert_query, (origin,))
         result = curr.fetchall() 
         for row in result:
             print(row)
    except Exception as e:
        print(f"Error: {e}")


     
def uptade_flight(id, flight_update_details, conn):
  uptade_query = """Update flights 
  SET 
  flight_number = %s,
  date = %s,
  time = %s,
  origin = %s, 
  destination = %s,
  seats = %s
  WHERE id = %s"""
  cursor = conn.cursor()

  try:
    cursor.execute(uptade_query, (
      flight_update_details["flight_number"],
      flight_update_details["date"],
      flight_update_details["time"],
      flight_update_details["origin"],
      flight_update_details["destination"],
      flight_update_details["seats"],
      id
      ))
    conn.commit()
    print("Uptaded successfully!")
  except Exception as e:
    conn.rollback()
    print(f"error detected {e}")