#!/usr/bin/python
import time
import json
import pprint
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.delegate import per_chat_id, create_open, pave_event_space, include_callback_query_chat_id


TOKEN = '291485784:AAGg8YM58v7U_iRH1_4FaUGF2-0Nvni3bfk'


class ChatHandler(telepot.helper.ChatHandler):
	def __init__(self, *args, **kwargs):
		super(ChatHandler, self).__init__(*args, **kwargs)
		self.editor = None

	def cancel_last(self):
		if self.editor:
			self.editor.editMessageReplyMarkup(reply_markup=None)
			self.editor = None

	def handle_command(self, cmd, chat_id):
		if cmd == '/show_button':
			keyboard = InlineKeyboardMarkup(inline_keyboard=[
				[
				 	InlineKeyboardButton(text='Yes', callback_data='yes'),
				 	InlineKeyboardButton(text='No', callback_data='no')
				],
			])
			sent = self.sender.sendMessage('Use inline keyboard', reply_markup=keyboard)
			self.editor = telepot.helper.Editor(self.bot, sent)

	def on_chat_message(self, msg):
		content_type, chat_type, chat_id = telepot.glance(msg)

		if content_type == 'text':
			text = msg['text']
			print msg['chat']['first_name'] + ': ' + text

			if text.startswith('/'):
				self.handle_command(text,chat_id)
			else:
				self.sender.sendMessage('Hey!')
				self.close()

	def on_callback_query(self, msg):
		query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

		if query_data == 'yes':
			self.cancel_last()
			self.sender.sendMessage(text='Yep')
		if query_data == 'no':
			self.cancel_last()
			self.sender.sendMessage(text='Nope')
		self.close()

	def on__idle(self, event):
		self.sender.sendMessage('You still there...?')

	def on_close(self, ex):
		a = 0



bot = telepot.DelegatorBot(TOKEN, [
    include_callback_query_chat_id(
        pave_event_space())(
            per_chat_id(), create_open, ChatHandler, timeout=10),
])
bot.message_loop(run_forever='Listening...')