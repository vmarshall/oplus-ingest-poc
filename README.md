# PARTNER INTEGRATOR

 This assumes you have a linux machine of osx box to deploy on. 
 This is a very rough set of instructions so YMMV.

# Installation

- install django
- install postgresql
   - create 'partner' database and user
   - see partner-database.ini for details
   - start postgresql
- install redis
  - start redis
- install rabbitmq
  - setup rabbitmq ( see scripts/rabbitmq.sh )
  - start rabbitmq
- install opensearch
  - start opensearch
  - create indexes later ( via django commands )
- install opensearch-dashboards
   - start opensearch-dashboards

- navigate to oplus directory
- create virtualenv and activate it
  - python -m venv venv
  - source venv/bin/activate
- install python/django deps
  - pip install -r requirements.txt
- create a superuser
  - python manage.py createsuperuser
  - follow prompts
- run migration
  - python manage.py migrate
  - Note: for the purposes of this demo, Django is running on sqlite3, the partnerdb is in postgres
- run the server
  - python manage.py runserver
- load fixture data
  - load fixture data
    - python manage.py loaddata fixtures/initial_data.json
    - ( this *should* work, but if it doesn't, you can load the data manually )
      - load data manually
        - Sample Data
          - data/patient_data.csv
          - data/partner_doctor_note.csv
          - data/patient_data.sql
- load partner data
  - Sample Data
    - data/partner_data.sql
    - data/partner_doctor_note.csv
    - data/patient_data.csv
- start celery workers
  - celery -A oplus beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
  - celery -A oplus worker -l INFO

# Configuration

Partner database is defined in `partner-database.ini` file.

oplus/settings.py is where most things are defined

# Important Config Settings
CELERY_BROKER_URL = "amqp://partner:partner@localhost:5672/partner_vhost"


# Docker Setup ( wip )

   (Optional, not-really setup completely )
  > edit docker-compose.yml as appropriate
  > docker-compose up -d --build

  
## API

- Swagger API Documentation: http://localhost:8000/swagger/
- Redoc API Documentation: http://localhost:8000/redoc/

## PDF Generation

generates PDF from first record

- https://localhost:8000/pdf/

## Synchronizing with Partner Database

Two Methods:
1. Celery Beat
2. Django Management Command
  
    Celery Beat
    > celery -A oplus beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

[Schedule Syncs via Admin UI](http://127.0.0.1:8000/admin/django_celery_beat/periodictask/)

Django Management Command
> python manage.py sync_partner_database
