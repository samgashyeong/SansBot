import discord
import asyncio
from SansParser import *
import datetime
import random
import pytz
client = discord.Client()

token = "1"

where = ["맘스터치", "롯데리아", "놀이터", "선린인고",
"급식실", "컴퓨터실", "화장실", "교무실", "경비실", "서브웨이", "편의점", "교실", "체육관", "방송실", "자택", "나는"]
doing_Ms = ["에 가서 피클먹는", "에서 검거된", "를 몰래 훔쳐보는", " 케찹도둑", " 감자튀김도둑", " 알바생모자도둑", "에서 애니보는", " 식판도둑", "에서 빅맥먹는", " 물티슈도둑", " 매직팬티도둑"]
doing_Ld = [" 케찹도둑", " 감자튀김도둑", "에서 검거된", "음료수 컵 도둑", "에서 애니보는", "아이스크림도둑", " 식판도둑", "에서 빅맥먹는", " 물티슈도둑", " 매직팬티도둑"]
doing_playground = [" 터트리는", "에서 꼽주는", "에서 노는거 훔쳐보는", "에서 다리떠는", " 모래도둑", "에서 고백하는"]
doing_surnin = [" 분필도둑", " 의자도둑", " 시험지도둑"," 책상도둑", "에서 다리떠는", "에서 아무것도 못하는", " 대표꼰대", " 대표찐따"," 롤창", " 대깨옵"," 들어가지 못하는", " 물티슈도둑", " 매직팬티도둑"]
doing_lunch = ["에서 애니보는"," 양파도둑", " 김치도둑", " 의자도둑", " 에서 혼자 밥먹는", " 터트리는", "몰래들어가는", " 세치기하는", "에서 고백하는"]
doing_computer = [" 마우스도둑", " 모니터도둑", "에서 애니보는", " 몰래보는", "에서 다리떠는", " 물티슈도둑", " 매직팬티도둑", " 조이스틱도둑"]
doing_tolit = [" 휴지도둑", "몰래들어가는", " 비누도둑", "에서 검거된", "에서 눈치보는", "에서 머리감는", "에서 고백하는", "에서 애니보는", "에서 급식먹는", " 물티슈도둑", " 매직팬티도둑"]
doing_geomu = ["에서 꼽주는", "에서 혼나는", " 몰래들어가는", " 시험지도둑", "에서 애니보는", "에서 라면먹는", "에서 급식먹는", " 컴퓨터도둑", "에서 꼽주는", "터트리는", "에서 검거된"]
doing_geongbi = ["에서 잠자는", " 터트리는", " 훔쳐보는", " 명단도둑", " 호루라기도둑", " 모자도둑", " 볼펜도둑"]
doing_subway = [" 양파도둑", " 소스도둑", " 케찹도둑", "에서 다리떠는", "에서 애니보는", "에서 검거된", " 식판도둑", "에서 아무것도 못하는", " 빵도둑", "에서 빅맥먹는"]
doing_24 = [" 알바생모자도둑", " 삼각김밥도둑", " 김밥도둑", " 사탕도둑", " 문상도둑", "에서 애니보는", "에서 꼽주는", "에서 다리떠는", "에서 검거된", " 터트리는"]
doing_class = [" 일짱", " 노예", " 분필도둑", " 볼펜도둑", " 출석부도둑", "에서 꼽주는", "에서 다리떠는", "터트리는", "에서 검거된", "에서 애니보는"]
doing_exer = ["농구공도둑", "축구공도둑", "에서 애니보는", "에서 가오잡는", "에서 키재는", "탁구공도둑", "테니스채도둑", "배드민턴채도둑", "에서 검거된", "에서 고백하는"] 
doing_board = [" 마이크도둑", " 카메라도둑", "에서 고백하는", "에서 애니보는", " 청소부", " 의자도둑", "에서 다리떠는", " 몰래들어가는", " 터트리는"]
doing_house = ["에서 검거된", "에 들어가지못하는", " 라면도둑", "에서 검거된", "에서 발견된", " 훔쳐보는", " 몰래들어가는", " 물티슈도둑", " 매직팬티도둑"]
doing_im = [" 왕렬쌤만 바라보는", " 매직팬티만 바라보는", " 분필만 바라보는", " 모니터만 바라보는", " 빢빢이", " 대깨옵", " 롤창", " 대깨메"]
doing = [" 몰래들어가는", " 훔쳐보는", " 터트리는", " 좋아하는", " 싫어하는", " 역겨워하는", " 들어가지못하는", "에서 노는", "에서 다리떠는", "에서 아무것도 못하는", "에서 검거된"]

def rdWhere():
    rdW = random.randint(0, len(where)-1);
    return where[rdW]
