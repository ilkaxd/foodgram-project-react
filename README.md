# foodgram-project
[![foodgram_workflow](https://github.com/ilkaxd/foodgram-project-react/actions/workflows/foodgram_workflow.yaml/badge.svg)](https://github.com/ilkaxd/foodgram-project-react/blob/master/.github/workflows/foodgram_workflow.yaml)

[![Python](https://img.shields.io/badge/-Python-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-darkgreen)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django_REST_Framework-darkred)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-darkblue)](https://www.postgresql.org/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-brightgreen)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-blue)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-blue)](https://cloud.yandex.ru/)

# Оглавление
- [Техническое описание проекта](#техническое-описание-проекта)
    - [Исходники](#исходники)
    - [Структура проекта](#структура-проекта)
    - [Базовые модели проекта](#базовые-модели-проекта)
        - [Рецепт](#рецепт)
        - [Тег](#тег)
        - [Ингредиент](#ингредиент)
        - [Пользователь](#пользователь)
    - [Страницы проекта](#страницы-проекта)
        - [Главная страница](#главная-страница)
        - [Страница рецепта](#страница-рецепта)
        - [Страница пользователя](#страница-пользователя)
        - [Подписка на авторов](#подписка-на-авторов)
        - [Список избранного](#список-избранного)
        - [Список покупок](#список-покупок)
        - [Фильтрация по тегам](#фильтрация-по-тегам)
    - [Регистрация и авторизация](#регистрация-и-авторизация)
        - [Уровни доступа пользователей](#уровни-доступа-пользователей)
        - [Возможности неавторизованных пользователей](#возможности-неавторизованных-пользователей)
        - [Возможности авторизованных пользователей](#возможности-авторизованных-пользователей)
        - [Возможности администраторов](#возможности-администраторов)
    - [Настройки админки](#настройки-админки)
        - [Модель пользователей](#модель-пользователей)
        - [Модель рецептов](#модель-рецептов)
        - [Модель ингредиентов](#модель-ингредиентов)
    - [Общие технические требования и инфраструктура](#общие-технические-требования-и-инфраструктура)
- [Запуск проекта](#запуск-проекта)
    - [Локальный запуск проекта](#локальный-запуск-проекта)
    - [Запуск проекта на сервере](#запуск-проекта-на-сервере)

# Техническое описание проекта
Проект - сайт Foodgram, «Продуктовый помощник», представляющий онлайн-сервис и API для него. В рамках сервиса пользователи могут: 
- публиковать рецепты
- подписываться на публикации других пользователей
- добавлять понравившиеся рецепты в список «Избранное»
- скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд

**[⭯ К огравлению](#оглавление)**

## Исходники
В рамках проекта были предоставлены:
- готовый фронтенд
- структура приложения

**[⭯ К огравлению](#оглавление)**

## Структура проекта
Проект имеет следующую структуру:
- frontend - содержит файлы, необходимые для сборки фронтенда приложения
- infra - содержит всю инфраструктуру проекта: конфигурационный файл nginx и docker-compose.yaml
- backend - разработанный в рамках проекта бэкенд продуктового помошника
- data - список ингредиентов с единицами измерения в форматах JSON и CSV для загрузки в БД
- docs - файлы спецификации API

**[⭯ К огравлению](#оглавление)**

## Базовые модели проекта

Более подробно с базовыми моделями можно ознакомиться в [спецификации API](#Тут-ссылка-на-redoc).

**[⭯ К огравлению](#оглавление)**

### Рецепт

Рецепт описывается следующими полями:
- Автор публикации (пользователь)
- Название
- Картинка
- Текстовое описание
- Ингредиенты: продукты для приготовления блюда по рецепту. Множественное поле с выбором из предустановленного списка, с указанием количества и единицы измерения
- Тег
- Время приготовления в минутах

Все поля обязательны для заполнения.

**[⭯ К огравлению](#оглавление)**

### Тег

Тег описывается следующими полями:
- Название
- Цветовой HEX-код (например, #93aa00)
- Slug

Все поля обязательны для заполнения.

**[⭯ К огравлению](#оглавление)**

### Ингредиент

Данные об ингредиентах хранятся в нескольких связанных таблицах:
- Название
- Количество
- Единицы измерения

Все поля обязательны для заполнения.

**[⭯ К огравлению](#оглавление)**

### Пользователь

User описывается следующими полями:
- Логин
- Пароль
- Email
- Имя
- Фамилия

## Страницы проекта

Дизайн-макеты проекта можно посмотреть на [Figma](https://www.figma.com/file/HHEJ68zF1bCa7Dx8ZsGxFh/Продуктовый-помощник-(Final)?node-id=0%3A1)
(может не прогрузиться с первого раза, просто перезагружаем её)

**[⭯ К огравлению](#оглавление)**

### Главная страница

Содержимое главной страницы - список первых шести рецептов, отсортированных по дате публикации (от новых к старым). Остальные рецепты доступны на следующих страницах: внизу страницы есть пагинация.

**[⭯ К огравлению](#оглавление)**

### Страница рецепта

На странице - полное описание рецепта. Для авторизованных пользователей имеются следующие возможности:
- добавить рецепт в избранное
- добавить рецепт в список покупок
- подписаться на автора

**[⭯ К огравлению](#оглавление)**

### Страница пользователя

Страница содержит:
- имя пользователя
- все рецепты, опубликованные пользователем
- кнопку подписаться на пользователя

**[⭯ К огравлению](#оглавление)**

### Подписка на авторов

Подписка на публикации доступна только авторизованному пользователю. Страница подписок доступна только владельцу.

Сценарий поведения пользователя:

1. Пользователь переходит на страницу другого пользователя или на страницу рецепта и подписывается на публикации автора кликом по кнопке «Подписаться на автора».
2. Пользователь переходит на страницу «Мои подписки» и просматривает список рецептов, опубликованных теми авторами, на которых он подписался. Сортировка записей — по дате публикации (от новых к старым).
3. При необходимости пользователь может отказаться от подписки на автора: переходит на страницу автора или на страницу его рецепта и нажимает «Отписаться от автора».

**[⭯ К огравлению](#оглавление)**

### Список избранного

Работа со списком избранного доступна только авторизованному пользователю. Список избранного может просматривать только его владелец.

Сценарий поведения пользователя:
1. Пользователь отмечает один или несколько рецептов кликом по кнопке «Добавить в избранное».
2. Пользователь переходит на страницу «Список избранного» и просматривает персональный список избранных рецептов.
3. При необходимости пользователь может удалить рецепт из избранного.

**[⭯ К огравлению](#оглавление)**

### Список покупок

Работа со списком покупок доступна авторизованным пользователям. Список покупок может просматривать только его владелец.

Сценарий поведения пользователя:

1. Пользователь отмечает один или несколько рецептов кликом по кнопке «Добавить в покупки».
2. Пользователь переходит на страницу Список покупок, там доступны все добавленные в список рецепты.
3. Пользователь нажимает кнопку Скачать список и получает файл с суммированным перечнем и количеством необходимых ингредиентов для всех рецептов, сохранённых в «Списке покупок».
4. При необходимости пользователь может удалить рецепт из списка покупок.

Список покупок скачивается в формате txt или PDF

При скачивании списка покупок ингредиенты в результирующем списке не должны дублироваться; если в двух рецептах есть сахар (в одном рецепте 5 г, в другом — 10 г), то в списке должен быть один пункт: Сахар — 15 г.


В результате список покупок может выглядеть так:
- Фарш (баранина и говядина) (г) — 600
- Сыр плавленый (г) — 200
- Лук репчатый (г) — 50
- Картофель (г) — 1000
- Молоко (мл) — 250
- Яйцо куриное (шт) — 5
- Соевый соус (ст. л.) — 8
- Сахар (г) — 230
- Растительное масло рафинированное (ст. л.) — 2
- Соль (по вкусу) — 4
- Перец черный (щепотка) — 3

**[⭯ К огравлению](#оглавление)**

### Фильтрация по тегам

При нажатии на название тега выводится список рецептов, отмеченных этим тегом. Фильтрация может проводится по нескольким тегам в комбинации «или»: если выбраны несколько тегов — в результате показываются рецепты, которые отмечены хотя бы одним из этих тегов.
При фильтрации на странице пользователя фильтруются только рецепты выбранного пользователя. Такой же принцип соблюдается при фильтрации списка избранного.

**[⭯ К огравлению](#оглавление)**

## Регистрация и авторизация

В проекте имеется система регистрации и авторизации пользователей. Управление пользователями собрано в приложении users

**[⭯ К огравлению](#оглавление)**

### Уровни доступа пользователей

- Гость (неавторизованный пользователь)
- Авторизованный пользователь
- Администратор

**[⭯ К огравлению](#оглавление)**

### Возможности неавторизованных пользователей

- Создание аккаунт.
- Просмотр рецептов на главной.
- Просмотр отдельной страницы рецептов.
- Просмотр страницы пользователей.
- Фильтрация рецептов по тегам.

**[⭯ К огравлению](#оглавление)**

### Возможности авторизованных пользователей

- Вход в систему под своим логином и паролем.
- Выходи из системы (разлогирование).
- Смена своего пароля.
- Создание/редактирование/удаление собственных рецептов
- Просмотр рецептов на главной странице.
- Просмотр страницы пользователей.
- Просмотр отдельной страницы рецепта.
- Фильтрация рецептов по тегам.
- Работа с персональным списком избранного: добавление/удаление в/из него рецептов, просмотр своей страницы избранных рецептов.
- Работа с персональным списком покупок: добавление/удалять любые рецепты, выгружать файл со количеством необходимых ингридиентов для рецептов из списка покупок.
- Подписка на публикации авторов рецептов и отмена подписки, просмотр своей страницы подписок.

**[⭯ К огравлению](#оглавление)**

### Возможности администраторов

Администратор обладает всеми правами авторизованного пользователя. Плюс к этому он может:

- изменять пароль любого пользователя,
- создавать/блокировать/удалять аккаунты пользователей,
- редактировать/удалять любые рецепты,
- добавлять/удалять/редактировать ингредиенты.
- добавлять/удалять/редактировать теги.

**[⭯ К огравлению](#оглавление)**

## Настройки админки

Админ-зона настроена на работа с указанными ниже моделями и фильтрами. Выводятся все модели с возможностью редактирования и удаления записей

**[⭯ К огравлению](#оглавление)**

### Модель пользователей

Добавлен фильтр списка по email и имени пользователя

**[⭯ К огравлению](#оглавление)**

### Модель рецептов

- В списке рецептов выводится название и автор рецепта
- Имеются фильтры по автору, названию рецепта и тегам
- На странице рецепта выводится общее число добавлений этого рецепта в избранное

**[⭯ К огравлению](#оглавление)**

### Модель ингредиентов

- В списке выводится название ингредиента и единица измерения
- Имеется фильтр по названию

**[⭯ К огравлению](#оглавление)**

## Общие технические требования и инфраструктура

- Проект использует базу данных PostgreSQL
- В Django-проекта имеется файл requirements.txt со всеми зависимостями
- Проект запускает в трёх контейнерах:
    - nginx
    - PostgreSQL
    - Django
через docker-compose на севере в Яндекс.Облаке. Образ с проектом запушен на Docker Hub
Контейнер frontend используется лишь для подготовки файлов.

**[⭯ К огравлению](#оглавление)**

# Запуск проекта
Тут добавим описание

**[⭯ К огравлению](#оглавление)**

## Локальный запуск проекта
Тут добавим описание для запуска проекта локально

**[⭯ К огравлению](#оглавление)**

## Запуск проекта на сервере
Тут добавим описание для запуска проекта на сервере

**[⭯ К огравлению](#оглавление)**