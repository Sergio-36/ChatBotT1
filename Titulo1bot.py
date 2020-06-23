
import logging
import pandas as pd
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hola mi nombre es MET')
    # HACER UNA VARIABLE QUE CAPTURA LA ID DEL MENSAJE

def help(update, context):
    #lista de comandos disponibles
    update.message.reply_text("Lista de Comandos")
    update.message.reply_text('1- /start')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


# Crear diccionario con respuestas
def respuesta(update, context):
    #Responder en caso que la ide del mensaje sea 
    Entrada = update.message['chat']['username']

    print(update.message)
    update.message.reply_text(f"Encantado {Entrada} ¿Como te encuentras?")


def main():

    updater = Updater("1226416345:AAGH62TAf5Upw1QMEouUWeha5T67JZ7idQ8",
     use_context=True)
    dp = updater.dispatcher

    #ASIGNAR COMMANDOS
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # Funcion Echo puede usarse para las respuestas.
    dp.add_handler(MessageHandler(Filters.text, respuesta))

    # INICIO BOT probando los puush
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
