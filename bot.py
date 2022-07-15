import telebot
from telebot import types # для указание типов

bot = telebot.TeleBot('5292026757:AAEc0IJbUeFIYX0G6QXgvPk7OV3IyVgesDA')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1 = types.KeyboardButton("БУЛОЧНИК/ЗАГОТОВЩИК")
    btn2 = types.KeyboardButton("СБОРЩИК/ГРИЛЬЩИК")
    btn3 = types.KeyboardButton("КАССИР/ВЫДАЧА")
    btn4 = types.KeyboardButton("МЕНЕДЖЕР РЕСТОРАНА")
    btn5 = types.KeyboardButton("ДИРЕКТОР РЕСТОРАНА")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, 'Добро пожаловать в компанию Франклинс Бургер, ' + message.from_user.first_name)
    bot.send_message(message.chat.id, 'Выберите выкансию, которая вас интересует?', reply_markup=markup )    

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "БУЛОЧНИК/ЗАГОТОВЩИК"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да-БУЛОЧНИК")
        btn2 = types.KeyboardButton("Нет")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text='Набор на данную должность не ведется, посмотрите другие вакансии.', parse_mode='MARKDOWN',reply_markup=markup )

    elif message.text == 'СБОРЩИК/ГРИЛЬЩИК':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да-СБОРЩИК")
        btn2 = types.KeyboardButton("Нет")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text='*СБОРЩИК/ГРИЛЬЩИК*\n*ЗП:* 160 - 180р/час;\n*График работы:* 5/2, 6/1, работы в выходные дни (ПТ-ВС);\n*Что нужно делать?*\nа) Собирать бургеры и роллы по стандартам компании;\nб) Готовить мясную продукцию (говядина, свинина, курица);\nв) Убирать свое рабочее место;\nг) Помогать в обучении новых сотрудников;\nд) Помогать менеджеру/директору ресторана в разгрузке поставки;\nе) Маркировать всю пищевую продукцию в ресторане\n*Что мы ждем от кандидата?*\nа) Понимать и хорошо говорить по – русски;\nб) Носить униформу;\nв) Выполнять поручения менеджера и директора ресторана;\nг) Проходить обучение в тренинг – ресторане;\n*Что мы предоставляем сотруднику:*\nа) Бесплатное горячее питание;\nб) Стабильная заработная плата 2 раза в месяц;\nв) Стильная униформа; ', parse_mode='MARKDOWN')
        bot.send_message(message.chat.id, text="Вас заинтересовало наше предложение?",reply_markup=markup)

    elif message.text == 'КАССИР/ВЫДАЧА':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да-КАССИР")
        btn2 = types.KeyboardButton("Нет")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="*КАССИР/ВЫДАЧА*\n*ЗП:* 170-195р/час;\n*График работы:* 5/2, 6/1,\nработы в выходные дни (ПТ-ВС); *Что нужно делать?*\nа) Обслуживать гостей по стандартам компании;\nб) Знать и применять на практике способы повышения продаж;\nв) Убирать свое рабочее место;\nг) Помогать в обучении новых сотрудников\n*Что мы ждем от кандидата?*\nа) Понимать и грамотно говорить по – русски;/nб) Носить униформу;/nв) Выполнять поручения менеджера и директора ресторана;\nг) Проходить обучение в тренинг – ресторане;\n*Что мы предоставляем сотруднику:*\nа) Бесплатное горячее питание;\nб) Стабильная заработная плата 2 раза в месяц;\nв) Стильная униформа;", parse_mode='MARKDOWN') 
        bot.send_message(message.chat.id, text="Вас заинтересовало наше предложение?",reply_markup=markup)

    elif message.text == 'МЕНЕДЖЕР РЕСТОРАНА':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да-Менеджер")
        btn2 = types.KeyboardButton("Нет")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text='*МЕНЕДЖЕР РЕСТОРАНА*\n*ЗП:* от 240 р/ч\n*График работы:* 5/2, 2/2.\n*Что нужно делать?*\nа) Обеспечивать бесперебойное ведение смены в течение дня: открытие/закрытие, обходы в течение дня;\nб) заказ продукции;\nв) Прием поставок;\nг) Ведение первичной документации и регулярная отправка отчетов;\nд) Обучение и адаптация новых сотрудников;\nе) Проведение собеседований;\n*Что мы ждем от кандидата?*\nа) Грамотная устная и письменная речь; \nв) Умение работать в режиме многозадачности;\nг) Желание развиваться и не бояться ответственности;\nе) Опыт работы в сетевых ресторанах от 0,5 года;\nж) Умение планировать и расставлять приоритеты в работе;\nз) Умение работать с программами Microsoft Office (уровень «Уверенный пользователь»);\nи) Умение работать в программе IIKO будет преимуществом.\nЧто мы предоставляем сотруднику:\nа) Бесплатное горячее питание;\nб) Стабильная заработная плата 2 раза в месяц;\nв) Стильная униформа;\nг) Корпоративное обучение;\nд) Официальное оформление по ТК РФ. ', parse_mode='MARKDOWN')
        bot.send_message(message.chat.id, text="Вас заинтересовало наше предложение?",reply_markup=markup)


    elif message.text == 'ДИРЕКТОР РЕСТОРАНА':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да-Директор")
        btn2 = types.KeyboardButton("Нет")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text='*МЕНЕДЖЕР РЕСТОРАНА*\n*ЗП:* от 240 р/ч\n*График работы:* 5/2, 2/2.\n*Что нужно делать?*\nа) Обеспечивать бесперебойное ведение смены в течение дня: открытие/закрытие, обходы в течение дня;\nб) заказ продукции;\nв) Прием поставок;\nг) Ведение первичной документации и регулярная отправка отчетов;\nд) Обучение и адаптация новых сотрудников;\nе) Проведение собеседований;\n*Что мы ждем от кандидата?*\nа) Грамотная устная и письменная речь; \nв) Умение работать в режиме многозадачности;\nг) Желание развиваться и не бояться ответственности;\nе) Опыт работы в сетевых ресторанах от 0,5 года;\nж) Умение планировать и расставлять приоритеты в работе;\nз) Умение работать с программами Microsoft Office (уровень «Уверенный пользователь»);\nи) Умение работать в программе IIKO будет преимуществом.\nЧто мы предоставляем сотруднику:\nа) Бесплатное горячее питание;\nб) Стабильная заработная плата 2 раза в месяц;\nв) Стильная униформа;\nг) Корпоративное обучение;\nд) Официальное оформление по ТК РФ. ', parse_mode='MARKDOWN')
        bot.send_message(message.chat.id, text="Вас заинтересовало наше предложение?",reply_markup=markup)    

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("БУЛОЧНИК/ЗАГОТОВЩИК")
        btn2 = types.KeyboardButton("СБОРЩИК/ГРИЛЬЩИК")
        btn3 = types.KeyboardButton("КАССИР/ВЫДАЧА")
        btn4 = types.KeyboardButton("МЕНЕДЖЕР РЕСТОРАНА")
        btn5 = types.KeyboardButton("ДИРЕКТОР РЕСТОРАНА")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif(message.text == "Да-БУЛОЧНИК"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("ТРЦ Красный Кит")
        btn2 = types.KeyboardButton("Не подходит ни один вариант")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="В нашей компании открыты вакансии в следующих ТЦ:", reply_markup=markup)

    elif(message.text == "Да-СБОРЩИК"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("ТРЦ Небо")
        btn2 = types.KeyboardButton("Не подходит ни один вариант")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="В нашей компании открыты вакансии в следующих ТЦ:", reply_markup=markup)    

    elif(message.text == "Да-КАССИР"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("ТРЦ Город Лефортово")
        btn2 = types.KeyboardButton("ТРЦ Гагаринский")
        btn3 = types.KeyboardButton("ТРЦ Охотный Ряд")
        btn4 = types.KeyboardButton("ТРЦ Ривьера")
        btn5 = types.KeyboardButton("Не подходит ни один вариант")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="В нашей компании открыты вакансии в следующих ТЦ:", reply_markup=markup)

    elif(message.text == "Да-Менеджер"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("ТРЦ Атриум")
        btn2 = types.KeyboardButton("ТРЦ Афимолл")
        btn3 = types.KeyboardButton("ТРЦ Вегас")
        btn4 = types.KeyboardButton("ТРЦ Калейдоскоп")
        btn5 = types.KeyboardButton("ТРЦ Зеленопарк")
        btn6 = types.KeyboardButton("ТРЦ Красный Кит")
        btn7 = types.KeyboardButton("ТРЦ Ривьера")
        btn8 = types.KeyboardButton("Не подходит ни один вариант")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id, text="В нашей компании открыты вакансии в следующих ТЦ:", reply_markup=markup)

    elif(message.text == "Да-Директор"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("ТРЦ Атриум")
        btn2 = types.KeyboardButton("Не подходит ни один вариант")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="В нашей компании открыты вакансии в следующих ТЦ:", reply_markup=markup)                    

    elif(message.text == "ТРЦ Атриум"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n \n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')

    elif(message.text == "ТРЦ Охотный Ряд"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n \n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')

    elif(message.text == "ТРЦ Афимолл"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n \n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')

    elif(message.text == "ТРЦ Ривьера"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n\n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN') 
    
    elif(message.text == "ТРЦ Зеленопарк"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n\n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')     

    elif(message.text == "ТРЦ Красный Кит"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n \n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')

    elif(message.text == "ТРЦ Авиапарк"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n \n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')


    elif(message.text == "ТРЦ Небо"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n \n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')            

    elif(message.text == "ТРЦ Вегас"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n \n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')                                

    elif(message.text == "ТРЦ Калейдоскоп"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n \n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')                                


    elif(message.text == "Не подходит ни один вариант"):
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Заполни форму кандидата", url='https://forms.gle/oziyg1UFRHySSrBs9')
        markup.add(button1)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("да")
        btn2 = types.KeyboardButton("Нет")
        markup2.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Оставь свои контактные данные по ссылке, мы с тобой свяжемся", reply_markup=markup)
        bot.send_message(message.chat.id, text="Также вы можете позвонить/написать в WhatsApp или Телеграмм\n По следующим номерам:\n\n 8(800)600-87-51 (WhatsApp)\n Telegram: \n@FranklinsHRbot", parse_mode='MARKDOWN')
        bot.send_message(message.chat.id, text="Посмотреть другие вакансии?", reply_markup=markup2)

    elif(message.text == "да"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton("БУЛОЧНИК/ЗАГОТОВЩИК")
        btn2 = types.KeyboardButton("СБОРЩИК/ГРИЛЬЩИК")
        btn3 = types.KeyboardButton("КАССИР/ВЫДАЧА")
        btn4 = types.KeyboardButton("МЕНЕДЖЕР РЕСТОРАНА")
        btn5 = types.KeyboardButton("ДИРЕКТОР РЕСТОРАНА")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
                                              

    elif(message.text == "Нет"):
        bot.send_message(message.chat.id, text="Спасибо, что заинтересовался нашей вакансией")

    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True, interval=0)