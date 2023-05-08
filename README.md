# English: Text-to-Speech with Virtual Microphone
This project is a Python script that converts text to speech and outputs it to a virtual microphone.

The script utilizes the ffmpeg and VB-Cable tools, so make sure they are installed on your computer before using it.

## Dependencies Installation
Before using the script, make sure you have the following tools installed:

- [ffmpeg](https://www.gyan.dev/ffmpeg/builds/): A multimedia framework for processing audio and video files.
- [VB-Cable](https://vb-audio.com/Cable/): A virtual audio device for routing audio signals.

## Python Dependencies Installation
1. Install Python on your computer if it is not already installed. You can download Python from the official website.

2. Install the required libraries:
```pip install -r requirements.txt```

## FFMPEG Installation - Windows:
A. Extract the downloaded archive and rename the FFmpeg folder to "ffmpeg". Note down the full path to the ffmpeg folder.
B. Add the path to the ffmpeg folder to the system PATH variable:

Open "Control Panel" -> "System" -> "Advanced system settings" -> "Environment Variables".
- In the "System variables" section, find the variable PATH and click "Edit".
- Add the full path to the ffmpeg folder (e.g., C:\path\to\ffmpeg) as a new value for the PATH variable. Note that each path is separated by a semicolon (;).
- Click "OK" to save the changes.

## FFMPEG Installation - Linux (Ubuntu/Debian):
Install FFmpeg using the following command: ```sudo apt-get install ffmpeg```


# Russian: Преобразование текста в речь с использованием виртуального микрофона
Этот проект представляет собой скрипт на языке Python, который преобразует текст в речь и выводит его в виртуальный микрофон. 

Скрипт использует инструменты ffmpeg и VB-Cable, поэтому перед использованием убедитесь, что они установлены на вашем компьютере.

## Установка зависимостей
Перед началом использования скрипта, убедитесь, что у вас установлены следующие инструменты:

- [ffmpeg](https://www.gyan.dev/ffmpeg/builds/): Мультимедийный фреймворк для обработки аудио и видео файлов.
- [VB-Cable](https://vb-audio.com/Cable/): Виртуальное аудиоустройство для перенаправления аудио сигналов.

## Установка Python зависимостей

1. Установите Python на вашем компьютере, если он еще не установлен. Вы можете загрузить Python с [официального сайта](https://www.python.org/downloads/).

2. Установите необходимые библиотеки:
```pip install -r requirements.txt```

## Установка FFMPEG - Windows:

A. Распакуйте загруженный архив и переименуйте папку FFmpeg в "ffmpeg". Обратите внимание на полный путь к папке ffmpeg.

B. Добавьте путь к папке ffmpeg в системную переменную PATH:

Откройте "Панель управления" -> "Система" -> "Дополнительные параметры системы" -> "Переменные среды".
- В разделе "Системные переменные" найдите переменную PATH и нажмите "Изменить".
- Добавьте полный путь к папке ffmpeg (например, C:\путь\к\папке\ffmpeg) в качестве нового значения переменной PATH. Обратите внимание на то, что каждый путь разделяется точкой с запятой (;).
- Нажмите "ОК" для сохранения изменений.
## Установка FFFMPEG - Linux (Ubuntu/Debian):

Установите FFmpeg с помощью следующей команды: ```sudo apt-get install ffmpeg```
