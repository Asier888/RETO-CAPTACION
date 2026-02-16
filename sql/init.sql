CREATE TABLE IF NOT EXISTS datos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    id_maquina VARCHAR(50),
    temperatura DECIMAL(5,2),
    presion DECIMAL(5,2),
    vibracion DECIMAL(5,2),
    humedad DECIMAL(5,2)
);
