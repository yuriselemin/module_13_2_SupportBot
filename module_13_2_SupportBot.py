from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '7318149436:AAGsSUVCDgZhtmeaAEPHaoSxhZDaYpYoO_U'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())  # Added parentheses to initialize MemoryStorage



@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.' )


@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


