CREATE TABLE departamentos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
)

CREATE TABLE empleados(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    salario DECIMAL(10,2) NOT NULL,
    fecha_ingreso DATE NOT NULL, 
    departamento_id INT,
    FOREIGN KEY (departamento_id) REFERENCES departamento(id)
);