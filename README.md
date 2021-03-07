# Турель с самонаведением ArduinoDay 2021

Для конкурса [Arduino Day 2021](https://vk.com/arduinday2021_rostov_on_don)


# Установка прошивки
[Ссылка на репозиторий прошивки](https://github.com/TheEnderOfficial/ArduinoDay-2021-ArduinoCode)

Для прошивки требуется Arduino IDE скачать можно с сайта [Arduino](https://arduino.cc)
```
git clone https://github.com/TheEnderOfficial/ArduinoDay-2021-ArduinoCode
```
Откройте Arduino IDE

Выберите Файл->Открыть и откройте папку с репозиторием

Выберите Инструменты->Порт и выберите ваш порт

Выберите Инструменты->Плата и выберите вашу плату

Нажмите Ctrl->U и программа загрузится


# Установка программы
Для установки требуется Python 3 скачать можно с сайта [Python](https://python.org)

Важно указать галоку Add Python To Path
```
git clone https://github.com/TheEnderOfficial/ArduinoDay-2021.git
```
```
cd ArduinoDay-2021
```
```
pip install -r reqs.txt
```

# Запуск программы
Перейдите в папку ArduinoDay-2021

И пропишите
```
python main.py
```

# Технечиские характеристки
+ Турелью - гир-бокс созданный в кружке [Robo.Grade](https://robograde.ru/)
+ Язык программирования - [Python](https://python.org/)
+ Фреймворк для распознавания лиц - [OpenCV](https://opencv.org/)
+ Фреймворк для создание графического интерфеса - [Qt](https://qt.io) и [PyQT](https://ru.wikipedia.org/wiki/PyQt)
+ Библиотека для передачи данных из ПО в Турель - [PySerial](https://pypi.org/project/pyserial/)


# API
Турель получает символ означаюший куда ей двигатся
+ U - вверх
+ D - вниз
+ L - влево
+ R - вправо