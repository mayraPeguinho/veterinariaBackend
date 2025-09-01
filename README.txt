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

python manage.py init-db  //crear base de datos
python manage.py drop-db  //eliminar base de datos
