import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from bs4 import BeautifulSoup as BS

API_TOKEN = '7786275569:AAH6f4wT1BXmfqNj6yd5A7dNkVmOp9ohuXg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start komandasi uchun handler
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"Salom {message.from_user.first_name}. Bu yerdan Shahar yoki Viloyat nomini tanlang 👇",
                         reply_markup=main_keyboard())
# back() funksiyasi
def back():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Orqaga", callback_data='back1')]
    ])

# Toshkent shahri ob-havo ma'lumotlari
toshkent = requests.get('https://sinoptik.ua/погода-ташкент')
html_t = BS(toshkent.content, 'html.parser')
for tosh in html_t.select('#content'):
    min_temp = tosh.select('.temperature .min')[0].text
    max_temp = tosh.select('.temperature .max')[0].text
    t_min = min_temp[4:]
    t_max = max_temp[5:]
    temperature1 = tosh.find('p', class_='today-temp').get_text()

# Samarqand shahri ob-havo ma'lumotlari
samarkand = requests.get('https://sinoptik.ua/погода-самарканд')
html_s = BS(samarkand.content, 'html.parser')
for sam in html_s.select('#content'):
    min_s = sam.select('.temperature .min')[0].text
    max_s = sam.select('.temperature .max')[0].text
    s_min = min_s[4:]
    s_max = max_s[5:]
    temperature2 = sam.find('p', class_='today-temp').get_text()
# Navoiy shahri ob-havo ma'lumotlari
navoi_y = requests.get('https://sinoptik.ua/погода-навои')
html_n = BS(navoi_y.content, 'html.parser')
for nav in html_n.select("#content"):
    min_n = nav.select('.temperature .min')[0].text
    max_n = nav.select('.temperature .max')[0].text
    n_min = min_n[4:]
    n_max = max_n[5:]
    temperature3 = nav.find('p', class_='today-temp').get_text()
# Buxoro shahri ob-havo ma'lumotlari
buxor_o = requests.get('https://sinoptik.ua/погода-бухара')
html_b = BS(buxor_o.content, 'html.parser')
for bux in html_b.select('#content'):
    min_b = bux.select('.temperature .min')[0].text
    max_b = bux.select('.temperature .max')[0].text
    b_min = min_b[4:]
    b_max = max_b[5:]
    temperature4 = bux.find('p', class_='today-temp').get_text()
# Andijon viloyati ob-havo ma'lumotlari
andijo_n = requests.get('https://sinoptik.ua/погода-андижан')
html_a = BS(andijo_n.content, 'html.parser')
for an in html_a.select('#content'):
    min_a = an.select('.temperature .min')[0].text
    max_a = an.select('.temperature .max')[0].text
    a_min = min_a[4:]
    a_max = max_a[4:]
    temperature5 = an.find('p', class_='today-temp').get_text()
# Farg'ona viloyati ob-havo ma'lumotlari
fargon_a = requests.get('https://sinoptik.ua/погода-фергана')
html_f = BS(fargon_a.content, 'html.parser')
for far in html_f.select('#content'):
    min_f = far.select('.temperature .min')[0].text
    max_f = far.select('.temperature .max')[0].text
    f_min = min_f[4:]
    f_max = max_f[5:]
    temperature6 = far.find('p', class_='today-temp').get_text()
# Namangan viloyati ob-havo ma'lumotlari
namanga_n = requests.get('https://sinoptik.ua/погода-наманган')
html_nam = BS(namanga_n.content, 'html.parser')
for nam in html_nam.select('#content'):
    min_nam = nam.select('.temperature .min')[0].text
    max_nam = nam.select('.temperature .max')[0].text
    nam_min = min_nam[4:]
    nam_max = max_nam[5:]
    temperature7 = nam.find('p', class_='today-temp').get_text()
# Xorazm viloyati ob-havo ma'lumotlari
xoraz_m = requests.get('https://sinoptik.ua/погода-ургенч')
html_xor = BS(xoraz_m.content, 'html.parser')
for xor in html_xor.select('#content'):
    min_xor = xor.select('.temperature .min')[0].text
    max_xor = xor.select('.temperature .max')[0].text
    xor_min = min_xor[4:]
    xor_max = max_xor[5:]
    temperature8 = xor.find('p', class_='today-temp').get_text()
