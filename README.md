# drf-treebeard
django rest framework + docker + postgres + django treebeard


```
docker-compose up --build
```
## create superuser
### 1- go to shell
```
docker exec -it drf-djshop sh
```
### 2- run the manage.py

linux: ``` python3 manage.py createsuperuser --noinput ```

Win: ```py manage.py createsuperuser --noinput```

---
### create a SECRET_KEY




