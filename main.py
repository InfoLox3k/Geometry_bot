# import telebot
# from telebot import types
from functions import *

# Указываем токен (не забудьте заменить на ваш токен)
  # Замените на ваш токен
keyboard_massive = []
final_text = ''
new_text = ''

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global final_text
    global keyboard_massive

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, сейчас я покажу тебе мой каталог.")

        keyboard_massive = [['ТРЕУГОЛЬНИК', 'Triangle'],
                            ['ПРЯМОУГОЛЬНИК И КВАДРАТ', 'Geometry'],
                            ['ОКРУЖНОСТЬ И КРУГ', 'Circle'],
                            ['ПРЯМАЯ', 'Straight'],
                            ['УГОЛ', 'Corner']]

        print(message.chat.id)

        list_clear(message)

        final_text = 'Выбери нужную фигуру:'

        inline_keyboard(keyboard_massive, final_text, message.from_user.id, "only start")

    # if message.text == "/botwrite":
    #     text_of_id = input("Тут: ")
    #     bot.send_message(949303033, text=text_of_id)

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    # else:
    #     bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    bot.answer_callback_query(call.id)

    chat_id = call.message.chat.id

    if call.data == "Geometry":
        msg = "Сейчас я покажу, что я знаю о прямоугольнике и квадрате."

        keyboard_massive = [['ПРЯМОУГОЛЬНИК', 'Rectangle'],
                            ['КВАДРАТ', 'Square']]

        final_text = "Выбери нужную фигуру:"

        inline_keyboard(keyboard_massive, final_text, call.message.chat.id ,msg)

    elif call.data == "Rectangle":
        new_text = """*Признаки прямоугольника:*
    *1.* Если у выпуклого четырехугольника все углы прямые, то он является прямоугольником.
    *2.* Если у параллелограмма диагонали равны, то он является прямоугольником.
*Свойство прямоугольника:*
    Диагонали прямоугольника равны.
    """
        message_layer(call, new_text, "Rectangle")

    elif call.data == "Square":
        new_text = """*Свойства квадрата:*
    *1.* Все стороны равны.
    *2.* Все углы прямые.
    *3.* Диагонали точкой пересечения делятся пополам.
    *4.* Диагонали равны.
    *5.* Диагонали взаимно перпендикулярны.
    *6.* Диагонали делят углы квадрата пополам.
    *7.* Диагональ квадрата со стороной a равна *a√2*.
    """

        message_layer(call, new_text, "Rectangle")

    elif call.data == 'Circle':
        msg = "Сейчас я покажу, что я знаю о окружностях и кругах."

        keyboard_massive = [['ОКРУЖНОСТЬ', 'Circle Kr'],
                            ['КРУГ', 'Circle OK']]
        inline_keyboard(keyboard_massive, "Выбери окружность или круг:", call.message.chat.id, msg)

    elif call.data == "Circle Kr":
        new_text = """*1.* Круг — это фигура с наибольшей площадью при заданной длине периметра
*2.* Окружность и радиус круга пропорциональны.
*3.* Заключенная в нем площадь и квадрат его радиуса пропорциональны.
*4.* Константы пропорциональности равны 2π и π соответственно.
"""
        message_layer(call, new_text, "Circle")

    elif call.data == "Circle OK":
        new_text = """*1.* Теорема о пересечении хорд гласит, что если два хорда CD и EB пересекаются в точке A, то AC × AD = AB × AE.
*2.* Если две секущие AE и AD также пересекают окружность в точках B и C соответственно, то AC × AD = AB × AE (следствие из теоремы о длине хорды).
*3.* Угол между хордой и касательной в одной из её конечных точек равен половине угла, образованного в центре окружности, на противоположной стороне хорды (угол между касательной и хордой).
"""
        message_layer(call, new_text, "Circle")
        
    elif call.data == "Straight":
        msg = "Сейчас я покажу, что я знаю о прямых."

        keyboard_massive = [['ПАРАЛЕЛЬНЫЕ', 'Straight Pa'],
                            ['ПЕРЕПЕНДЕКУЛЯРНЫЕ', 'Straight Pe']]
        final_text = "Выбери тип прямой:"

        inline_keyboard(keyboard_massive, final_text, call.message.chat.id, msg)

    elif call.data == "Straight Pa":
        new_text = """*1*. Через любую точку, не лежащую на прямой, можно провести прямую, параллельную данной, и притом только одну.
        *2.* Если прямая пересекает одну из параллельных прямых, то она пересекает и другую.
            """
        message_layer(call, new_text, "Straight")
    elif call.data == "Straight Pe":
        new_text = """*1.* Две прямые на плоскости называются перпендикулярными, если при пересечении они образуют 4 прямых угла.
        *2.* Две прямые в пространстве перпендикулярны друг другу, если они соответственно параллельны некоторым двум другим взаимно перпендикулярным прямым, лежащим в одной плоскости.
            """
        message_layer(call, new_text, "Straight")

    elif call.data == "Corner":
        msg = "Сейчас я покажу, что я знаю о углах."

        keyboard_massive = [['ВЕРТЕКАЛЬНЫЕ УГЛЫ', 'Corner Ve'],
                            ['СМЕЖНЫЕ УГЛЫ', 'Corner Sm'],
                            ['ДВЕ ПРЯМЫЕ И СЕКУЩАЯ', 'Corner Pe']]

        final_text = "Выбери тип угла:"

        inline_keyboard(keyboard_massive, final_text, call.message.chat.id, msg)

    elif call.data == "Corner Ve":
        new_text = "Вертикальные углы всегда равны друг другу."
        message_layer(call, new_text, "Corner")

    elif call.data == "Corner Sm":
        new_text = "Сумма смежных углов равна 180 градусов"
        message_layer(call, new_text, "Corner")

    elif call.data == "Corner Pe":
        bot.send_message(call.message.chat.id, "Это информация о пересечения двух прямых секущей...")

        msg = "Сейчас я покажу, что я знаю о пересечении двух прямых секущей."

        keyboard_massive = [['Соответственные углы', 'Corner So'],
                            ['накрест лежащие углы', 'Corner Na'],
                            ['Односторонние углы', 'Corner Od']]

        inline_keyboard(keyboard_massive, "Выбери тип угла:", call.message.chat.id, msg)

    elif call.data == "Corner So":
        new_text = "Если две параллельные прямые пересечены секущей, то соответственные углы равны."
        message_layer(call, new_text, "Corner PE")
    elif call.data == "Corner Na":
        new_text = "Если две параллельные прямые пересечены секущей, то накрест лежащие углы равны."
        message_layer(call, new_text, "Corner PE")
    elif call.data == "Corner Od":
        new_text = "Если две параллельные прямые пересечены секущей, то сумма односторонних углов равна 180 градусов."
        message_layer(call, new_text, "Corner PE")




    elif call.data == "Triangle":
        msg = "Сейчас я покажу, что я знаю о треугольниках."

        text_and_data_list = [['ПРЯМОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', 'Triangle PR'],
                              ['ОСТРОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', 'Triangle OS'],
                              ['ТУПОУГОЛЬНЫЙ ТРЕУГОЛЬНИК', 'Triangle TY']]

        final_text = "Выбери тип треугольника:"

        inline_keyboard(text_and_data_list, final_text, call.message.chat.id, msg)


    elif call.data == "Triangle PR":
        keyboard_massive = [['БИССИКТРИСА', 'Triangle PrB'],
                            ['МЕДИАНА', 'Triangle PrM'],
                            ['ВЫСОТА', 'Triangle PrV'],
                            ['ПРИЗНАКИ РАВЕНСТВА', 'Triangle PrR'],
                            ['РАВНОБЕДРЕННОСТЬ', 'Triangle PrRB']]
        final_text = "Выбери что ты хочешь узнать о прямоугольном треугольнике:"

        inline_keyboard(keyboard_massive, final_text, call.message.chat.id, "")

    elif call.data == "Triangle PrB":
        new_text = "Биссектриса в прямоугольном треугольнике делит угол на два равных"
        message_layer(call, new_text, "Triangle PR")

    elif call.data == "Triangle PrM":
        new_text = "Медиана проведенная к гипотенузе равна ее половине"
        message_layer(call, new_text, "Triangle PR")
    elif call.data == "Triangle PrV":
        new_text = """*1.* Высота, опущенная на гипотенузу, является средним геометрическим (средним пропорциональным) двух отрезков гипотенузы.
*2.* Каждая сторона треугольника является средним пропорциональным между гипотенузой и отрезком гипотенузы, примыкающим к стороне.
        """
        message_layer(call, new_text, "Triangle PR")
    elif call.data == "Triangle PrR":
        new_text = """*1.* Если два катета одного прямоугольного треугольника соответственно равны двум катетам другого прямоугольного треугольника, то такие треугольники равны.
*2.* Если катет и прилежащий к нему острый угол одного прямоугольного треугольника соответственно равны катету и прилежащему острому углу другого прямоугольного треугольника, то такие треугольники равны.
*3.* Если гипотенуза и прилежащий к ней угол одного прямоугольного треугольника соответственно равны гипотенузе и прилежащему углу другого треугольника, то такие треугольники равны.
*4.* Если катет и гипотенуза одного треугольника соответственно равны катету и гипотенузе другого треугольника, такие прямоугольные треугольники равны.
        """
        message_layer(call, new_text, "Triangle PR")
    elif call.data == "Triangle PrRB":
        new_text = "Биссектриса, медиана, высота и серединный перпендикуляр, проведённые к основанию, совпадают между собой. "
        message_layer(call, new_text, "Triangle PR")



    elif call.data == "Triangle OS":
        msg = "Сейчас я покажу, что я знаю о прямоугольных треугольных."

        keyboard_massive = [['БИССИКТРИСА', 'Triangle OSB'],
                            ['МЕДИАНА', 'Triangle OSM'],
                            ['ВЫСОТА', 'Triangle OSV'],
                            ['ПРИЗНАКИ РАВЕНСТВА', 'Triangle OSR'],
                            ['РАВНОБЕДРЕННОСТЬ', 'Triangle OSRB'],
                            ['РАВНОСТОРОННОСТЬ', 'Triangle OSRS']
                            ]
        final_text = "Выбери что ты хочешь узнать о остроугоьном  треугольнике:"
        inline_keyboard(keyboard_massive, final_text, call.message.chat.id, msg)

    elif call.data == "Triangle OSB":
        new_text = "Биссиктрисса делит угол на два равных"
        message_layer(call, new_text, "Triangle OS")
    elif call.data == "Triangle OSM":
        new_text = "Медиана делит сторону пополам"
        message_layer(call, new_text, "Triangle OS")
    elif call.data == "Triangle OSV":
        new_text = "Высота образует прямой угол"
        message_layer(call, new_text, "Triangle OS")
    elif call.data == "Triangle OSR":
        new_text = """1. Если две стороны и угол между ними одного треугольника равны соответственно двум сторонам и углу между ними другого треугольника, то такие треугольники равны.
2. Если сторона и прилежащие к ней углы одного треугольника равны соответственно стороне и прилежащим к ней углам другого треугольника, то такие треугольники равны.
3. Если три стороны одного треугольника равны трём сторонам другого треугольника, то такие треугольники равны.
        """
        message_layer(call, new_text, "Triangle OS")

    elif call.data == "Triangle OSRB":
        new_text = "Биссектриса, медиана, высота и серединный перпендикуляр, проведённые к основанию, совпадают между собой. "
        message_layer(call, new_text, "Triangle OS")
    elif call.data == "Triangle OSRS":
        new_text = """1. В равностороннем треугольнике все стороны равны.
2. В равностороннем треугольнике все углы равны 60 градусов.
        """
        message_layer(call, new_text, "Triangle OS")


    elif call.data == "Triangle TY":
        msg = "Сейчас я покажу, что я знаю о тупогольных треугольных."

        keyboard_massive = [['БИССИКТРИСА', 'Triangle TYB'],
                            ['МЕДИАНА', 'Triangle TYM'],
                            ['ВЫСОТА', 'Triangle TYV'],
                            ['ПРИЗНАКИ РАВЕНСТВА', 'Triangle TYR'],
                            ['РАВНОБЕДРЕННОСТЬ', 'Triangle TYRB']
                            ]
        final_text = "Выбери что ты хочешь узнать о тупоугоьном  треугольнике:"
        inline_keyboard(keyboard_massive, final_text, call.message.chat.id, msg)

    elif call.data == "Triangle TYB":
        new_text = "Биссектрисса делит угол на два равных"
        message_layer(call, new_text, "Triangle TY")
    elif call.data == "Triangle TYM":
        new_text = "Медиана делит сторону пополам"
        message_layer(call, new_text, "Triangle TY")
    elif call.data == "Triangle TYV":
        new_text = "Высота в прямоугольном треугольнике проводится на продолжение стороны"
        message_layer(call, new_text, "Triangle TY")
    elif call.data == "Triangle TYR":
        new_text = """1. Если две стороны и угол между ними одного треугольника равны соответственно двум сторонам и углу между ними другого треугольника, то такие треугольники равны.
2. Если сторона и прилежащие к ней углы одного треугольника равны соответственно стороне и прилежащим к ней углам другого треугольника, то такие треугольники равны.
3. Если три стороны одного треугольника равны трём сторонам другого треугольника, то такие треугольники равны."""
        message_layer(call, new_text, "Triangle TY")

    elif call.data == "Triangle TYRB":
        new_text = "Биссектриса, медиана, высота и серединный перпендикуляр, проведённые к основанию, совпадают между собой."
        message_layer(call, new_text, "Triangle TY")

        # Запускаем бота

bot.polling(none_stop=True)