# Jizzax viloyati ob-havo ma'lumotlari
jizza_x = requests.get('https://sinoptik.ua/погода-джизак')
html_jiz = BS(jizza_x.content, 'html.parser')
for jiz in html_jiz.select('#content'):
    min_jiz = jiz.select('.temperature .min')[0].text
    max_jiz = jiz.select('.temperature .max')[0].text
    jiz_min = min_jiz[4:]
    jiz_max = max_jiz[5:]
    temperature9 = jiz.find('p', class_='today-temp').get_text()
# Sirdaryo viloyati ob-havo ma'lumotlari
sirdary_o = requests.get('https://sinoptik.ua/погода-сырдарья')
html_sir = BS(sirdary_o.content, 'html.parser')
for sir in html_sir.select('#content'):
    min_sir = sir.select('.temperature .min')[0].text
    max_sir = sir.select('.temperature .max')[0].text
    sir_min = min_sir[4:]
    sir_max = max_sir[5:]
    temperature10 = sir.find('p', class_='today-temp').get_text()


# Callback query handler
@dp.callback_query_handler()
async def process_callback(query: types.CallbackQuery):

    data = query.data

    if data == "01":
        await query.message.edit_text(f"Bugun Toshkent shaxrida havo o`zgarib turadi\nmin {t_min}\nmax "
                                f"{t_max} \nbo`lishi kutilmoqda ⛅\nHozirgi temperatura {temperature1}", reply_markup=back())
    elif data == "02":
        await query.message.edit_text(f"Bugun Samarqand shahrida havo o'zgarib turadi\nmin {s_min}\nmax "
                                f"{s_max} \nbo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature2}", reply_markup=back())
    elif data == "03":
        await query.message.edit_text(f"Bugun Navoiy viloyatida havo o'zgarib turadi\nmin {n_min} "
                                f"Max {n_max} bo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature3}", reply_markup=back())
    elif data == "04":
        await query.message.edit_text(f"Bugun Buxoro viloyatida havo o'zgarib turadi\nmin {n_min} "
                                f"Max {n_max} bo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature4}", reply_markup=back())
    elif data == "05":
        await query.message.edit_text(f"Bugun Andijon viloyatida havo o'zgarib turadi\nmin {a_min} "
                                f"Max {a_max} bo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature5}", reply_markup=back())
    elif data == "06":
        await query.message.edit_text(f"Bugun Farg'ona viloyatida havo o'zgarib turadi\nmin {f_min} "
                                f"Max {f_max} bo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature6}", reply_markup=back())
    elif data == "07":
        await query.message.edit_text(f"Bugun Namangan viloyatida havo o'zgarib turadi\nmin {nam_min} "
                                f"Max {nam_max} bo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature7}", reply_markup=back())
    elif data == "08":
        await query.message.edit_text(f"Bugun Xorazm viloyatida havo o'zgarib turadi\nmin {xor_min} "
                                f"Max {xor_max} bo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature8}", reply_markup=back())
    elif data == "09":
        await query.message.edit_text(f"Bugun Jizzax viloyatida havo o'zgarib turadi\nmin {jiz_min} "
                                f"Max {xor_max} bo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature9}", reply_markup=back())
    elif data == "10":
        await query.message.edit_text(f"Bugun Sirdaryo viloyatida havo o'zgarib turadi\nmin {sir_min} "
                                f"Max {sir_max} bo'lishi kutilmoqda ⛅\nHozirgi temperatura {temperature10}", reply_markup=back())
    elif data == "11":
        await query.message.edit_text("Surxandaryo: Havo ma'lumotlari mavjud emas ⛅", reply_markup=back())
    elif data == "back1":
        await query.message.edit_text("Bu yerdan shahar yoki viloyatni tanlang:", reply_markup=main_keyboard())

# Asosiy keyboard
def main_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Toshkent", callback_data='01')],
        [InlineKeyboardButton("Samarqand", callback_data='02')],
        [InlineKeyboardButton("Navoiy", callback_data='03')],
        [InlineKeyboardButton("Buxoro", callback_data='04')],
        [InlineKeyboardButton("Andijon", callback_data='05')],
        [InlineKeyboardButton("Farg'ona", callback_data='06')],
        [InlineKeyboardButton("Namangan", callback_data='07')],
        [InlineKeyboardButton("Xorazm", callback_data='08')],
        [InlineKeyboardButton("Jizzax", callback_data='09')],
        [InlineKeyboardButton("Sirdaryo", callback_data='10')],
        [InlineKeyboardButton("Surxandaryo", callback_data='11')]
    ])
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
