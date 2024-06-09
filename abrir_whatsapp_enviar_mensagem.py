import pyautogui as bot 
import time 

bot.pause = 3 #tempo de resposta bot 

# abrir o whatsapp 
bot.press ('win')
bot.write('whatsapp')
bot.press('enter')
time.sleep(5)

#localização de contato 
bot.click(x=171, y=119)
time.sleep(2)
bot.write('Nome do contato')
time.sleep(2)
bot.press('enter')
time.sleep(5)


#enviando a mensagem pro contato 
bot.click(x=890, y=1018)
time.sleep(2)
bot.write('inserir a mensagem que eu quero enviar')
bot.press('enter')

