# Architecture

For this project i'm using 2 docker container:

- NGINX - Web Server
- FLASK - Flask web application with uswsgi server

The frontend was built using Angular and the code is inside the folder angular/client.

## Tech stack

- Angular (v10.2.0) - Frontend framework.
- Flask(1.1.2) - Micro web framework (Python-3.7.2) for the backend.
- Pandas - Python library for data manipulation
- nginx - web server
- uwsgi - It's a WSGI server that help running web application written in Python.
- Docker - Usage of Docker Compose to build and host the application.

# Usage

**NOTE**: Make sure you have Docker, node, npm and angular-cli installed. Check Angular
Prerequisites [here](https://github.com/angular/angular-cli#prerequisites).

- Clone this repository
- **Not Required** - Navigate to angular/client directory and execute:\
  `ng build --configuration="production" --output-path ../../nginx/front`\
  this will create a production build for Angular and put it inside the nginx folder to be served.
- Then navigate back and execute following command:
  - `docker-compose -f docker-compose.yml up --build`

Open: http://localhost

## Running Python Tests:

docker-compose -f docker-compose.yml run --rm flask_demo python manage.py test

## Development:

After installing the requirements for both front and backend, run the following commands in their respective folders:\

- `python run.py`
- `ng serve --configuration=development`
