Проект:Создание БД с разметкой видео (данные, жестикуляция, мимика, текст).
=====================================



Для работы с Базой данных нужно: импортировать бд videos.sql; заменить USER и PASSWORD на логин и пароль от вашего сервера; заменить NAME если импортировали бд под другим именем.
---
Запускать файл: db_class.py (база данных реализована через класс).

БД: videos.sql
http://127.0.0.1:5000/
---

**Таблицы БД:**

meta: id_video, name, date_of_recording, location, author, lang


zhest: id_video, time, zhesticulation


mimic: id_video, time, text


text: id_video, time, text

**Функции:**

Добавлять данные в таблицы

Запрос на всю мимику по имени автора видео(Сложный запрос с JOIN)

Запрос на весь текст после введенной секунды видео(Запрос с WHERE и AND)

Показ таблиц(SELECT *)


P.S. Для заполнения таблицы были взяты открывки из роликов с TED конференций. (https://www.youtube.com/watch?v=k0GQSJrpVhM&t=6s, https://www.youtube.com/watch?v=Zd-h7ImxOnw&t=45s, https://www.youtube.com/watch?v=e72sBt_BSuQ&t=8s)
