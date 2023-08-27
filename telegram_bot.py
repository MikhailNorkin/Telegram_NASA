import telegram


bot = telegram.Bot(token='6548050139:AAGf7MR4IC0UFTBjvnlmfoDhhRQOthzGudI')
bot.send_message(chat_id='@NASA_images_2023', text="I'm sorry Dave I'm afraid I can't do that.")
print(bot.get_me())