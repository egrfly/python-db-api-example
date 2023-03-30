CREATE DATABASE IF NOT EXISTS hotel;
USE hotel;

CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    guest_name VARCHAR(255) NOT NULL,
    arrival_date DATE NOT NULL,
    departure_date DATE NOT NULL
);

INSERT INTO bookings (guest_name, arrival_date, departure_date) VALUES
('Kim', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 2 DAY)),
('Emily', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 4 DAY)),
('Helen', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 5 DAY)),
('Shepstone', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY));
