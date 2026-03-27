from telethon import TelegramClient, events

clients = {}

async def start_userbot(phone, api_id, api_hash):
    client = TelegramClient(f"sessions/{phone}", api_id, api_hash)

    await client.start(phone=phone)
    clients[phone] = client

    print(f"✅ {phone} ulandi")

    @client.on(events.NewMessage)
    async def handler(event):
        sender = await event.get_sender()
        print(f"{sender.id}: {event.text}")

    await client.run_until_disconnected()
