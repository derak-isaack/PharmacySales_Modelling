CREATE TABLE IF NOT EXISTS Employees
(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  salary INT NOT NULL,
  phone_number INT(50) NOT NULL,
  email VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Drugs_items
(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  price INT NOT NULL,
  quantity_supplied INT NOT NULL,
  stock_remaining INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Doctors_table
(
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  phone_number INT(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  specialization TEXT(50) NOT NULL,
  region TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Sales  
(
  emp_id INT NOT NULL,
  drug_id INT NOT NULL,
  doc_id INT NOT NULL,
  pharmacy_name VARCHAR(50), 
  pharmacy_region TEXT,        
  quantity_sold INT NOT NULL,
  date_sold DATE NOT NULL,
  PRIMARY KEY (emp_id, drug_id, doc_id),
  FOREIGN KEY (emp_id) REFERENCES Employees(id),
  FOREIGN KEY (drug_id) REFERENCES Drugs_items(id),
  FOREIGN KEY (doc_id) REFERENCES Doctors_table(id)
);
