<h1>Тестовое ITK</h1>
<p>Реализовано FastAPI приложение с 5 эндпоинтами:</p>
<p><ul>
  <li>list - получить весь список людей, опционально - query-параметр age. Выполняет поиск всех людей по возрасту</li>
  <li>get - получить 1 человека по id</li>
  <li>create - создать запись</li>
  <li>update - редактировать запись</li>
  <li>delete - удалить запись</li>
</ul></p>

Для запуска проекта:</br>
Создать файл ".env" </br>
Пример заполнения файла:</br>
DATABASE_URL = 'postgresql+psycopg2://username:password@localhost/db_name'</br>
POSTGRES_USER = username</br>
POSTGRES_PASSWORD = password</br>
POSTGRES_DB = database_name</br>

Создать таблицу:</br>
alembic revision --autogenerate -m "init" - сохранить миграцию</br>
alembic upgrade head - применить миграции</br>
