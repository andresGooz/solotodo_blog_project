Prueba ingreso desarrollador Full-Stack SoloTodo
Introducción

El siguiente ejercicio espera probar las capacidades de los postulantes al cargo de desarrollador full stack en las tecnologías usadas dentro de SoloTodo.

El contenido del ejercicio mismo no tiene ninguna relación con las actividades comerciales de SoloTodo, y sus respuestas sólo se van a ocupar para evaluar las capacidades de las herramientas utilizadas. En particular no se va a ocupar el contenido de ninguna de las respuestas recibidas dentro de la plataforma de SoloTodo.

El ejercicio mismo consiste en la implementación de una API usando Python y Django, y en el consumo de dicha API por una aplicación implementada en React.

El resultado del ejercicio se puede enviar como dos links a repositorios de GitHub vía el chat de Get On Board o bien como links a dos archivos comprimidos que contengan cada una de las aplicaciones.

El ejercicio no tiene un límite de tiempo o fecha de entrega, pero la postulación quedará cerrada cuando se encuentre un candidato óptimo para el cargo.

Cada proyecto va a tener partes opcionales por incorporar ciertas tecnologías o herramientas que le van a dar puntos extra a la solución entregada.
Parte 1: Desarrollo de API usando Python y Django

La primera parte del ejercicio es la implementación de una API REST utilizando una versión reciente de Python (3.10 o superior) y Django (5.0.6). 

Esta API sólo va a requerir poder crear, listar y visualizar publicaciones (Posts) de un blog.

Requisitos

Configuración

Crear un nuevo proyecto de Django llamado blog_project.

Crear una nueva aplicación de Django llamada blog dentro del proyecto.

Modelos

Crear un modelo Post con los siguientes campos:

title: CharField (longitud máxima 200)
content: TextField
author: CharField (longitud máxima 100)
created_at: DateTimeField (auto_now_add=True)

Admin

Habilitar el admin de Django y que se pueda visualizar el modelo descrito más arriba

Vistas

Crear vistas para manejar las siguientes acciones:

Listar todas las publicaciones del blog.
Obtener los detalles de una publicación específica.
Crear una nueva publicación.

Implementando los siguientes endpoints

/api/posts/ [GET, POST]: Listar todas las publicaciones o crear una nueva publicación.
/api/posts/<id>/ [GET]: Obtener una publicación específica.


Para correr el proyecto final se van a ejecutar los siguientes comandos dentro del directorio del proyecto

Se va a crear y activar un ambiente virtual (virtualenv) vacío
Se van a instalar las dependencias del proyecto ejecutando “pip install -r requirements.txt” (El archivo requirements.txt debe estar incluido en el proyecto)
Se van a correr las migraciones del proyecto (“python manage.py migrate”)
Se va a crear un superusuario (“python manage.py createsuperuser”)
Se va a correr la aplicación (“python manage.py runserver”)

Notas

La base de datos a ocupar es SQLite3
El archivo de settings.py se puede enviar tal cual, incluyendo el campo SECRET_KEY

Puntos extra

Implementar la API utilizando Django REST Framework 

