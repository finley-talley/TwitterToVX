import discord, config
import bot_tools as tools
from aiohttp import connector

intents = discord.Intents.default()
intents.message_content = True # required for on_message event

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # ignore bot's messages
    if message.author == client.user:
        return

    if 'https://twitter.com' in message.content:
        await message.edit(suppress=True)
        ind = tools.find_url_index('https://twitter.com', message.content)
        urls = tools.get_urls(message.content, ind)
        urls = tools.change_to_vx('https://twitter.com', urls, 'twt')
        await message.channel.send('\n'.join(urls))

    if 'https://x.com' in message.content:
        await message.edit(suppress=True)
        ind = tools.find_url_index('https://x.com', message.content)
        urls = tools.get_urls(message.content, ind)
        urls = tools.change_to_vx('https://x.com', urls, 'twt')
        await message.channel.send('\n'.join(urls))

    if 'https://www.tiktok.com' in message.content:
        await message.edit(suppress=True)
        ind = tools.find_url_index('https://www.tiktok.com', message.content)
        urls = tools.get_urls(message.content, ind)
        urls = tools.change_to_vx('https://www.tiktok.com', urls, 'tt')
        await message.channel.send('\n'.join(urls))

    if 'https://www.instagram.com' in message.content:
        await message.edit(suppress=True)
        ind = tools.find_url_index('https://www.instagram.com', message.content)
        urls = tools.get_urls(message.content, ind)
        urls = tools.change_to_vx('https://www.instagram.com', urls, 'ig')
        await message.channel.send('\n'.join(urls))

# try:
#     client.run(config.dsc_token)
# except connector.ClientConnectorError:
#     pass

client.run(config.dsc_token)


