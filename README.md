# RETO-CAPTACION
Reto de captura de datos - Desarrollo de aplicaciones para IoT

## Miembros del equipo

- Asier Sánchez Fernández
- Alaia Yeregui Foncea

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de captura y transmisión de datos en un entorno IoT.
El objetivo es generar datos simulados en un contenedor y enviarlos a otro contenedor encargado de almacenarlos en una base de datos, todo ello gestionado mediante Docker Compose.

## Explicación de los pasos seguidos
Para la elaboración de este proyecto, primero hemos generado los archivos de python, separando la generación de datos, el almacenamiento de los mismos y un archivo con la estructura de la base de datos.

El script de generación simula los datos de un sensor e incueye datos de temperatura, presión, vibración y humedad. Todos los datos se envían en formato JSON.

Por otro lado, se creo un script con una llamada de API usando Flask. Esta API tiene como endpoint "/datos" que recibe las peticiones de POST. Los datos que se reciben se insertan en la base de datos.

Para la base de datos se ha utilizado MySQL, creando un archivo que crea automáticamente la tabla necesaria cuando se arranca el contenedor.

Después, se han creado los archivos Dockerfile para cada parte (generación y almacenamiento), y generó el docker-compose para la comunicación entre esos dos contenedores y el de MySQL.

## Instrucciones de uso
Para poder ejecutarlo, se debe tener instalado wsl, Docker y Docker Compose. 

1. Clonar repositorio de GitHub, ejecutando en la terminal:
git clone https://github.com/Asier888/RETO-CAPTACION.git

2. Entrar en el directorio:
cd RETO-CAPTACION

3. Levantar el sistema:
docker compose up --build

Al ejecutarlo en la consola se verá la API conectándo a MySQL, el generador enviando datos y la respuesta HTTP con 201.

4. Observar los datos almacenados
docker ps
docker ecex -it reto-captacion-db-1 mysql -u user -p datos
(reto-captacion-db-1 corresponde al nombre del contenedor de MySQL)

Pedirá la contraseña, que será: "userpass"

Para poder visualizar los datos se debe realizar una consulta sql:
SELECT * FROM datos;

## Problemas encontrados
La API al conectarse antes de que la base de datos estuviera arrancada. Por eso, en el archivo api.py se añadió un bucle cada 3 segundos hasta conseguir conectar.

## Alternativas posibles
Como alternativas posibles par los mensajes se podría haber uilizado Kafka o RabbitMQ. Además se podrían haber enviado los datos mediante MQTT en lugar de mediante HTTP.

En cuánto a las alternativas para el framework utilziado para la API, se podría haber utilizado FastAPI o Django REST.

Las alternativas barajadas para la base de datos han sido PostgreSQL o MongoDB.