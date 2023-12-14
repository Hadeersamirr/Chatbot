from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
tokenn:Final ='6601782958:AAEYEcMcXMqjzjhYwfw6QA7DeayPusPczvY'
bot_username ='@banbananaaaa_bot'
#commands
async def start_command(update: Update ,context:ContextTypes.DEFAULT_TYPE ):
    # dy el message elly hatzhr awl ma press start
    await update.message.reply_text("Hello, thanks for Chatting with me, I am a banana!  ")

async def help_command(update: Update ,context:ContextTypes.DEFAULT_TYPE ):
    # dy el message elly hatzhr awl ma press start
    await update.message.reply_text("I am a Banana, Please Type something so I can Respond ! ")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # dy el message elly hatzhr awl ma press start
    await update.message.reply_text("This is a custome code!")


# Responses

#comment22


def handle_response(text: str) -> str:
    processed :str = text.lower()
    if 'hello' in processed :
        return 'Hey There !'

    if 'Hello' in processed :
        return 'Hey There !'

    if 'hi' in processed :
        return 'Hey There !'

    if 'Hi' in processed :
        return 'Hey There !'
    if 'how are you' in processed :
        return 'I am good!'

    if 'i am sad' in processed :
        return 'I am really sorry to hear that you are feeling sad. It is okay to feel this way sometimes. If you would like to talk about it or if there is anything I can do to help, please feel free to share. I am here for you'

    if 'who created you' in processed:
        return 'I was created by a talented individual who loves bananas!'
    if 'how do you work' in processed:
        return 'I analyze your input and try to respond in a way that makes sense. It\'s all about coding and algorithms!'

    if 'how is your day going?' in processed:
        return ' My day is going well, thanks for asking! How about yours?'

    if 'tell me a joke!' in processed:
        return ' Sure, here is one: Why did the scarecrow win an award? Because he was outstanding in '

    if 'tell me another joke' in processed:
        return 'Why did the banana go to the doctor? Because it wasn’t peeling well!'

    if 'tell me something interesting' in processed:
        return 'Did you know that bananas are berries but strawberries are not?'

    if 'thank you' in processed:
        return 'You\'re welcome!'

    if 'baaolk eh' in processed:
        return ' eh ya yasso?? '
    if 'banana bot is my favourite bot' in processed:
        return ' oh no i love you so much  '
    if 'okay thank you, bye' in processed:
        return 'Goodbye! If you ever want to chat, I will be here.'

    return 'I do not understand what you wrote.....'

async def handle_message(update:Update , context : ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text:str = update.message.text
    print(f'User({update.message.chat.id} in {message_type}: "{text}" ' )
    if message_type=='group':
        if bot_username in text:
            new_text:str =text.replace(bot_username,'').strip()
            response:str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)

    print('Bot: ',response )
    await update.message.reply_text(response)

async def error(update:Update , context : ContextTypes.DEFAULT_TYPE):
    print(f'Update {Update} caused error {context.error}')


if __name__ == '__main__':
    print('starting bot.... ')
    app = Application.builder().token(tokenn).build()
    app.add_handler(CommandHandler('Start', start_command))
    app.add_handler(CommandHandler('Help', help_command))
    app.add_handler(CommandHandler('Custom',custom_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    #error
    app.add_error_handler(error)
    print('Polling')
    app.run_polling(poll_interval=3)