---------------------------------------------------------------
Imagen con conexión a Supabase

docker compose -p veterinaria-supabase up -d
---------------------------------------------------------------
Imagen con conexión a db local

docker compose -p veterinaria-local -f docker-compose.local.yml up -d
---------------------------------------------------------------

Para meternos dentro del contenedor:

docker exec -it Veterinaria-Backend bash
o
docker exec -it Veterinaria-Backend-Local bash

//crear base de datos
python manage.py init-db

//resetea bd y ejecuta seeds
python manage.py reset-db  

Nombre de las clases CamelCase
metodos ,variables, nombre de archivos que no sean repositories,


Lista a Realizar:
1- Validacion para recursos no encontrados
2- ENDPOINT PARA EDITAR USUARIO
3- SALIDA DE FEHCAS
4- VER TELEFONO
5- paginar usuarios
6- Ver Exception para token expirado
7- REFRESH TOKEN
8- Numero Legajo repetido, ver Excepcion
11- Editar usuario (dependiendo del rol datos que se van a pedir)
12- Eliminar Usuario... seria mas bien desactivar usuario/activar usuario.
13- Enviar un mail desde la ap
i con codigo, para reestablecer contraseña.
14-usuario con la relacion persona, o empleado o responsable en login
15-Definir y asignar permisos


2- ENDPOINTS DE CONFIGURACION HORARIO VETERINARIA, SOLO ADMINS
