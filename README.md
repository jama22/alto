# alto
app to try out different deployments

# Things I copied
Initial tutorial for getting a Flask proejct setup by Michael Herman
- https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#project-setup
- https://github.com/testdrivenio/flask-on-docker

# Commands to run for local dev compose
```
docker-compose down -v
docker-compose up -d --build
docker-compose exec web python manage.py create_db
docker-compose exec web python manage.py seed_dbv
```

# Dommands to run for "prod" compose
```
docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
```

# Deploying as containers on a VM
* Really not the best way to do this, but its an easier starting point based off the notion that I straight copy & pasted some of this stuff.
* https://cloud.google.com/community/tutorials/docker-compose-on-container-optimized-os 

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
