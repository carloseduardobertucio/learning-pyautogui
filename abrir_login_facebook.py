import pyautogui as bot 
import time 

bot.pause = 3 #duração de execução do bot

#execução de abrir o navegador 
bot.press('win')
bot.write('google chrome')
bot.press('enter')

#esperando o google chrome abrir
time.sleep(5)

#execução de abrir o facebook
bot.write('facebook.com')
bot.press('enter')

#esperando o facebook abrir
time.sleep(5)

#Point(x=1145, y=231) posição de login facebook
#Point(x=1168, y=284) posição de senha do facebook 

#agora vamos efetuar o login 
bot.click(x=1145, y=231) #clicando em email para escrever 
time.sleep(5)
bot.write('login') #escrevendo email 
time.sleep(5)
bot.press('tab')
time.sleep(5)
bot.write('senha') #escrevendo a senha 




