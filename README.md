## Финальный проект 6 спринта
<hr>

## Студент: Филипченко Сергей

## <h>Когорта: 20fs</h>
<hr>

## <h>Project: Yandex.Scooter</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest tests --alluredir=allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure-results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла                        | Содержание файла                                      |
|---------------------------------------|-------------------------------------------------------|
| Tests dir                             | Директория с тестами                                  |
| test_drop_down.py                     | Тесты на проверку текста у выпадающих списков         |
| test_registration_scooter.py          | Тесты на проверку успешной регистрации аренды скутера |
| test_successful_logo_click_through.py | Тесты на проверку перехода по логотипам               |
| conftest.py                           | Фикстуры                                              |
| helpers.py                            | Хэлпер для тела запросов                              |
| data.py                               | Файл с URL и body запросов                            |
| requirements.txt                      | Файл с зависимостями                                  |
| allure_results.dir                    | Папка с отчетами Allure                               |


