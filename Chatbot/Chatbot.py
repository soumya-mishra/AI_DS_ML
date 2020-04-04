from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
for files in os.listdir("C:/Machine Learning/data/"):
    data = open("C:/Machine Learning/data/"+ files,'r').readlines()
    bot.train(data)
while True:
    message = input("You:")
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
        print("Chatbot:",reply)
    if message.strip() == 'Bye':
           print("ChatBot:Bye")
           break
________
