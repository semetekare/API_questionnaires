import asyncio
import logging
import sys
import requests
import random

from aiogram import Bot, F, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.utils.deep_linking import decode_payload


class Registration(StatesGroup):
    answer = State()
    lastname = State()
    firstname = State()
    middlename = State()
    university = State()
    group = State()


TOKEN = '6830518143:AAG6cxJYJQTxkzXeNQvRpYfLfVZEcR4qwwo'
BOT_URL = 'https://t.me/hackaton_zone_test_bot'
SERVER_URL = 'http://localhost:8000'
router = Router()


@router.message(CommandStart(deep_link=True, deep_link_encoded=True))
async def test_args(msg: Message):
    text, *args = msg.text.split()
    try:
        test = decode_payload(args[0]).split("_")[0]
        if test == 'test':
            test_number = decode_payload(args[0]).split("_")[1]
            response = requests.get(f'{SERVER_URL}/test/{test_number}')
            print(response.json())
            test_info = response.json()

            questions_quantity = test_info['total_questions_quantity']
            questions = []

            response = requests.get(f'{SERVER_URL}/question/')
            amount: int = response.json()['count']
            print(f'amount = {amount}')

            for i in range(questions_quantity):
                rand_question = random.randint(1, amount)
                print(rand_question)
                response = requests.get(f'{SERVER_URL}/question/{rand_question}')
                question = response.json()['formulation']
                print(question)
                questions.append(question)

            text = (f"<b>Название:</b>\n{test_info['title']}\n<b>Описание:</b>\n{test_info['description']}\n"
                    f"<b>Время выполнения (в сек.):</b>\n{test_info['expires_in']}\n"
                    f"\n<b>Описание вопроса:</b>\n{questions[random.randint(0,len(questions))]}")
            print(text)

            await msg.answer(f"{text}")
        else:
            await msg.answer("Эта ссылка не подходит")
    except TypeError:
        print('Ошибочка...')


@router.message(CommandStart())
async def check_start(msg: Message, state: FSMContext):
    response = requests.get(f'{SERVER_URL}/checkStudent/{msg.from_user.username}')
    await state.set_state(Registration.answer)

    if response.status_code == 200:
        student = response.json()
        student_name = f'{student["first_name"]} {student["middle_name"]}'
        await msg.answer(f'Здравствуйте, {student_name}. Вы уже зарегистрированы в системе.')
    else:
        kb = ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Да"), KeyboardButton(text="Нет")]],
            resize_keyboard=True
        )
        await msg.answer(f'Здравствуйте, {msg.from_user.first_name}. Вы не зарегистрированы в системе. '
                         f'Желаете зарегистрироваться?',
                         reply_markup=kb)


@router.message(Registration.answer, F.text.casefold() == 'нет')
async def no_reg(msg: Message, state: FSMContext):
    await state.clear()

    await msg.answer(f'До свидания, {msg.from_user.first_name}.', reply_markup=ReplyKeyboardRemove())


@router.message(Registration.answer, F.text.casefold() == 'да')
async def yes_reg(msg: Message, state: FSMContext):
    await state.clear()
    await state.set_state(Registration.lastname)

    await msg.answer("Введите вашу фамилию:", reply_markup=ReplyKeyboardRemove())


@router.message(Registration.lastname)
async def reg(msg: Message, state: FSMContext):
    await state.update_data(lastname=msg.text)
    await state.set_state(Registration.firstname)

    await msg.answer("Введите ваше имя:", reply_markup=ReplyKeyboardRemove())


@router.message(Registration.firstname)
async def reg(msg: Message, state: FSMContext):
    await state.update_data(firstname=msg.text)
    await state.set_state(Registration.middlename)

    await msg.answer("Введите ваше отчество:", reply_markup=ReplyKeyboardRemove())


@router.message(Registration.middlename)
async def reg(msg: Message, state: FSMContext):
    await state.update_data(middlename=msg.text)
    await state.set_state(Registration.university)

    response = requests.get(f'{SERVER_URL}/university')
    university_list = []
    for univ in response.json()['results']:
        university_list.append(KeyboardButton(text=f'{univ["name"]}'))

    keyboard = ReplyKeyboardMarkup(
        keyboard=[university_list],
        resize_keyboard=True,
        input_field_placeholder="Выберите ваш ВУЗ..."
    )

    await msg.answer("Выберите ваш ВУЗ:", reply_markup=keyboard)


@router.message(Registration.university)
async def reg(msg: Message, state: FSMContext):
    response = requests.get(f'{SERVER_URL}/university')
    for univ in response.json()['results']:
        if univ['name'] == msg.text:
            await state.update_data(university=univ['id'])

    await state.set_state(Registration.group)
    await msg.answer("Введите вашу группу:", reply_markup=ReplyKeyboardRemove())


@router.message(Registration.group)
async def reg(msg: Message, state: FSMContext):
    data = await state.update_data(group=msg.text)
    await state.clear()
    tg_username = msg.from_user.username

    text = post_reg(firstname=data['firstname'],
                    lastname=data['lastname'],
                    middlename=data['middlename'],
                    university=data['university'],
                    group=data['group'],
                    tg_username=tg_username)

    await msg.answer(text=text)


def post_reg(firstname: str, lastname: str, middlename: str, university: str, group: str,
             tg_username: str) -> str:
    new_student = {
        "first_name": firstname,
        "last_name": lastname,
        "middle_name": middlename,
        "university": university,
        "group": group,
        "tg_username": tg_username,
    }

    response = requests.post(f'{SERVER_URL}/student/', json=new_student)

    if response.status_code == 201:
        return 'Вы успешно зарегистрировались!'
    else:
        return 'Ошибка при регистрации!'


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
