import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='hotel',
        user='admin',
        password='admin',
    )


def get_bookings():
    pass


def create_booking(guest_name, arrival_date, departure_date):
    pass


def update_booking(booking_id, guest_name, arrival_date, departure_date):
    pass


def delete_booking(booking_id):
    pass
