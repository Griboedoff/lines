##Декомпозиция 
Модель игры лежит в директории `Model`. 
В основе класс `GameField`, реализующий игровое поле. 
Классы `Ball, Line, Cell` - классы контейнеры хранящие состояния конкретных объектов.
Класс `BallGenerator` - реализует логику создания и добавления шаров на поле.

В директории `Interfaces` лежит класс `Controller`, реализующий логику рекации на игровые события.

В директории `Gui` лежат классы `GuiController`, `GuiField`- расширения классов `Controller` и `GameField` для работы с ГУИ, вся логика отрисовки в `GuiField`. Модуль `gui_main` необходим для запуска игры с интерфейсом.
В директории `Console` лежат классы `ConsoleController`, `ConsoleField`- расширения классов `Controller` и `GameField` для работы в пакетном режиме. Модуль `console_main` необходим для запуска пакетного режима.

Тесты лежат в директории `Tests`. 

В файле `config.py` - описаны константы использующиеся в программе.
