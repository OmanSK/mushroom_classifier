from aiogram import Bot, executor, Dispatcher, types
from io import BytesIO
from PIL import Image
import requests
from model import prediction as PRED
from config import TOKEN_API, ONNX

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

URL_IMAGE = f'https://api.telegram.org/bot{TOKEN_API}/getFile?file_id='
URL = f'https://api.telegram.org/file/bot{TOKEN_API}/'

HELP_MESSAGE = """
    Желательно, чтобы гриб располагался по центру.
    В боте представлены только те грибы, что растут на территории Брянской области:
    Бледная поганка
    Боровик
    Волнушка розовая
    Груздь
    Дождевик
    Лиловка лиловоногая
    Лисичка
    Ложнодождевик
    Ложноопенок серно-желтый
    Моховик зеленый
    Мухомор красный
    Опенок осенний
    Подберезовик
    Подосиновик
    Польский гриб
    Рядовка тигровая
    Сатанинискй гриб
    Сморчок
    Шампиньон желтокожий
"""

@dp.message_handler(commands=['start'])
async def start_message(msg: types.Message):
    await msg.answer('Выбери фото для классификации\nБот определяет только те грибы, которые указаны в //help')

@dp.message_handler(commands=['help'])
async def help_message(msg: types.Message):
    await msg.answer(HELP_MESSAGE)

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def process_photo(msg: types.Message):
    print(msg.photo)
    file = msg.photo[-1].file_id
    resp = requests.get(URL_IMAGE + str(file))
    image_path = resp.json()['result']['file_path']
    img = requests.get(URL + image_path)
    img = Image.open(BytesIO(img.content)).convert('RGB')
    
    result = PRED(img)
    answer = ''
    for k, v in result.items():
        answer += k.capitalize() + ': ' + v + '\n'
    
    await msg.reply(text=answer)
    
if __name__=='__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
