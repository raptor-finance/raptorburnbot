import requests
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
print("Starting up...")


node = "https://rpc.raptorchain.io/"
burnAddress = "0x000000000000000000000000000000000000dead"
updater = Updater("", use_context=True) # removed login token
  
  
def start(update: Update, context: CallbackContext):
    print("Got a /start !")
    update.message.reply_text("Hi fellow raptor")

def burnStats(update: Update, context: CallbackContext):
    burned = requests.get(f"{node}/accounts/accountInfo/{burnAddress}").json().get("result").get("balance")
    update.message.reply_text(f"Total burnt \U0001f525 : {burned / 10**18} RPTR")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('burn', burnStats))
    
print("Loaded successfully !")
updater.start_polling()
