-- Crear una bd
CREATE DATABASE rhr_cursos;

-- Usar bd
USE rhr_cursos;

-- Creamos las tablas
CREATE TABLE cursos (
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
duracion INT, -- horas
precio DECIMAL(10,2)
);

CREATE TABLE alumnos(
id INT PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(100),
email VARCHAR(100)
);

CREATE TABLE inscripciones(
id INT PRIMARY KEY AUTO_INCREMENT,
alumno_id INT,
curso_id INT,
fecha_inscripcion DATE,
FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

-- Insertartamos datos
INSERT INTO cursos (nombre, duracion, precio) VALUES
('SQL Básico', 20 , 500),
('SQL Avanzado', 30, 1000),
('Power BI',25,800),
('Python para datos', 35, 1500);

INSERT INTO alumnos (nombre, email) VALUES
('Ana Lopez', 'ana@email.com'),
('Bruno Diaz','asd@ads.com'),
('Carla Gomez','carla@gmail.com');

INSERT INTO inscripciones (alumno_id, curso_id, fecha_inscripcion) VALUES
(1,1, '2025-06-01'),
(1,3, '2025-06-01'),
(2,2, '2025-06-01'),
(3,1, '2025-06-01'),
(3,4, '2025-06-01');

-- INNER JOIN ejemplo
-- Solo los alumnos que están inscriptos en algún curso
SELECT a.nombre AS Alumno, c.nombre AS Curso
FROM inscripciones i 
INNER JOIN alumnos a ON i.alumno_id = a.id 
INNER JOIN cursos c ON i.curso_id = c.id;

-- LEFT JOIN
-- Todos los alumnos. Si alguno no esta inscripto, el campo curso aparecerá NULL
SELECT a.nombre AS Alumno, c.nombre AS Curso
FROM alumnos a
LEFT JOIN inscripciones i ON a.id = i.alumno_id
LEFT JOIN cursos c ON i.curso_id = c.id;

-- RIGHT JOIN
-- Mostramos todos los cursos, aunque no tengan alumnos inscriptos
SELECT a.nombre as Alumno, c.nombre AS Curso
FROM alumnos a
RIGHT JOIN inscripciones i ON a.id = i.alumno_id
RIGHT JOIN cursos c ON i.curso_id = c.id;

-- Subconsultas
-- Alumnos que se inscribieron en mas de un curso
SELECT nombre
FROM alumnos
WHERE id IN (
	SELECT alumno_id 
    FROM inscripciones
    GROUP BY alumno_id
    HAVING Count(*) > 1
);

-- Subconsulta con funcion de agregacion
-- Cursos mas caros que el promedio
SELECT nombre, precio
FROM cursos
WHERE precio > (
	SELECT AVG(precio) FROM cursos
);
SELECT AVG(precio) FROM cursos; -- ver el promedio

-- Alteramos la tabla cursos para agregar la columna vacantes disponibles
ALTER TABLE cursos ADD COLUMN vacantes_disponibles INT DEFAULT 10;

-- Creamos una transaccion para agregar un alumno a un curso, descontando un lugar vacante
START TRANSACTION ;

INSERT INTO inscripciones (alumno_id, curso_id, fecha_inscripcion) 
VALUES (2,1, CURDATE());

UPDATE cursos
SET vacantes_disponibles = vacantes_disponibles - 1
WHERE id = 1;

SELECT * FROM cursos;

COMMIT;

-- Control de concurrencia
UPDATE cursos SET vacantes_disponibles = 1 WHERE id = 1;

START TRANSACTION ;

SELECT vacantes_disponibles 
FROM cursos
WHERE id = 1;

UPDATE cursos SET vacantes_disponibles = vacantes_disponibles -1 WHERE id = 1;

INSERT INTO inscripciones (alumno_id, curso_id , fecha_inscripcion)
VALUES (1,1, CURDATE());

COMMIT;