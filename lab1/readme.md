# Laboratory work 1
## Построить веб-систему, поддерживающую заданную функциональность с использованием Python:
* На основе сущностей предметной области создать классы их описывающие.
* Классы и методы должны иметь отражающую их функциональность названия и должны быть грамотно структурированы по пакетам. 
* Информацию о предметной области хранить в БД. В качестве СУБД рекомендуется MySQL или Oracle.
* Приложение должно поддерживать работу с кириллицей (быть многоязычной), в том числе и при хранении информации в БД.
* Архитектура приложения должна соответствовать шаблону Model-View-Controller.
* При реализации алгоритмов бизнес-логики использовать шаблоны GoF: Factory Method, Command, Builder, Strategy, State, Observer etc.
* Используя Django, реализовать функциональности, предложенные в постановке конкретной задачи. Использовать наследование в html templates
* При разработке бизнес логики использовать сессии и фильтры(пример фильтра http://httpbots.com/ru/blog/pishem-prostoj-filtr-dlya-django/).
* Выполнить журналирование событий, то есть информацию о возникающих исключениях и событиях в системе обрабатывать с помощью logging.
* Код должен содержать комментарии.

## Вариант 8
Система `Races`. `Client` делает `Bet` разных видов на `Race`. `Bookmaker` устанавливает уровень выигрыша. `Administrator` фиксирует результаты `Races`.