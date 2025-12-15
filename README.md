# de-test-task

## Задание 1
Можно найти в `task_1.py`

## Задание 2
Можно найти в `task_2.py`


## Задание 3
### Что такое ETL

Extract: Извлечение данных из разных источников.

Transform: Очистка и приведение данных в порядок.

Load: Загрузка готовых данных в целевое хранилище.

### Какие решают задачи
Разрозненность данных: Позволяют собрать данные из десятков разных систем в одном месте.

Качество данных: Автоматически чистят "мусор" и приводят форматы к стандарту.

Автоматизация: Заменяют ручной труд (Excel-таблицы) на автоматические скрипты, работающие по расписанию.



## Задание 4
Оконная функция это функция, которая выполняет действия над набором строк.
Например `AVG(salary) OVER (PARTITION BY department) as avg_dept_salary` средняя зп по отделу в котором работает сотрудник.


## Задание 5
Самый простой это через ide, пару кнопок и готово:) 

Или используя venv `python -m venv .venv` и активирость его `venv\Scripts\activate`

Есть ещё `virtualenv`  `Conda` `Pipenv`


## Задание 6
Можно так `pip install название_библиотеки`
Или из файла `pip install -r requirements.txt`





# Текст задания
Тестовые вопросы
1. У тебя есть ответ из сервиса в формате JSON:
```
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```

a) Получи имена участников Супергеройского отряда. Каким образом ты их получил?
b) Получи суперсилу каждого участника. Каким образом ты это сделал?

2. Существует строка со следующим содержанием “01 июля 2025 года”.
Приведи строку к такому виду, чтобы можно было записать её в таблицу базы с типом данных Date. Как ты это сделал?

3. Что такое ETL инструменты? Какие проблемы они решают?

4. Что такое оконная функция в SQL?

5. Как можно создать виртуальное окружение для python?

6. Каким образом быстро установить библиотеки для проекта на python?
