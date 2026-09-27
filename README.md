Linux Server Monitor API

API REST desarrollada con Python 3 y Flask para consultar información de un servidor Linux.

El proyecto permite obtener información del sistema, procesos, red, servicios y almacenamiento mediante diferentes endpoints.

---

🎥 Video demostrativo

https://youtu.be/yQVTPIQmP9I?si=0kGZPzHvYFvjWCAy

---

Tecnologías utilizadas

- Python 3
- Flask
- Flask-CORS
- Psutil
- Linux / Ubuntu
- Git y GitHub

---

Funcionalidades

La API proporciona seis endpoints:

- GET "/api/health" Comprueba que la API esté funcionando
- GET "/api/system" Información del sistema, CPU, RAM, disco y uptime
- GET "/api/processes" Procesos y consumo de CPU y memoria
- GET "/api/network" Información y tráfico de red
- GET "/api/services" Estado de los servicios de Linux
- GET "/api/disk" Particiones y uso del almacenamiento

---

Requisitos

- Linux / Ubuntu
- Python 3
- Git

---

Instalación

1. Clonar el repositorio:

```bash

git clone https://github.com/Patogol35/linux-backend-api.git

```

2. Entrar en el proyecto:

```bash

cd linux-backend-api

```

3. Crear el entorno virtual:

```bash

python3 -m venv venv

```

4. Activar el entorno virtual:

```bash

source venv/bin/activate

```

5. Instalar las dependencias:

Para instalar las dependencias, puedes usar una de estas dos opciones:

Opción 1:

```bash

pip install flask-cors psutil

```

Opción 2:

```bash

pip install -r requirements.txt

```

6. Ejecutar la aplicación:

```bash

python3 app.py

```

7. La API estará disponible en:

http://localhost:5000

---

Endpoints

- Health

GET /api/health

Comprueba que el servidor esté funcionando.

- System

GET /api/system

Obtiene información del sistema operativo, CPU, memoria, almacenamiento y tiempo de actividad.

- Processes

GET /api/processes

Obtiene los procesos activos y su consumo de CPU y memoria.

- Network

GET /api/network

Obtiene información de las interfaces de red y estadísticas de tráfico.

- Services

GET /api/services

Consulta los servicios administrados por "systemd" y muestra su estado.

- Disk

GET /api/disk

Obtiene información sobre las particiones, sistemas de archivos y uso del almacenamiento.

---

Objetivo

Este proyecto fue desarrollado como práctica de Linux, Python 3, Flask y APIs REST, utilizando una máquina virtual con Ubuntu para obtener información real de los recursos y servicios del sistema.

---

Autor Jorge Patricio Santamaría Cherrez Máster en Ingeniería de Software y Sistemas Informáticos
