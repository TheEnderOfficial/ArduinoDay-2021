# ArduinoDay-2021
Турель с самонаведением
Для конкурса [Arduino Day 2021](https://vk.com/arduinday2021_rostov_on_don)


### Установка
Для установки требуется Python 3 скачать можно с сайта [Python](https://python.org)

Важно указать галоку Add Python To Path
```batch
git clone https://github.com/TheEnderOfficial/ArduinoDay-2021.git
cd ArduinoDay-2021
pip install -r reqs.txt
```


### Технечиские характеристки
+ Турелью - гир-бокс созданый в кружке [Robo.Grade](https://robograde.ru/)
+ Язык программирования - [Python](https://python.org/)
+ Фреймворк для распознавания лиц - [OpenCV](https://opencv.org/
+ Фреймворк для создание графического интерфеса - [Qt](https://qt.io) и [PyQT](https://ru.wikipedia.org/wiki/PyQt)
+ Библиотека для передачи данных из ПО в Турель - [PySerial](https://pypi.org/project/pyserial/)


### API
Турель получает символ означаюший куда ей двигатся
+ U - вверх
+ D - вниз
+ L - влево
+ R - вправо