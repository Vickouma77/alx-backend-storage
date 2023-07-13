-- script that creates a table users
-- has id, email, name and country

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREAMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(255) ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
)
