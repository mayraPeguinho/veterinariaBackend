docker compose up -d //contenedor a supabase
docker compose -f docker-compose.yml -f docker-compose.local.yml up --build -d //contenedor con conexion a bd local

Para meternos dentro del contenedor:

docker exec -it Veterinaria-Backend bash
o
docker exec -it Veterinaria-Backend-Local bash

python manage.py init-db  //crear base de datos
python manage.py drop-db  //crear base de datos