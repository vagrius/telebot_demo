# Для корректной работы программы следует создать файл bot_config.py, в котором прописать значение переменных в виде
# token = 'значение'
# channel = 'имя_канала'

import telebot
import requests
from bs4 import BeautifulSoup as bs
from bot_config import token_value
from bot_config import channel_name


TOKEN = token_value  # Токен нашего бота
CHANNEL_NAME = channel_name  # Имя канала, куда будем отправлять новости
bot = telebot.TeleBot(TOKEN)

# Получаем нужную страницу и парсим на предмет последней новости
request = requests.get('https://vc.ru')
soup = bs(request.text, features="html.parser")
source = soup.find('a', class_='news_item__title')
news_header = source.text
news_link = source.get('href')
news_text = f'{news_header.strip()}\n{news_link.strip()}'

# Отправляем новость в канал
bot.send_message(CHANNEL_NAME, news_text)
