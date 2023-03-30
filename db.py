import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='hotel',
        user='admin',
        password='admin',
    )


def get_bookings():
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT * FROM bookings""")
            return cursor.fetchall()


def create_booking(guest_name, arrival_date, departure_date):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO bookings (guest_name, arrival_date, departure_date)
                              VALUES (%s, %s, %s)""", [guest_name, arrival_date, departure_date])
        connection.commit()


def update_booking(booking_id, guest_name, arrival_date, departure_date):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE bookings
                              SET guest_name = %s, arrival_date = %s, departure_date = %s
                              WHERE id = %s""", [guest_name, arrival_date, departure_date, booking_id])
        connection.commit()


def delete_booking(booking_id):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE FROM bookings
                              WHERE id = %s""", [booking_id])
        connection.commit()
