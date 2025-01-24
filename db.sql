-- Crear la tabla principal para almacenar las encuestas
CREATE TABLE encuestas (
    id SERIAL PRIMARY KEY,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear la tabla para almacenar las preguntas de la encuesta
CREATE TABLE preguntas (
    id SERIAL PRIMARY KEY,
    texto VARCHAR(255) NOT NULL,
    categoria VARCHAR(100) NOT NULL
);

-- Crear la tabla para almacenar las opciones de respuesta de las preguntas de selección
CREATE TABLE opciones (
    id SERIAL PRIMARY KEY,
    id_pregunta INT REFERENCES preguntas(id) ON DELETE CASCADE,
    texto VARCHAR(255) NOT NULL,
    codigo CHAR(1) NOT NULL
);

-- Crear la tabla para almacenar las respuestas de las encuestas
CREATE TABLE respuestas (
    id SERIAL PRIMARY KEY,
    id_encuesta INT REFERENCES encuestas(id) ON DELETE CASCADE,
    id_pregunta INT REFERENCES preguntas(id) ON DELETE CASCADE,
    id_opcion INT REFERENCES opciones(id),
    respuesta_libre VARCHAR(255) -- Para preguntas abiertas o "Otro"
);