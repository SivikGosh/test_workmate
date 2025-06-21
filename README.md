# test_workmate

Программа разрабатывалась на Python 3.12.

## Установка и запуск

```bash
$ git clone git@github.com:SivikGosh/test_workmate.git
$ cd test_workmate/
$ python3.12 -m venv venv
$ source venv/bin/activate

(venv) $ pip3 install -r requirements.txt
(venv) $ python3.12 -m parser.main --file ./product.csv
```

#### Вывод тестовых данных без каких-либо доп. условий

![Без условий](screenshots/full.jpg)

## Команды

### Аргумент '--where'

| поле       | доступные операции | примечание                             |
|-----------:|:------------------:|:---------------------------------------|
| name       | =                  | доступен поиск по частичному значению. |
| brand      | =                  | доступен поиск по частичному значению. |
| brandprice | >, <, =            |                                        |
| rating     | >, <, =            |                                        |

#### Примеры:
![Название](screenshots/where_name.jpg)
![Брэнд](screenshots/where_brand.jpg)
![Цена больше](screenshots/where_price_more.jpg)
![Цена меньше](screenshots/where_price_less.jpg)
![Цена](screenshots/where_price_eq.jpg)
![Рейтинг больше](screenshots/where_rating_more.jpg)
![Рейтинг меньше](screenshots/where_rating_less.jpg)
![Рейтинг](screenshots/where_rating_eq.jpg)

#### В случае ошибки, данные не фильтруются:
![Рейтинг](screenshots/where_error.jpg)

### Аргумент '--aggrerate'

| поле       | доступные операции |
|-----------:|:------------------:|
| brandprice | avg, min, max      |
| rating     | avg, min, max      |

#### Примеры:
![Цена средняя](screenshots/price_avg.jpg)
![Цена минимальная](screenshots/price_min.jpg)
![Цена максимальная](screenshots/price_max.jpg)
![Рейтинг средний](screenshots/rating_avg.jpg)
![Рейтинг минимальный](screenshots/rating_min.jpg)
![Рейтинг максимальный](screenshots/rating_max.jpg)

### Аргумент '--order-by'

| поле       | доступные операции |
|-----------:|:------------------:|
| name       | asc, desc          |
| brand      | asc, desc          |
| brandprice | asc, desc          |
| rating     | asc, desc          |

#### Примеры:
![Название по возрастанию](screenshots/name_asc.jpg)
![Название по убыванию](screenshots/name_desc.jpg)
![Брэнд по возрастанию](screenshots/brand_asc.jpg)
![Брэнд по убыванию](screenshots/brand_desc.jpg)
![Цена по возрастанию](screenshots/price_asc.jpg)
![Цена по убыванию](screenshots/price_desc.jpg)
![Рейтинг по возрастанию](screenshots/rating_asc.jpg)
![Рейтинг по убыванию](screenshots/rating_desc.jpg)


### Комбинирование аргументов
#### --where и --aggregate:
![Фильтрация и аггрегация](screenshots/where_and_aggregate.jpg)
#### --where и --order-by:
![Фильтрация и аггрегация](screenshots/where_and_order.jpg)

## Тестирование

### Покрытие кода тестами выполнено на 100%
![Фильтрация и аггрегация](screenshots/coverage.jpg)

### В проект также включены mypy, isort, flake8. Вместе с pytest они автоматически запускаются в пре-коммите.

```bash
# автотесты
(venv) $ pre-commit install  # активация пре-коммита
```

### Ручной прогон тестов, форматтеров и линтеров

```bash
# автотесты
(venv)$ pytest . -v

# покрытие тестами
(venv)$ pytest . --cov=parser  # вывод в консоль
(venv)$ pytest . --cov=parser --cov-report=html  # формирование отчёта

(venv)$ make install  # установка библиотек (нужно только 1 раз)
(venv)$ make check  # проверка на типы, импорты, PEP8
```