def rdDoing(doing):
    rdD = random.randint(0, len(doing)-1);
    return doing[rdD]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='ㅘ도움말'))
 
@client.event
async def on_message(message):
    if message.content.startswith("WA!"):
        await message.channel.send('SANS!')

    elif message.content.startswith("무한~"):
        await message.channel.send("무야호~")

    elif message.content.startswith('ㅘ오늘급식'):
        today = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
        todayDate = today.strftime("%Y.%m.%d")
        weekday = today.weekday()
        print(weekday)

        diet = get_diet(2, todayDate, weekday)

        if len(diet) == 1:
            await message.channel.send('오늘급식없다!')
        else:
            lunchDate = todayDate+"\n"+diet
            await message.channel.send(lunchDate)

    elif message.content.startswith('ㅘ내일급식'):
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

    elif message.content.startswith('ㅘ급식 이번주'):
        strweekday = str(message.content.split(" ")[2])
        if(strweekday == "월"): weekday = 0
        elif(strweekday == "화"): weekday = 1
        elif(strweekday == "수"): weekday = 2
        elif(strweekday == "목"): weekday = 3
        elif(strweekday == "금"): weekday = 4
        elif(strweekday == "토" or strweekday == "일"): 
            await message.channel.send(strweekday+"요일는 급식이 없는 날임 ㅋ")
            return
        else: 
            await message.channel.send("요일 다시보내셈 ㅋ")
            return

        today = datetime.datetime.now(pytz.timezone('Asia/Seoul'))+datetime.timedelta(weekday);
        todayDate = today.strftime("%Y.%m.%d")
        realweekday = today.weekday()

        diet = get_diet(2, todayDate, realweekday)

        if len(diet) == 1:
            await message.channel.send('급식없다!')
        else:
            lunchDate = todayDate+"\n"+diet
            await message.channel.send(lunchDate)

    elif message.content.startswith('ㅘ급식 다음주'):
        strweekday = str(message.content.split(" ")[2])
        if(strweekday == "월"): weekday = 0
        elif(strweekday == "화"): weekday = 1
        elif(strweekday == "수"): weekday = 2
        elif(strweekday == "목"): weekday = 3
        elif(strweekday == "금"): weekday = 4
        elif(strweekday == "토" or strweekday == "일"): 
            await message.channel.send(strweekday+"요일는 급식이 없는 날임 ㅋ")
            return
        else: 
            await message.channel.send("요일 다시보내셈 ㅋ")
            return

        today = datetime.datetime.now(pytz.timezone('Asia/Seoul'))+datetime.timedelta(weekday)+datetime.timedelta(days=7);
        todayDate = today.strftime("%Y.%m.%d")
        realweekday = today.weekday()

        diet = get_diet(2, todayDate, realweekday)

        if len(diet) == 1:
            await message.channel.send('급식없다!')
        else:
            lunchDate = todayDate+"\n"+diet
            await message.channel.send(lunchDate)
    
    elif message.content.startswith('ㅘ급식 '):
        date = str(message.content.split(" ")[1])
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

    elif message.content.startswith('ㅘ이름추천 '):
        name = str(message.content.split(" ")[1])
        wh = rdWhere()
        if wh == '맘스터치': apt = doing_Ms
        elif wh == "롯데리아" : apt = doing_Ld
        elif wh == "놀이터" : apt = doing_playground
        elif wh == "선린인고" : apt = doing_surnin
        elif wh == "급식실" : apt = doing_lunch
        elif wh == "컴퓨터실" : apt = doing_computer
        elif wh == "화장실" : apt = doing_tolit
        elif wh == "교무실" : apt = doing_geomu
        elif wh == "경비실" : apt = doing_geongbi
        elif wh == "서브웨이" : apt = doing_subway
        elif wh == "편의점" : apt = doing_24
        elif wh == "교실" : apt = doing_class
        elif wh == "체육관" : apt = doing_exer
        elif wh == "방송실" : apt = doing_board
        elif wh == "자택" : apt = doing_house
        elif wh == "나는" : apt = doing_im

        print(wh ,apt)

        nickname = str(wh + rdDoing(apt) +" "+name)
        await message.channel.send("\'"+nickname +"\'" + "을 추천합니다!")
        


    elif message.content.startswith('ㅘ도움말'):
        explain = "ㅘ[오늘/내일]급식 -> 해당날 급식 안내\n\nㅘ급식 [이번주/다음주] [요일] ->해당날 급식 안내\n\nㅘ급식 [일정] -> 해당날 급식 안내\n\nex)-급식 2020MMDD\n\nㅘ이름추천 [이름] ->이름추천"
        await message.channel.send(explain)



client.run(token)
