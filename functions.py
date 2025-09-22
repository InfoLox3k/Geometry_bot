import telebot
from telebot import types
from token_data import *

# False - state of existance of message, 0 - message id, 0 - chat id,

message_sended = [[[False, 0, 0],  # Rectangle
                    [False, 0, 0],  # Circle
                    [False, 0, 0],  # Corner
                    [False, 0, 0],  # Corner PE
                    [False, 0, 0],  # Straight
                    [False, 0, 0],  # Triangle
                    [False, 0, 0],  # Triangle PR
                    [False, 0, 0],  # Triangle OS
                    [False, 0, 0]  # Triangle TY
                  ]]

ids_list = [5278854769]

chat_info = 0


rect_states = message_sended[chat_info][0]

circle_states = message_sended[chat_info][1]

corner_states = message_sended[chat_info][2]
corner_pe_states = message_sended[chat_info][3]

straight_states = message_sended[chat_info][4]

triangle_states = message_sended[chat_info][5]
triangle_pr_states = message_sended[chat_info][6]
triangle_os_states = message_sended[chat_info][7]
triangle_ty_states = message_sended[chat_info][8]


list_it = {"Rectangle": rect_states,
           "Circle": circle_states,
           "Corner": corner_states,
           "Corner PE": corner_pe_states,
           "Straight": straight_states,
           "Triangle": triangle_states,
           "Triangle PR": triangle_pr_states,
           "Triangle OS": triangle_os_states,
           "Triangle TY": triangle_ty_states
           }


bot = telebot.TeleBot(general_token)


def inline_keyboard(text_and_data_list, end_text, call_chat_id, msg):
    keyboard = types.InlineKeyboardMarkup()

    buttons_list = []

    for i in range(len(text_and_data_list)):
        buttons_list.append(types.InlineKeyboardButton(text=text_and_data_list[i][0], callback_data=text_and_data_list[i][1]))

    keyboard.add(*buttons_list)

    if msg != "only start" and msg != "":
        bot.send_message(call_chat_id, msg)

    bot.send_message(call_chat_id, text=end_text, reply_markup=keyboard)

def list_clear(message):
    global message_sended, list_it, ids_list
    user_id = message.chat.id

    print(message_sended)
    print(ids_list)

    if user_id in ids_list:
        id_index = ids_list.index(user_id)
        del ids_list[id_index]
        del message_sended[id_index]

    corteg()

    print(message_sended)
    print(ids_list)

def corteg():
    global list_it
    list_it = {"Rectangle": rect_states,
               "Circle": circle_states,
               "Corner": corner_states,
               "Corner PE": corner_pe_states,
               "Straight": straight_states,
               "Triangle": triangle_states,
               "Triangle PR": triangle_pr_states,
               "Triangle OS": triangle_os_states,
               "Triangle TY": triangle_ty_states
               }

def message_layer(call, new_text, info_type):
    global message_sended, ids_list
    global chat_id

    chat_id = call.message.chat.id

    if chat_id in ids_list:
        chat_info = ids_list.index(chat_id)
    else:
        message_sended.append([[False, 0, 0],  # Rectangle
                               [False, 0, 0],  # Circle
                               [False, 0, 0],  # Corner
                               [False, 0, 0],  # Corner PE
                               [False, 0, 0],  # Straight
                               [False, 0, 0],  # Triangle
                               [False, 0, 0],  # Triangle PR
                               [False, 0, 0],  # Triangle OS
                               [False, 0, 0],  # Triangle TY
                              ])
        ids_list.append(chat_id)
        corteg()
        chat_info = ids_list.index(chat_id)

    print(f"chat_info: {chat_info}")
    print(f"info_type: {info_type}")
    print(f"chat_id_state: {chat_id in ids_list}")
    print(f"ids_list: {ids_list}")
    print(f"chat_states: {message_sended[chat_info]}")

    type_list = list_it[info_type]
    print(type_list)

    if type_list[0] == False and type_list[1] == 0:
        bot_message = bot.send_message(call.message.chat.id, text=new_text, parse_mode="Markdown")
        type_list[0] = True
        type_list[1] = bot_message.message_id
        type_list[2] = call.message.chat.id

    elif type_list[0] == True or type_list[1] != 0:
        bot.edit_message_text(text=new_text, chat_id=call.message.chat.id, message_id=type_list[1], parse_mode="Markdown")
        type_list[0] = False

