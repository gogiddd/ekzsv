from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id='26724138', api_hash='cff6dfd60637abb12cde975d934a16d8')


chat_id = "@datinganon_bot"  #тут свой чат в котором спамить

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if '/stop - завершить диалог' in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(1.8)
        await app.send_message(chat_id, "Здраствуйте! Совсем скоро огэ/еге, а ты ещё не готов к этому геммору?")
        sleep(2)
        await app.send_message(chat_id, """У меня есть специальное предложение для тебя!\n
Все знают, что система образования в нашей стране меняется, именно поэтому у меня есть доступ к ответам!\n
За небольшую, чисто символическу сумму, я готов поделиться всеми вариантами, какие могут только попасться, в твоём регионе!""")

        if '/stop - завершить диалог' in message.text:
             sleep(1.7)
             await app.send_sticker(chat_id, "CAACAgIAAxkBAAEIZHVkJmA83VTzbUpwOutlg3clP7XNawACgykAAgHYOUnFuS7AQ72iOi8E")
             sleep(2)

             if "/stop - завершить диалог"  in message.text:  # Меняем это значение если хотим спамить в другом чате
                 await app.send_message(chat_id, "/stop")
                 sleep(1.5 )
                 await app.send_message(chat_id, "Найти собеседника 🔎")


app.run()