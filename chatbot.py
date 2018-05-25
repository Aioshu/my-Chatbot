from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os # since we import os directory

bot = ChatBot('REady For U AI') #Assign name to chatbot
bot.set_trainer(ListTrainer) # to train my ChatBot

for files in os.listdir('C:/Users/user\Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'): #load my files from the system 
        data =open('C:/Users/user\Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines() # for opening the data and to read the data from files
        bot.train(data) #train the bot using data
  
  
while True: # when training is done we input the message
		message = input('You:')
		if message.strip()!='Bye':
				reply = bot.get_response(message)
				print('ChatBot:',reply)
		if message.strip()=='Bye':
				print('ChatBot: Bye')
				break	   