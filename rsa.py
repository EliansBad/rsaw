import requests as send
import json
from random import choice as rand
from rsaw.v5.RsawErrors import *

class RandomStuff:
    def __init__(self, key, server='main', debug=False, plan='none'):
        if plan in 'none': self.ai = 'https://api.pgamerx.com/v5/ai'
        else: self.ai = f'https://api.pgamerx.com/v5/premium/{plan}/ai'
        self.joke = 'https://api.pgamerx.com/v5/joke'
        self.covid = 'https://api.pgamerx.com/v5/covid'
        self.weather = ''
        self.server = server
        self.debug = debug
        self.key = key  #probably a good time to mention i have no intentions of stealing anyones key's

    def set_backups(self, ai=['Request failed!'], joke=['Request failed!']):
        self.ai_backup = ai
        self.joke_backup = joke

    def ai_response(
        self,
        message,
        res_type='json',
        custom={
            'bot_name': 'Random Stuf API ™',
            'bot_gender': 'male',
            'bot_master': 'PGamerX',
            'bot_age': '19',
            'bot_company': 'PGamerX Studio',
            'bot_location': 'India',
            'bot_email': 'admin@pgamerx.com',
            'bot_build': 'Public',
            'bot_birth_year': '2002',
            'bot_birth_date': '1st January, 2002',
            'bot_birth_place': 'India',
            'bot_favorite_color': 'Blue',
            'bot_favorite_book': 'Harry Potter',
            'bot_favorite_band': 'Imagine Doggos',
            'bot_favorite_artist': 'Eminem',
            'bot_favorite_actress': 'Emma Watson',
            'bot_favorite_actor': 'Jim Carrey'
        }
    ):  # PLEASE EITHER GIVE A TYPE OF JSON IF YOU WANT THE FULL REQUEST OR TEXT

        head = {'Authorization': self.key}
        params = {'message': message, 'server': self.server}
        params.update(custom)
        req = send.get(url=self.ai, params=params, headers=head)

        try:
            if res_type.lower() in 'text':  # if res_type is set to text it will just auto index it just to the response
                val = req.json()[0]['response']
            else:
                val = req.json()

        except json.decoder.JSONDecodeError as err:
            if self.debug == False:
                val = rand(self.ai_backup)
            else:
                if req.text in 'Forbidden! The Premium API Key is incorrect, kindly recheck':
                    raise InvalidKeyError('Your Key is invalid')

                elif req.text in 'Message/Server is missing':
                    raise ParamError('Message is missing')

                elif req.text in 'API Key is missing! Kindly get one at api.pgamerx.com/register':
                    raise InvalidKeyError('Key is missing, get one at api.pgamerx.com/register')
                    
        return val

    def get_joke(self, joke_type='any', block='', res_type='json'):
        head = {'Authorization': self.key}
        if block == '':
            params = {'type': joke_type}
        else:
            params = {'type': joke_type, 'blacklist': block}

        joke = send.get(url=self.joke, params=params, headers=head)

        try:
            if res_type.lower() in 'text': val = joke.json()['joke']
            else: val = joke.json()
        except KeyError:
            if res_type.lower() in 'text':
                val = joke.json()['setup'] + '\n' + joke.json()['delivery']
            else:
                val = joke.json()
        except json.decoder.JSONDecodeError:
            if self.debug == False:
                val = rand(self.joke_backup)
            else:
                if joke.text in 'Forbidden! The Premium API Key is incorrect, kindly recheck':
                    raise InvalidKeyError('Your Key is invalid')

                elif joke.text in 'No Type Provided':
                    raise ParamError('Joke type not provided')

                elif joke.text in 'Invalid Type Provided':
                    raise ParamError('Please enter a valid type (https://docs.pgamerx.com/endpoints/joke/types)')

                elif joke.text in 'Invalid Flags Provided':
                    raise ParamError('Please enter valid flags (https://docs.pgamerx.com/endpoints/joke/flags)')

                elif joke.text in 'API Key is missing! Kindly get one at api.pgamerx.com/register':
                    raise InvalidKeyError('Key is missing, get one at api.pgamerx.com/register')
                    

        return val
