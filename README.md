### Описание
   Тестовое задание. 
   <details><summary>Описание задания</summary>

   1.	С помощью Docker (предпочтительно - docker-compose) развернуть образ с любой опенсорсной СУБД (предпочтительно - PostgreSQL).  
      Предоставить все необходимые скрипты и конфигурационные (docker/compose) файлы для развертывания СУБД,  
      а также инструкции для подключения к ней. Необходимо обеспечить сохранность данных при рестарте контейнера  
      то есть - использовать volume-ы для хранения файлов СУБД на хост-машине.  
   2.	Реализовать на Python3 веб сервис (с помощью FastAPI или Flask, например), выполняющий следующие функции:
      2.1.	В сервисе должно быть реализован POST REST метод, принимающий на вход запросы с содержимым вида {"questions_num": integer}.  
      2.2.	После получения запроса сервис, в свою очередь, запрашивает с публичного API (англоязычные вопросы для викторин) https://jservice.io/api/random?count=1 указанное в полученном запросе количество вопросов.  
      2.3.	Далее, полученные ответы должны сохраняться в базе данных из п. 1, причем сохранена должна быть как минимум следующая информация  
            (название колонок и типы данный можете выбрать сами, также можете добавлять свои колонки): 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса.  
            В случае, если в БД имеется такой же вопрос, к публичному API с викторинами должны выполняться дополнительные запросы до тех пор, пока не будет получен уникальный вопрос для викторины.
      2.4.	Ответом на запрос из п.2.a должен быть предыдущей сохранённый вопрос для викторины. В случае его отсутствия - пустой объект.  
   3.	В репозитории с заданием должны быть предоставлены инструкции по сборке докер-образа с сервисом из п. 2., его настройке и запуску. А также пример запроса к POST API сервиса.
   4.	Желательно, если при выполнении задания вы будете использовать docker-compose, SQLAalchemy,  пользоваться аннотацией типов.

   </details>  
   
   Реализован веб сервис на FastAPI, с возможностью получения и сохранения в базе данных  
   необходимого количества вопросов, с ресурса https://jservice.io/api/random?count=1<br/>  
   База данных - PostgreSQL  
   ORM - SQLAlchemy, миграции - Alembic  
   Проект разворачивается с помощью docker compose  
   Python версии 3.11.1
### Технологии:
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![FastAPI](https://img.shields.io/badge/FastAPI-092E20?style=for-the-badge&logo=FastAPI&logoColor=green)
![Docker](https://img.shields.io/badge/Docker-092E20?style=for-the-badge&logo=docker&logoColor=blue)
### Используемые пакеты:
* fastapi==0.95.2
* asyncpg==0.27.0  
* httpx==0.24.0  
* uvicorn==0.22.0  
* SQLAlchemy==2.0.13  
* alembic==1.11.0  
* python-dotenv==1.0.0  

### Установка

1. Клонировать репозиторий:

   ```python
   git clone ...
   ```

2. Перейти в папку с проектом:

   ```python
   cd quize_test_task/
   ```

3. Создать и запустить контейнер:

   ```python
   docker-compose up -d
   ```

4. (Опционально) Панель управления pgadmin доступна по адресу http://localhost:5050/  
    Авторизация:  
    email=pgadmin4@pgadmin.org  
    password=admin  
    Подключение к базе:  
    1.  
    ![image](https://github.com/Asterrus/quize_test_task/assets/59145527/550ec784-0231-46cc-a50d-f3a9b937cff7)   
    2.  
    ![image](https://github.com/Asterrus/quize_test_task/assets/59145527/61eb020e-64f8-4c87-b936-4afe72274dba)   
    3.  
    ![image](https://github.com/Asterrus/quize_test_task/assets/59145527/b6a463f2-d25c-46c9-823d-7ca60c623b2a)   

### Дополнительно

* Ресурс доступен по адресу:
   ```
   http://localhost:8000/
   ```

* Документация:
   ```
   https://localhost:8000/docs
   ```
### Пример запроса
* Первый запрос. В базе нет вопросов.  
    `POST http://localhost:8000/get_questions?questions_num=10`
* Пример ответа:
    ```json
    null
    ```
* Второй запрос.  
    `POST http://localhost:8000/get_questions?questions_num=10`
* Пример ответа:
    ```json
    {
        "question_id": 210551,
        "question_text": "Here's the logo of this nonprofit newsroom that uses the moral force of investigative journalism",
        "answer_text": "ProPublica",
        "created_at": "2022-12-30T21:59:23.562000+00:00",
        "id": 8
    }
    ```

### Автор проекта 
* Роман Дячук   

