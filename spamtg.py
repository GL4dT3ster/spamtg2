from telethon.sync import TelegramClient, events

#from pyotp import TOTP

#if input("Введи код из статьи: ") != TOTP("UC2UQZPN32334CZK").now():
#	exit(1)
#else:
#	print("Код верный")


print(" 'TG - spam' - скрипт написан SergoProxy, для спама в лс Telegram. \n Все вопросы и идеи в TG: @sergey0804 \n P.S. На данный момент, октябрь 2022 года, на гитхабе этот скрипт отсутсвует. \n Пересоздал скрипт GL4T3ster. Удачи!")
print()
hashtg = input("Хэш аккаунта: ")
iptg = int(input("IP приложения: "))
px = int(input("Кол-во сообщений: "))
idp = input("ID пользователя: ")
mes = input("Текст сообщения: ")

api_id = iptg
api_hash = hashtg

with TelegramClient('proxy', api-id, api-hash) as client:
	for i in range(px):
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
		client.send_message(idp, mes)
