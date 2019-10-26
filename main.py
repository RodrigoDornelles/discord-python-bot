import discord
import pyrebase
import json


dataFirebase = {}
dataDiscord = {}

############################################################
# Carregar dados importantes para o bot
with open('config.json') as config:    
    
    data = json.load(config)

    dataFirebase = data['firebase']
    dataDiscord = data['discord']

############################################################
# Conectar ao firebase

firebase = pyrebase.initialize_app(dataFirebase)
db = firebase.database()

############################################################
# @todo n lembro como descrever oq isso faz

class MyClient(discord.Client):

    async def on_ready(self):
        print('[!] bot ativado como: ', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if 'defina' in message.content:
            data = {"teste": message.content}
            db.child("users").push(data)

        if message.author.id == 287242211215802368:
            await message.channel.send('cala boca iago!')

        if message.content == 'ping':
            await message.channel.send('pong')



client = MyClient()
client.run(dataDiscord['token'])


