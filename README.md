# Взломщик электронного дневника

Проект служит для внесения изменений в базу данных электронного дневника.
Проект работает совместно с проектом [электронного дневника](https://github.com/devmanorg/e-diary/tree/master).

### Как установить

Файле projects/.env должен содержать информацию для подключения к БД и содержать такие параметры:
- DB_ENGINE = django.db.backends.postgresql_psycopg2(используемая БД)
- DB_HOST = checkpoint.devman.org(имя сервера БД)
- DB_PORT = 5434(порт для подключения к БД)
- DB_NAME = checkpoint(имя используемой БД)
- DB_USER(имя пользователя БД)
- DB_PASSWORD(пароль пользователя БД)
- SECRET_KEY(секретный ключ)
- DEBUG(отладочный режим)

Пример .env
```
DB_ENGINE = django.db.backends.postgresql_psycopg2
DB_HOST = checkpoint.devman.org
DB_PORT = 5434
DB_NAME = checkpoint
DB_USER = user
DB_PASSWORD = password

SECRET_KEY = secret_key
DEBUG = false
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Запуск
Проект запускается командой 
```
python manage.py runserver 0.0.0.0:8000.
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).