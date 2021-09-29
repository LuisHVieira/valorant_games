import discord 

def embed_games_today(ctx, dic):
	
	for kw in dic.keys():

		if kw == 'serieName':
			embed = discord.Embed(title=dic[kw], colour=discord.Colour.green())

		elif kw =='id':
			pass

		elif kw == 'dateTime':
			embed.add_field(name='Datetime', value=dic[kw], inline='false')

		elif kw == 'thumb':
			embed.set_thumbnail(url=dic[kw])

		elif kw == 'serieID':
			pass

		elif kw == 'id0':
			pass

		elif kw == 'id1':
			pass

		elif kw == 'teamName0':
			embed.add_field(name='Teams', value=dic[kw], inline='false')
			
		else:
			embed.add_field(name='vs', value=dic[kw], inline='false')
		

	return ctx.send(embed=embed)
