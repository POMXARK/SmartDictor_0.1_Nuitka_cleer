
import edit_img as e
from choice_of_voice_engine import choice_of_voice_engine

def Dictor():

    num = 0
    while num < 10: #бесконечный цикл

        if e.edit_img() == True: #Проверка нового кадра
            choice_of_voice_engine() # проверка голосового движка какой выбран
