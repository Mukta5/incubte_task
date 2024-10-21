CREATE TABLE IF NOT EXISTS staging_customers (
    customer_name VARCHAR(255) NOT NULL,
    customer_id VARCHAR(18) NOT NULL PRIMARY KEY,
    open_date DATE NOT NULL,
    last_consulted_date DATE,
    vaccination_type CHAR(5),
    doctor_consulted VARCHAR(255),
    state CHAR(5),
    country CHAR(5) NOT NULL,
    post_code INT,
    date_of_birth DATE NOT NULL,
    active_customer CHAR(1) CHECK (active_customer IN ('A', 'I'))
);
