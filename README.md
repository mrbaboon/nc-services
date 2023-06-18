# NCDot Services Site

### Environment Setup

##### Requirements

* Docker
* Docker Compose

##### Setup

Create your .env file from the example `sample.env`.  Ensure any empty values are filled out.

The *callback uri* should be set to `http://localhost:8000/sso/callback`

You'll need ESI credentials from [https://developers.eveonline.com/](https://developers.eveonline.com/)

```
cp sample.env .env
```

Build the docker image

```
docker-compose build
```

Start the stack

```
docker-compose up -d
```

Run the migrations

```
docker-compose run ncservices python manage.py migrate
```

Create a superuser

```
docker-compose run ncservices python manage.py createsuperuser
```


### Development

The alliance-auth server can be accessed at [http://localhost:8000](http://localhost:8000)

The MYSQL database can be accessed via PHPMyAdmin at [http://localhost:3380](http://localhost:3380)

Outgoing email is sent to a [Mailcatcher](https://mailcatcher.me/) container via port 1025.  This service can be accessed at [http://localhost:1080](http://localhost:1080)
