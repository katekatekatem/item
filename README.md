### **Автор проекта:**

Екатерина Мужжухина

Python Backend Developer

github: @katekatekatem

e-mail: muzhzhukhina@mail.ru


### **Используемые технологии:**

Python 3, Django, HTML, PostgreSQL, Docker


### **База данных и переменные окружения:**

Проект использует базу данных PostgreSQL.
Для подключения и выполненя запросов к базе данных необходимо создать файл ".env" в папке "./item_project/".

Нужно переименовать файл example.env в .env и заполнить его своими данными:

```
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY='Здесь указать секретный ключ'
ALLOWED_HOSTS='Здесь указать имя или IP хоста' (для локального запуска - 127.0.0.1)
DEBUG=False
STRIPE_SECRET_KEY='Здесь секретный ключ Stripe'
```


### **Как запустить проект локально:**

Клонировать репозиторий и перейти в него в командной строке:

> git clone git@github.com:katekatekatem/item.git

Перейдите в папку проекта item и запустите оркестр контейнеров:

> docker-compose up -d

После успешного запуска контейнеров выполните миграции:

> docker exec backend python manage.py migrate

Создать суперюзера:

> docker exec backend python manage.py createsuperuser


Запустится проект и будет доступен по адресу [localhost:8000](http://localhost:8000/).
