import discord
import asyncio
from SansParser import *
import datetime
client = discord.Client()

token = "1"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='!WA 도움말'))
 
@client.event
async def on_message(message):
    if message.content.startswith("WA!"):
        await message.channel.send('SANS!')
 
    elif message.content.startswith('!say'):
        await message.channel.send('leave message')
        msg = await message.channel.send(timeout=15.0, author=message.author)
 
        if msg is None:
            await message.channel.send('15초내로 입력해주세요. 다시시도: !say')
            return
        else:
            await message.channel.send(msg.content)
    
    elif message.content.startswith('!WA 오늘급식'):
        today = datetime.datetime.today()
        todayDate = today.strftime("%Y.%m.%d")
        weekday = today.weekday()
        print(weekday)

        diet = get_diet(2, todayDate, weekday)

        if len(diet) == 1:
            await message.channel.send('오늘급식없다!')
        else:
            lunchDate = todayDate+diet
            await message.channel.send(lunchDate)

    elif message.content.startswith('!WA 내일급식'):
        today = datetime.datetime.today()+datetime.timedelta(days=1);
        todayDate = today.strftime("%Y.%m.%d")
        weekday = today.weekday()
        print(weekday)

        diet = get_diet(2, todayDate, weekday)

        if len(diet) == 1:
            await message.channel.send('내일급식없다!')
        else:
            lunchDate = todayDate+diet
            await message.channel.send(lunchDate)
    
    elif message.content.startswith('!WA 급식 '):
        date = str(message.content.split(" ")[2])
        year = int('20'+date[2:4])
        month = int(date[4:6])
        day = int(date[6:])
        date = '20' + date[2:4] + '.' + date[4:6] + '.' + date[6:]
        date1 = datetime.datetime(year, month, day).weekday()
        try:
            whatday = date1
            print(whatday)
        except:
            await message.channel.send("다시입력하셈 ㅋ : !WA 급식 날짜")
            return

        diet = get_diet(2, date, whatday)

        if len(diet) == 1:
            await message.channel.send('급식없다!')
        else:
            lunchDate = date+"\n"+diet
            await message.channel.send(lunchDate)


    elif message.content.startswith('!WA 도움말'):
        explain = "!WA [오늘/내일]급식 -> 해당날 급식 안내\n!WA 급식 [일정] -> 해당날 급식 안내\nex)!WA 급식 2020MMDD"
        await message.channel.send(explain)


client.run(token)