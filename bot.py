import discord
import json 
import datasValorant as dtv
import embeds as e
import time

#archive with tokens
archive = open('tokens.json', )
data = json.load(archive)

#disc tokens
tokenDisc = data['discord_token']
serverName = data['server_name']

client = discord.Client()

#Instance datas valorant
datasTodaygames = dtv.get_games_today()

#avatar
avatar_path = "cypher.jpg"

fp = open(avatar_path, 'rb')
pfp = fp.read()


@client.event
async def on_ready():
    channel = discord.utils.get(client.get_all_channels(), guild__name=serverName, name='news')


    for datas in datasTodaygames:
    	message = await e.embed_games_today(channel, datas)

    await client.user.edit(avatar=pfp)

client.run(tokenDisc)
