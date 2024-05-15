import os
from dotenv import load_dotenv
import sounddevice as sd
from scipy.io.wavfile import write
import telebot

load_dotenv()

token = os.getenv("BOT_TOCKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

def record_audio(duration):
    fs = 44100  # Частота дискретизации
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    write('output.wav', fs, recording)

def send_audio_to_telegram():
    bot = telebot.TeleBot(token)
    audio = open('output.wav', 'rb')
    bot.send_audio(chat_id, audio)
    audio.close()

while True:
    record_audio(10)
    send_audio_to_telegram()
