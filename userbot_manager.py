from telethon import TelegramClient, events

clients = {}

async def start_userbot(name, api_id, api_hash, phone):
    client = TelegramClient(f"sessions/{name}", api_id, api_hash)

    await client.start(phone=phone)

    clients[name] = client

    print(f"✅ {name} ulandi")

    @client.on(events.NewMessage)
    async def handler(event):
        sender = await event.get_sender()
        print(f"[{name}] {sender.id}: {event.text}")

    await client.run_until_disconnected()
