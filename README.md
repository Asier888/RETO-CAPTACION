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

## Vías de mejoras
Durante el diseño del proyecto se han considerado diversas alternativas tecnológicas que podrían haber sido utilizadas dependiendo de los requisitos del sistema.

Para las peticiones POST se podrían haber empleado otros protocolos diferentes en lugar de HTTP: como MQTT, el cual es más ligero e ideal en dispositivos con bajos 

## Alternativas posibles
En lugar de utilizar HTTP con peticiones POST, se podrían haber empleado otros mecanismos de comunicación más habituales en IoT; o RabbitMQ, permitiendo una comunicación asíncrona para individualizar los diferentes generadores. Y Apache Kafka, que está más orientado a sistemas que tienen un gran volumen de datos.

En cuanto al framework utilizado para la generación de la API, podría haberse utilizado FastAPI, que tiene un mejor rendimiento y  tiene validación automática de datos; o Django REST Framework, que incluye autenticación y administración integrada en el mismo. Sin embargo Flask debido a su simplicidad y fácil integración con Docker.

En vez de MySQL, se podría haber trabajado con PostgreSQL, el cual tiene una mayor potencia en consultas y mayor complejidad; también se ha barajado MongoDB, que es NoSQL y podríamos utilizar datos variables; o InfluxDB, que es muy utilizada en IoT y está especializada en series temporales.