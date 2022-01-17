# alto
app to try out different deployments

# Project Structure
- `services/` has the main web app 
- `other-apps/` has experimental mini apps

# References (aka things I copied)
Initial tutorial for getting a Flask proejct setup by Michael Herman
- https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#project-setup
- https://github.com/testdrivenio/flask-on-docker

- Bulma.io for CSS https://bulma.io/ 

Spotipy
- Spotipy library for Spotify API https://github.com/plamere/spotipy
- Spotipy Flask example for authenticating and querying information about the user https://github.com/plamere/spotipy/blob/master/examples/app.py


# Cheatsheet for running it
## Running it locally with flask
- `cd services/web/`
- `export FLASK_APP=project/__init__.py`
- `python3 manage.py run`

## Running containers locally with docker compose
From project root:

```
docker-compose down -v
docker-compose up -d --build
docker-compose exec web python manage.py create_db
docker-compose exec web python manage.py seed_dbv
```

## Running  "prod" compose locally
```
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
```

## Deploying as containers inside a VM
* Really not the best way to do this, but its an easier starting point based off the notion that I straight copy & pasted some of this stuff.
* https://cloud.google.com/community/tutorials/docker-compose-on-container-optimized-os 
* MAKE SURE HTTP TRAFFIC IS ON

```
git clone <this repo>

# sync over the .env.prod and .env.prod.db files

chmod +x ~/alto/services/web/entrypoint.prod.sh

docker run docker/compose version

docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:$PWD" \
    -w="$PWD" \
    docker/compose -f docker-compose.prod.yml up -d --build

docker run --rm \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:$PWD" \
    -w="$PWD" \
    docker/compose -f docker-compose.prod.yml exec web python manage.py create_db
```
