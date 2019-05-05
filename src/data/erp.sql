CREATE TABLE passports(
	id INTEGER NOT NULL AUTO_INCREMENT,
	passport_series CHAR(4) NOT NULL,
	passport_number CHAR(6) NOT NULL,
	name VARCHAR(255) NOT NULL,
	surname VARCHAR(255) NOT NULL,
	patronymic VARCHAR(255) NOT NULL,
	date_of_birth DATE NOT NULL,
	place_of_birth VARCHAR(255) NOT NULL,
	sex ENUM ('M', 'F') NOT NULL,
	authority VARCHAR(255) NOT NULL,
	issued_at DATE NOT NULL,
	created_at

	PRIMARY KEY (id),
	UNIQUE passport_number_idx (passport_series, passport_number)
) ENGINE=InnoDB;


CREATE TABLE contractors(
	id INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	surname VARCHAR(255) NOT NULL,
	patronymic VARCHAR(255) NOT NULL,
	rating DECIMAL(5, 2) NOT NULL DEFAULT 0.0,
	passport_id INTEGER NOT NULL,
	email VARCHAR(100) NOT NULL,
	email_confirmed_at DATETIME,
	phone_number VARCHAR(20) NOT NULL,
	phone_number_confirmed_at DATETIME,

	PRIMARY KEY (id),
	FOREIGN KEY passport_id_fk (passport_id) REFERENCES passports(id) ON DELETE CASCADE ON UPDATE RESTRICT,
	UNIQUE (email),
	UNIQUE (phone_number)
) ENGINE=InnoDB;


CREATE TABLE customers(
	id INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,

	PRIMARY KEY (id)
) ENGINE=InnoDB;


CREATE TABLE service_categories(
	id INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	left_node INTEGER,
	right_node INTEGER,
	node_level INTEGER NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY left_node_fk (left_node) REFERENCES service_categories(id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY right_node_fk (right_node) REFERENCES service_categories(id) ON DELETE CASCADE ON UPDATE CASCADE,
	INDEX nested_set_idx (left_node, right_node)
) ENGINE=InnoDB;


CREATE TABLE services(
	id INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
	category_id INTEGER NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY category_id_fk (category_id) REFERENCES service_categories(id) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB;


CREATE TABLE orders(
	id INTEGER NOT NULL AUTO_INCREMENT,
	service_id INTEGER NOT NULL,
	customer_id INTEGER NOT NULL,
	contractor_id INTEGER NOT NULL,
	status ENUM('new', 'pending', 'completed', 'cancelled') NOT NULL DEFAULT 'new',
	license_required BOOLEAN NOT NULL,
	priority INTEGER NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY service_id_fk (service_id) REFERENCES services(id) ON DELETE CASCADE ON UPDATE RESTRICT,
	FOREIGN KEY customer_id_fk (customer_id) REFERENCES customers(id) ON DELETE CASCADE ON UPDATE RESTRICT,
	FOREIGN KEY contractor_id_fk (contractor_id) REFERENCES contractors(id) ON DELETE CASCADE ON UPDATE RESTRICT,
	INDEX (priority),
	INDEX (status)
) ENGINE=InnoDB;


CREATE TABLE reviews(
	id INTEGER NOT NULL AUTO_INCREMENT,
	order_id INTEGER NOT NULL,
	service_category_id INTEGER NOT NULL,
	order_category_id INTEGER NOT NULL,
	review_type ENUM('feedback', 'complaint') NOT NULL DEFAULT 'feedback',
	rating ENUM ('badly', 'unsatisfactorily', 'satisfactorily', 'good', 'excellently') NOT NULL,
	body TINYTEXT NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY order_id_fk (order_id) REFERENCES orders(id) ON DELETE CASCADE ON UPDATE RESTRICT,
	FOREIGN KEY service_category_id_fk (service_category_id) REFERENCES service_categories(id) ON DELETE CASCADE ON UPDATE RESTRICT,
	FOREIGN KEY order_category_id_fk (order_category_id) REFERENCES service_categories(id) ON DELETE CASCADE ON UPDATE RESTRICT,
	INDEX (rating)
) ENGINE=InnoDB;

