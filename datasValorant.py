import requests
import json
import datetime
import embeds as e
import discord

def get_games_today():

	#Get current date and convert from string
	today = datetime.datetime.now()
	year = str(today.year)
	month = str(today.month) if today.month >= 10 else '0' + str(today.month)
	day = str(today.day) if today.day >= 10 else '0' + str(today.day)


	#String complete and only date formartBR
	dateBr = day + '/' + month + '/' + year
	stringRangeToday = year + '-' + month + '-' + day + 'T'  

	#Request
	linkRequest = 'https://api.pandascore.co/valorant/matches/upcoming?&range[begin_at]=' + stringRangeToday + '00:00:00Z,' + stringRangeToday + '23:59:59Z&token=CZ2gKXBwL8LYIKbj_VzKC8cjujXZcVF-vlwPf8P3qC-GcHnSoRQ'

	#rTest = 'https://api.pandascore.co/valorant/matches/upcoming?&range[begin_at]=2021-09-13T00:00:00Z,2021-09-13T23:59:59Z&token=CZ2gKXBwL8LYIKbj_VzKC8cjujXZcVF-vlwPf8P3qC-GcHnSoRQ'

	r = requests.get(linkRequest)
	responseJson = r.json()

	#list and count
	a  = []
	count = 0
	count2 = 0
	for i in responseJson:
		idC = count
		dateTime = i['begin_at']
		serieName = i['serie']['name']
		thumb = i['league']['image_url']
		idSerie = i['serie']['id']

		hour = int(dateTime[11:13]) - 3
		minSec = dateTime[13:16]
		dateTimeFormated = dateBr + ' - ' + str(hour) + minSec
		
		datas = dict(id=idC, serieName=serieName, dateTime=dateTimeFormated, thumb=thumb, serieID=idSerie)


		for j in i['opponents']:
			teamName = j['opponent']['name']
			idTeam = j['opponent']['id']

			if count % 2 == 0:

				teams = dict(teamName0=teamName, id0=idTeam)

			else:

				teams = dict(teamName1=teamName, id1=idTeam)

			datas.update(teams)
			count += 1

		count2 += 1

		a.append(datas)	

	return a

