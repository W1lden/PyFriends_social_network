## [17.07.25] - [Айша - Разработчик 5]

### Добавлено:
- CHANGELOG.md
- Dockerfile, docker compose, .dockerignore
- base.html
- .env
- .flake8, .pre-commit-config.yaml
- requirements: base.txt, dev.txt
- posts app

### Изменено:
- ...

### Удалено:
- ...

## [18.07.25] - [Arsen - Разработчик 2]

### Добавлено:
- Posts model
- Admin posts
- post_detail.html, post_form.html, all_posts.html
- constants.py
- forms.py

### Изменено:
- urls.py
- views.py

### Удалено:
- ...


## [18.07.25] - [Асан - Разработчик 1]

### Добавлено:
- приложение users (авторизация);
- миграции users;
- шаблоны login, register в templates.

### Изменено:
- friends/urls.py: добавил маршрут users и logout;
- header.html: добавил ссылку на страницы входа и регистрации;
- header.html: убрал кнопку входа и регистрации для авторизованных пользователей;
- header.html: добавил кнопку выхода для авторизованных пользователей;
- settings.py: добавил приложение users и кастомную модель CustomUser;
- удалил лишние комменты в py файлах каталога friends/friends;
- .flake8: изменил migrations на */migrations/*, чтобы не проверять миграции приложений.
