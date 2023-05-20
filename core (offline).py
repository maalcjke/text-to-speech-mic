#mAlc_Jke \ vya4es.ru/projects/txt-to-speech-mic

import pyttsx3
import pygame

from time import sleep
from pydub import AudioSegment
from pygame import mixer, _sdl2 as devices

def play(file_path: str, device: str):
    if device is None:
        devices = get_devices()
        if not devices:
            raise RuntimeError("No device!")
        device = devices[0]
    print("Play: {}\r\nDevice: {}".format(file_path, device))
    pygame.mixer.init(devicename=device)
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    duration = get_audio_duration(file_path)
    sleep(duration)
    pygame.mixer.quit()

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Установка скорости речи (по умолчанию: 200)
    engine.setProperty('volume', 0.8)  # Установка громкости речи (от 0 до 1)
    engine.save_to_file(text, 'temp.wav')  # Сохраняем речь в файл
    engine.runAndWait()

def get_audio_duration(file_path):
    audio = AudioSegment.from_file(file_path)
    duration_in_seconds = len(audio) / 1000  # Преобразование миллисекунд в секунды
    return duration_in_seconds

def get_audio_input_device():
    mixer.init()  # Инициализация mixer
    audio_devices = devices.audio.get_audio_device_names(False)  # Получение всех доступных аудио-входных устройств

    print("Доступные аудио-входные устройства:")
    for i, device in enumerate(audio_devices):
        print(f"{i+1}. {device}")

    while True:
        try:
            choice = int(input("Выберите номер аудио-входного устройства: "))
            if 1 <= choice <= len(audio_devices):
                break
            else:
                print(f"Пожалуйста, выберите номер от 1 до {len(audio_devices)}")
        except ValueError:
            print("Пожалуйста, введите корректный номер")

    selected_device = audio_devices[choice - 1]  # Выбор указанного устройства
    mixer.quit()  # Завершение работы mixer

    return selected_device

def main():

    selected_device = get_audio_input_device()

    while True:
        text = input("Введите текст для преобразования в речь (или 'выход' для завершения): ")
        if text.lower() == 'выход':
            break

        text_to_speech(text)

        # Воспроизведение сохраненной речи через виртуальный микрофон
        play('temp.wav', selected_device)

if __name__ == '__main__':
    main()
