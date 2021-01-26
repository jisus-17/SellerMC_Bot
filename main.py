import discord, asyncio
import json

pre = '#'
game = discord.Game("Shopping")
client = discord.Client()


with open('SellerMC_Bot/local/token.json') as f:
    data = json.load(f)

with open('SellerMC_Bot/data/img/logo.png', 'rb') as i:
    picture = discord.File(i)
    

token = data['token']

embed1=discord.Embed(color=0x5cd6ff)
embed1.set_thumbnail(url='https://minecraft-api.com/api/skins/Destine_ice/head/10/10.5/12')
embed1.add_field(name='React to make your buy', value=None, inline=False)
embed1.add_field(name='Producto1 - reaction💎', value=None, inline=True)
embed1.add_field(name='Producto2 - reaction💊', value=None, inline=True)
embed1.add_field(name='Producto3 - reaction🎺', value=None, inline=True)
embed1.set_footer(text='BOTShop ver 0.1.0')



@client.event
async def on_ready():
    print('Iniciado como {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=game)


#@client.event
#async def on_member_join(member):
#	get(member.guild.channels, id=768670193379049483)
#	await channel.send(f"{member} Welcome")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(pre + 'ping'):
        await message.channel.send('pong🏓')

    if message.content.startswith(pre + 'user'):
        #await message.channel.send(picture)
        await message.channel.send(file=discord.File('SellerMC_Bot/data/img/logo.png'))

    if message.content.startswith(pre + 'comprar'):
        
        await message.channel.send(embed=embed1)

    

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send('comprado')

client.run(token)
