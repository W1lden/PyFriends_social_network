## [21.07.25] - [Жарас - Разработчик 4]

### Добавлено:
- Реализован просмотр профиля пользователя по адресу `/profiles/<username>/`
- Реализовано редактирование собственного профиля по адресу `/profiles/edit/`
- Добавлен шаблон `profile.html` с отображением биографии, даты рождения и списка постов
- Добавлен шаблон `edit_profile.html` с формой редактирования профиля
- Добавлена модель `UserProfile` и форма `UserProfileForm`
- В `settings.py` подключено приложение `profiles`
- В `urls.py` проекта добавлен маршрут `path("profiles/", include(...))`

### Изменено:
- нет


### Удалено:
- нет


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
