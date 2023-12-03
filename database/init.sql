CREATE TABLE currency(
  id SERIAL PRIMARY KEY,
  name VARCHAR(3),
  long_name VARCHAR(100)
);

CREATE TABLE price_data (
  time TIMESTAMPTZ NOT NULL,
  currency_id INTEGER,
  price DOUBLE PRECISION,
  FOREIGN KEY (currency_id) REFERENCES currency (id)
);
