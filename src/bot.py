import os

import emoji
import telebot
from loguru import logger
from telebot import types

from src.constants import keyboards
from src.utils.io import read_json, write_json


class Bot:
	"""
	Template for telegram bot.
	"""
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
		self.echo_all = self.bot.message_handler(
			func=lambda m: True
			)(self.echo_all)

	def run(self):
		logger.info('Bot is running...')
		self.bot.infinity_polling()

	def echo_all(self, message):
		#write_json(message.json, "message.json")
		print(emoji.demojize(message.text))
		# self.bot.reply_to(message, message.text)
		self.bot.send_message(
			message.chat.id, message.text,
			#reply_markup=keyboards.main,
			#reply_markup=create_keyboard(message.chat.first_name)
			reply_markup=keyboards.main
			)

if __name__ == '__main__':
	logger.info('Bot started')
	bot = Bot()
	bot.run()
