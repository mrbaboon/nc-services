docker-compose build
docker-compose up -d mariadb adminer redis mailcatcher

docker-compose run --rm ncservices python manage.py migrate

docker-compose up -d ncservices worker beat
