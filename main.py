from telegram import Bot
import time
import os

# Pegando o token e o ID do grupo nas variáveis de ambiente
TOKEN = os.environ['TOKEN']
GROUP_ID = int(os.environ['GROUP_ID'])

# Mensagem que será enviada
MENSAGEM = """⚠️ **Promoção exclusiva:** cadastre-se na BullsBet e garanta bônus de boas‑vindas!
Acesse agora → https://bullsbet.bet.br/?ref=ca938e040caa"""

bot = Bot(token=TOKEN)

# Envia a mensagem a cada 1 hora
while True:
    bot.send_message(chat_id=GROUP_ID, text=MENSAGEM, parse_mode='Markdown')
    time.sleep(3600)  # espera 1 hora
