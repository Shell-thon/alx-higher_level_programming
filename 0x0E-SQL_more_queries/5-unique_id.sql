--creates the table unique_id on your MySQL server.
-- creates unique_id table
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
