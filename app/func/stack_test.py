import json
from aiogram.types import Message,CallbackQuery
from aiogram.filters import BaseFilter
import asyncio
import config
import datetime
import random
import os
id = -1002345076311
def create_json():
    print(1)  # Це можна прибрати після тестування

    if not os.path.exists('players.json'):
        try:
            with open('players.json', 'w') as file:
                bd = {'players': {}, 'chats': {}}
                json.dump(bd, file, indent=4)
                print('players.json створений')
        except Exception as e:
            print(f"Помилка при створенні файлу: {e}")
create_json()
class Player:
    
    def __init__(self,id_user:int, fullname):
        
        self.id= id_user
        self.fullname = fullname
        print(self.id)
        with open('players.json', 'r', encoding='UTF-8') as file:
            bd = json.load(file)
            bd["players"].setdefault(str(self.id), {})
            bd['players'][str(self.id)].setdefault('money',10000)
            bd['players'][str(self.id)].setdefault('rep',5)
            bd['players'][str(self.id)]['fullname'] = fullname
            bd['players'][str(self.id)].setdefault("date_first",datetime.datetime.now().strftime("%d %m %Y"))
        
        with open('players.json', 'w') as file:
                
            json.dump(bd,file, indent=4)


    def plus(self,money:int):
        self.money = money
        with open('players.json', 'r') as file:
            bd = json.load(file)
            bd["players"][str(self.id)]['money'] += money
            json.dumps(bd)
        with open('players.json', 'w') as file:
            json.dump(bd,file, indent=4)
    
    def minus(self,money:int):
        self.money = money
        with open('players.json', 'r') as file:
            bd = json.load(file)
            bd["players"][str(self.id)]['money'] -= money
            json.dumps(bd)
        with open('players.json', 'w') as file:
            json.dump(bd,file, indent=4)
    
    def check(self, key='all'):
        '''
            case 'all':        
                return bd['players'][str(self.id)]
            case 'rep':
                return bd["players"][str(self.id)]['rep']
            case 'money':
                return bd["players"][str(self.id)]['money']
            case "date_first":
                return bd['players'][str(self.id)]["date_first"]
            case _:
                raise KeyError(f'в функції check немає:{key}')
    
    '''
        with open('players.json', 'r') as file:
            bd = json.load(file)
        match key:    
            case 'all':        
                return bd['players'][str(self.id)]
            case 'rep':
                return bd["players"][str(self.id)]['rep']
            case 'money':
                return bd["players"][str(self.id)]['money']
            case "date_first":
                return bd['players'][str(self.id)]["date_first"]
            case _:
                raise KeyError(f'в функції check немає:{key}')


    def minus_rep(self, num=1):
        with open('players.json', 'r') as file:
            bd = json.load(file)
            bd['players'][str(self.id)]['rep'] -= num
            json.dumps(bd)
        with open('players.json', 'w') as file:
            json.dump(bd,file, indent=4)
    
    def plus_rep(self,num=1):
        with open('players.json', 'r') as file:
            bd = json.load(file)
            bd['players'][str(self.id)]['rep'] += num
            json.dumps(bd)
        with open('players.json', 'w') as file:
            json.dump(bd,file, indent=4)
    

    def all_id(self) -> list:
        with open('players.json', 'r') as file:
            bd = json.load(file)
            return list(bd['players'].keys())

    def all_user(self) -> list:
        with open('players.json', 'r') as file:
            bd = json.load(file)
            return bd['players']
    def stats_money(self) -> list:
        """
        [money,id,name]
        """
        stats_list = []
        
        for key,value in self.all_user().items():
            user = str(key)
            money = value['money']
            try:
                full_name = value['fullname']
            except:
                full_name = "Анонім"
            stats_list.append([money,user, full_name])
        stats_list.sort(key=lambda x: x[0],reverse=True)
        return stats_list

    async def subscribe(self,message:Message):
        status = await message.bot.get_chat_member(chat_id=id,user_id=self.id )
        print(status.status, "-"*10000)
        status.status
        if status.status == 'left':
            return False
        else:
            return True       
    def last_using_zp(self):
        with open('players.json', 'r') as file:
            bd = json.load(file)
            bd['players'][str(self.id)].setdefault(
                'last_using_zp', datetime.datetime.now().strftime('%d %m %Y, %H')
                )
            
            if (datetime.datetime.now() - datetime.datetime.strptime(bd['players'][str(self.id)]["last_using_zp"], "%d %m %Y, %H")).days >= 1:
                with open('players.json', 'w') as file:
                    bd['players'][str(self.id)]["last_using_zp"] = datetime.datetime.now().strftime('%d %m %Y, %H')
                    json.dump(bd,file, indent=4)
                    return True
            else:
                
                with open('players.json', 'w') as file:
                    json.dump(bd,file, indent=4)
        
