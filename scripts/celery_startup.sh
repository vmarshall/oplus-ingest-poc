celery -A oplus beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A oplus worker -l INFO

