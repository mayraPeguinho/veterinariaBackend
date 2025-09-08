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

//tirar base de datos  
python manage.py drop-db  

python manage.py reset-db  