class Chat:
    
    def __init__(self, chat_id:int):
        self.chat_id = chat_id
        with open('players.json', 'r+') as file:
            bd = json.load(file)
            bd['chats'].setdefault(str(self.chat_id), {})
            bd['chats'][str(self.chat_id)].setdefault("rules", None)
            bd['chats'][str(self.chat_id)].setdefault("mode", False)
           
        with open('players.json', 'w') as file:
            json.dump(bd,file,indent=4)

    def all_id(self) -> list:
        with open('players.json', 'r') as file:
            bd = json.load(file)
            return list(bd['chats'].keys())
        
    def set_rule(self, rule):
        with open('players.json', 'r') as file:
            bd = json.load(file)
            bd['chats'][str(self.chat_id)]['rules'] = rule
            json.dumps(bd)
        with open('players.json', 'w') as file:
            json.dump(bd,file,indent=4)
            print(1)
    
    def del_rule(self):
        with open('players.json', 'r') as file:
            bd = json.load(file)
            bd['chats'][str(self.chat_id)]['rules'] = None

        with open('players.json', 'w') as file:
            json.dump(bd,file,indent=4)

    def info_rule(self):
        with open('players.json', 'r+') as file:
            bd = json.load(file)
            return bd['chats'][str(self.chat_id)]['rules']
        
    def set_rufilt(self,mode=bool):
        with open('players.json', 'r') as file:
            bd = json.load(file)
            bd['chats'][str(self.chat_id)]['mode'] = mode
            json.dumps(bd)
        with open('players.json', 'w') as file:
            json.dump(bd,file, indent=4)
            print(1)
    def check_mode(self):
        with open('players.json', 'r') as file:
            bd = json.load(file)
            return bool(bd['chats'][str(self.chat_id)]['mode'])


class Filter_type(BaseFilter):
    def __init__(self,chat_type):
        self.chat_type = chat_type

    async def __call__(self,message:Message):
        if message.chat.type in self.chat_type:
            return message.chat.type in self.chat_type
        else:
            await message.reply('Команда не доступна в пп')
class Filter_admin(BaseFilter):
    def __init__(self):
        pass
    async def __call__(self,message:Message):
        admins = await message.bot.get_chat_administrators(message.chat.id)
        print(admins)
        for i in admins:
            if i.user.id == message.from_user.id :
                
                return True
        await message.reply('В вас немає прав адміністратора')
        return False

class Filter_admin_kb(BaseFilter):
    def __init__(self,id:int,chat:int):
        self.id = id
        self.chat = chat
    async def __call__(self,callback:CallbackQuery ):
        admins = await callback.bot.get_chat_administrators(self.chat)
        print(admins)
        print(callback)
        print('-'*200)
        print(callback.message)
        for i in admins:
            if i.user.id == self.id:
                callback.answer()
                return True
        await callback.answer('В вас немає прав адміністратора',show_alert=True)
        return False
a = Player(1, '3')