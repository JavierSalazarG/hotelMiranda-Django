# Hotel Miranda

¡Bienvenido a Hotel Miranda! Este proyecto, desarrollado en Python 3 con el framework Django, te ofrece una solución completa para la gestión de hoteles. Desde la administración de habitaciones y reservas hasta la gestión de personal, Hotel Miranda simplifica tus tareas diarias.

## Configuración del Entorno

Antes de comenzar, asegúrate de tener Python 3 instalado en tu sistema. Se recomienda utilizar un entorno virtual (venv) para gestionar las dependencias del proyecto. Puedes crear y activar el entorno virtual con los siguientes comandos:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

## Configuración de la Base de Datos

Este proyecto utiliza SQLite como base de datos por defecto. Realiza las migraciones necesarias con los siguientes comandos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Ejecución del Proyecto

Inicia el servidor de desarrollo con el siguiente comando:

```bash
python manage.py runserver

```

Accede a la aplicación a través de tu navegador web visitando http://localhost:8000/.

## Características Principales

. Gestión de Habitaciones: Registra y administra información detallada sobre las habitaciones disponibles, incluyendo características, tarifas y disponibilidad.

. Reservas: Realiza y gestiona reservas de habitaciones, proporcionando un sistema eficiente para rastrear las fechas de entrada, salida y detalles de los huéspedes.

. Gestión de Trabajadores: Administra la información del personal del hotel, incluyendo detalles de contacto, roles y responsabilidades.
