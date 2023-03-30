import requests
import json
from datetime import date, timedelta
from pprint import pprint


app_url = 'http://localhost:5000'
json_header = {'Content-Type': 'application/json'}


def test_view_all_bookings():
    response = requests.get(f'{app_url}/bookings')
    pprint(response.json())


def test_make_booking():
    booking_data = {
        'guest_name': 'Sam',
        'arrival_date': date.today().strftime("%Y-%m-%d"),
        'departure_date': (date.today() + timedelta(days=3)).strftime("%Y-%m-%d"),
    }
    response = requests.post(f'{app_url}/bookings',
                             headers=json_header,
                             data=json.dumps(booking_data))
    print(response)


def test_modify_booking():
    id_of_booking_to_modify = 5
    new_booking_data = {
        'guest_name': 'Arthur',
        'arrival_date': date.today().strftime("%Y-%m-%d"),
        'departure_date': (date.today() + timedelta(days=4)).strftime("%Y-%m-%d"),
    }
    response = requests.put(f'{app_url}/bookings/{id_of_booking_to_modify}',
                            headers=json_header,
                            data=json.dumps(new_booking_data))
    print(response)


def test_remove_booking():
    id_of_booking_to_delete = 5
    response = requests.delete(f'{app_url}/bookings/{id_of_booking_to_delete}')
    print(response)


# test_view_all_bookings()
# test_make_booking()
# test_modify_booking()
# test_remove_booking()
