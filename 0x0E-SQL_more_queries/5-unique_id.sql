-- creates table unique_id
-- id attribute is UNIQUE
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, name VARCHAR(256), UNIQUE(id));