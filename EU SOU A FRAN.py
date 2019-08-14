# -*- coding: utf-8 -*-   ##COLOCAR ACENTUAÇÃO##
import multiprocessing

import os

#Reconhecimento de voz#

import speech_recognition as sr
#importar chat#

from chatterbot import ChatBot
#METODO DE TREINAMENTO#

from chatterbot.trainers import ListTrainer
import win32com.client as wincl
import win32com
import random
#############################
#Aleatorios
from datetime import datetime


#######################################################################



shell = win32com.client.Dispatch('WScript.Shell')




conv = open('texto1.txt', 'r').readlines()
#frases = open('FRASESFRAN.txt','r').readline()

frases = random.choice(open("FRASESFRAN.txt",'r').readlines())
bot = ChatBot('Fran')

bot.set_trainer(ListTrainer)
#for _file in os.listdir('chats'):
 #   lines = open('chats/' + _file,'r').readlines())

bot.train(conv)# apontar treinamento



import pyttsx3
import speech_recognition as sr
from chatterbot.trainers import ListTrainer

speak = wincl.Dispatch('SAPI.SpVoice')

r=sr.Recognizer()

with sr.Microphone() as s:

    r.adjust_for_ambient_noise(s)#ajusta o microfone
    now = datetime.now()
    horas = 'São ' + str(now.hour) + ' horas e ' + str(now.minute) + ' minutos e ' + str(now.second) + ' segundos'

    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
              'Novembro', 'Dezembro']
    dia = ' Hoje é ' + str(now.day) + ' de ' + months[now.month - 1] + ' de ' + str(now.year)



    while True:
        try:

            audio = r.listen(s) #saida de audio
            speech = r.recognize_google(audio, language='pt-br')#entrada de audio

            if 'desligar' in speech:
                print('Você: ', speech)
                os.system('shutdown -s -t 540 -c "Vou desligar em 9 minutos"')
                speak.Speak('CURUZES desligando em nove minutos')
                print('CURUZES desligando em nove minutos')


            elif 'piada' in speech:
                print('Você: ', speech)
                print('Fran: Hm! Tá bom, vou contar essa daqui...')
                speak.Speak('Um! Tá bom, vou contar essa daqui...')
                piada = random.choice(open("Piadas.txt", 'r').readlines())
                print('Fran: ', piada)
                speak.Speak(piada)

            elif 'conta mais uma' in speech:
                print('Você: ', speech)
                print('Fran: Hmmm, Okay, Mas não ache que sou palhaça, vou contar só mais essa...')
                speak.Speak('Hmmm, Okay, Mas não ache que sou palhaça, vou contar só mais essa...')
                piada = (open("Piadapesadas.txt", 'r').readlines())
                print('Fra: ', piada)
                speak.Speak(piada)

            elif 'rola' in speech:
                print('Você: ', speech)
                print('Fran: KKKKKKKKKKKKKKKKK VAI LEVAR ROLA ENTÃO KKKKKK')
                speak.Speak('KKKKKKKKKKKKKKKKK VAI LEVAR ROLA ENTÃO KKKKKK')



            elif 'cancelar desligamento' in speech:
                print('Você: ', speech)
                os.system('shutdown -a')
                speak.Speak('Cancelando')
                print('Cancelando')

            elif 'Abrir Google' in speech:
                print('Você: ', speech)
                os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
                speak.Speak('Abrigando Google Chrome')
                print('Abrigando Google Chrome')

            elif 'Fechar Google' in speech:
                print('Você: ', speech)
                os.system('taskkill /f /im chrome.exe')
                speak.Speak('Fechando o Google Chrome')
                print('Fechando o Google Chrome')

            elif 'Oi Fran' in speech:
                print('Você: ', speech)
                frases = random.choice(open("FRASESFRAN.txt", 'r').readlines())
                speak.Speak(frases)
                print('Fran: ', frases)


            elif 'triste' in speech:
                print('Você: ', speech)
                triste = random.choice(open("tristeza.txt", 'r').readlines())
                speak.Speak(triste)
                print('Fran: ', triste)

            elif 'Quem é você' in speech:
                print('Você: ', speech)
                speak.Speak('Oi eu sou a FRAN')
                print('Fran: Oi eu sou a FRAN')

            elif 'Qual o seu nome' in speech:
                print('Você: ', speech)
                speak.Speak('Oi Prazer meu nome é Fran, e eu sou uma desinteligencia artificial')
                print('Fran: Oi Prazer meu nome é Fran, e eu sou uma desinteligencia artificial')

            elif 'reiniciar' in speech:
                print('Você: ', speech)
                os.system('shutdown -r -f -t 180 -c "Estou reiniciando o seu computador Jonas"')
                speak.Speak('Oi Jonas, vou reiniciar o seu computador')
                print('Fran: Oi Jonas, vou reiniciar o seu computador')

            elif 'Que horas são' in speech:
                print('Você: ', speech)
                speak.Speak(horas)
                print('Fran: ', horas)

            elif 'Que dia é hoje' in speech:
                print('Você: ', speech)
                speak.Speak(dia)
                print('Fran: ', dia)


            elif 'burra' in speech:
                print('Você: ', speech)
                speak.Speak('Burra é teu pai')
                print('Burra é teu pai')


            else:
                print('Você: ', speech)
                response = bot.get_response(speech)
                print('Fran: ', response)
                speak.Speak(response)  # falar a resposta
        except:
            frases = random.choice(open("FRASESFRAN.txt", 'r').readlines())
            speak.Speak(frases)
            print('Fran: ', frases)
            #speak.Speak('UM UM UM, não entendiii')
            #print('Hmmmm!, não entendiii')


