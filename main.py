from chatbot import ChatBot
from view import View
import tkinter
from tkinter import *

myChatBot = ChatBot()

#myChatBot.loadModel()

myChatBot.createModel()

View(myChatBot)
