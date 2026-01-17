# RFD-TOOL

RFD tool

## Cd into django-adminlte-master

```
cd django-adminlte-master
```

## Commands to run

### Activate Venv

```
python3 -m venv venv
source venv/bin/activate
```

```
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
```

### Build (Mac/Linux)

```
# only for linux/mac
chmod +x build.sh
./build.sh
```

### Fallback for build in windows

```
python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate
```

### Runnning the server

```
python3 manage.py runserver
```

```
python manage.py runserver
```
