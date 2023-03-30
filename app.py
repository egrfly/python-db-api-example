from flask import Flask, request, jsonify, Response
import db

app = Flask(__name__)


@app.get('/bookings')
def view_all_bookings():
    pass


@app.post('/bookings')
def make_booking():
    pass


@app.put('/bookings/<int:booking_id>')
def modify_booking(booking_id):
    pass


@app.delete('/bookings/<int:booking_id>')
def remove_booking(booking_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
