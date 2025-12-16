# Aplicación Web de Gestión de Tareas – Flask

## Descripción
Este proyecto consiste en una aplicación web desarrollada en **Python con Flask** que permite a los usuarios registrarse, iniciar sesión y gestionar una lista personal de tareas. Cada usuario solo puede ver y administrar sus propias tareas. Además, existe un usuario administrador con permisos para gestionar usuarios del sistema.

## Tecnologías utilizadas
- Python  
- Flask  
- MySQL  
- HTML / CSS  
- Git y GitHub  

## Funcionalidades principales

### Usuarios
- Registro de usuarios mediante formulario  
- Inicio de sesión  
- Cierre de sesión  
- Validación de campos obligatorios  
- No se permiten usuarios duplicados  
- Redirección automática si el usuario ya está logueado  

### Administrador
- Vista de administración de usuarios  
- Eliminación de usuarios  
- Promoción de usuarios a administrador  

Ruta de administración: /admin/usuarios

## Tareas
- Crear tareas  
- Listar tareas del usuario logueado  
- Eliminar tareas  
- Cada tarea pertenece a un único usuario  

## API REST
La aplicación cuenta con un endpoint REST que devuelve las tareas del usuario autenticado en formato JSON: GET /api/tareas

## Programación Orientada a Objetos (POO)
Se implementaron las siguientes clases:
- `Usuario`
- `UsuarioAdmin` (hereda de `Usuario`)
- `Tarea`

Se utilizan atributos, métodos y herencia, cumpliendo con los principios básicos de la Programación Orientada a Objetos.

## Base de Datos
- Se utiliza **MySQL** para la persistencia de datos  
- Se realizan operaciones CRUD:
  - Altas  
  - Bajas  
  - Consultas  
  - Modificaciones  

## Testing
Se incluye un test unitario para la clase `Tarea`, utilizando el módulo `unittest` de Python.

## Diagrama UML

El diagrama UML del modelo de clases se encuentra en:

tareas_flask/uml/uml_clases.png

## Autor
Taiel Matias Castro Gimenez
Proyecto realizado como trabajo práctico para la materia EFSI / DAI.