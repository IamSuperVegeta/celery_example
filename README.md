# Celery Python Example with Flask Api

#####  Install redis server Ubuntu
```
sudo apt install redis-server
```
#####  This starts the redis server
```
redis-server 
```
#####  Commad to kick off redis task manager for project
```
celery -A task worker --pool=solo --loglevel=info
```
#####  run flash project
```
python3 app.py
```