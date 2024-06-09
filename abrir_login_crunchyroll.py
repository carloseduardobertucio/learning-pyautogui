import pyautogui as bot
import time

bot.pause = 3  # Pausa de 3 segundos entre as ações

# Abrir o navegador
bot.press('win')
time.sleep(1)  # Aguardar o menu iniciar abrir
bot.write('google chrome')
bot.press('enter')

# Aguarde o Chrome abrir
time.sleep(5)  # Ajuste conforme necessário dependendo da velocidade do seu sistema

# Abrir o site
bot.write('crunchyroll.com')
bot.press('enter')


# Aguarde o site carregar
time.sleep(10)  # Ajuste conforme necessário dependendo da velocidade da sua conexão e do carregamento do site

# Inserir dados no input do site
bot.click(x=1338, y=157)  # Clicar no login do site
time.sleep(5)  # Pausa para garantir que a ação seja registrada

bot.click(x=899, y=469)  # Clicar no campo de email
time.sleep(3)  # Pausa para garantir que o campo esteja focado

bot.write('login')  # Escrever o email
time.sleep(1)  # Pausa para garantir que o email foi escrito

bot.press('tab')  # Mudar para o campo de senha
time.sleep(1)  # Pausa para garantir que o campo de senha esteja focado

bot.write('senha')  # Escrever a senha
time.sleep(1)  # Pausa para garantir que a senha foi escrita

bot.press('enter')  # Pressionar enter para fazer login
