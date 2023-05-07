#mAlc_Jke \ vya4es.ru/projects/txt-to-speech-mic

from time import sleep
from pydub import AudioSegment
import pygame
import pyttsx3

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

def main():
    while True:
        text = input("Введите текст для преобразования в речь (или 'выход' для завершения): ")
        if text.lower() == 'выход':
            break

        text_to_speech(text)

        # Воспроизведение сохраненной речи через виртуальный микрофон
        play('temp.wav', "CABLE Input (VB-Audio Virtual Cable)")

if __name__ == '__main__':
    main()