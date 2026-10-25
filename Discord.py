
import discord
from bot_logic import gen_pass
from bot_logic import gen_emoji
from bot_logic import flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("ok")
    elif message.content.startswith('contraseña'):
        respuesta = gen_pass(10)
        await message.channel.send(respuesta)
    elif message.content.startswith('emoji'):
        respuesta = gen_emoji()
        await message.channel.send(respuesta)
    elif message.content.startswith('moneda'):
        respuesta = flip_coin()
        await message.channel.send(respuesta)
    else:
        await message.channel.send(message.content)

client.run("MTU1Njc5NzA4MzExNjM3NjEyNA.GwaFoY.nmwj-PtACArr1idGyYN35oIKp_eaWn5xtwaT-Y")