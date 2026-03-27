from telethon import TelegramClient, events
from config import API_ID, API_HASH

clients = {}

async def start_userbot(phone):
    client = TelegramClient(f"sessions/{phone}", API_ID, API_HASH)
    await client.start(phone=phone)

    clients[phone] = client
    print(f"✅ {phone} ulandi")

    @client.on(events.NewMessage)
    async def handler(event):
        sender = await event.get_sender()
        print(f"{sender.id}: {event.text}")

    await client.run_until_disconnected()
