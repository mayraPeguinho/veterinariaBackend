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
4- VER TELEFONO
11- Editar usuario, es posible editar el email... y el rol?? el nombre de usuario idem...

13- Enviar un mail desde la api con codigo, para reestablecer contraseña.

2- ENDPOINTS DE CONFIGURACION HORARIO VETERINARIA, SOLO ADMINS
