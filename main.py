from chatbot import ChatBot
from view import View
import tkinter
from tkinter import *

myChatBot = ChatBot()
#apenas carregar um modelo pronto
myChatBot.loadModel()

#criar o modelo
#myChatBot.createModel()

View(myChatBot)
