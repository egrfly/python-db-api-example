from flask import Flask, request, jsonify, Response
import db

app = Flask(__name__)


@app.get('/bookings')
def view_all_bookings():
    return jsonify(db.get_bookings())


@app.post('/bookings')
def make_booking():
    booking_data = request.get_json()
    db.create_booking(booking_data.get('guest_name'),
                      booking_data.get('arrival_date'),
                      booking_data.get('departure_date'))
    return Response(status=204)


@app.put('/bookings/<int:booking_id>')
def modify_booking(booking_id):
    new_booking_data = request.get_json()
    db.update_booking(booking_id,
                      new_booking_data.get('guest_name'),
                      new_booking_data.get('arrival_date'),
                      new_booking_data.get('departure_date'))
    return Response(status=204)


@app.delete('/bookings/<int:booking_id>')
def remove_booking(booking_id):
    db.delete_booking(booking_id)
    return Response(status=204)


if __name__ == '__main__':
    app.run(debug=True)
