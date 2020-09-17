import json
import os
import random
import requests
import time

from config import *
from util import mocking_case

class Bot:
    def __init__(self, bot_id, token=AUTH_TOKEN):
        self.token = AUTH_TOKEN
        self.id = bot_id

    def _send_message(self, msg):
        url = "https://api.groupme.com/v3/bots/post?token="+self.token
        payload = {'bot_id': self.id,
                   'text': msg}
        time.sleep(1)
        r = requests.post(url, data = json.dumps(payload))
        if r.status_code != 202:
            print("Msg sending failed with code: "+str(r.status_code))

    def on_receive_message(self, content):
        pass
    

class HenryBreyneBot(Bot):
    def on_receive_message(self, content):
        status_msg = "Breyne Bot running.\nEnv: {env}\nVersion: {version}".format(env=ENV,version=VERSION)
        
        generic_choices = ["Only I can say faggot, faggot.",
                           "Honestly, shut the fuck up, this is a Chick Fil A.",
                           "I am a massive pussy.",
                           "Those are my titties",
                           "~resepects woman~",
                           "~gets mad pussy~",
                           "YALL CLOSED??",
                           "WHERE IS MY BIKINI PICTURE?",
                           "I\'M PUTTING THE PUSSY BACK IN PUSSY LIPS, BITCH.",
                           "Hillary Clinton is one thicc bitch.",
                           "My respect woman meter is off the charts right now.",
                           "~falls in love with neonatzi~",
                           "~drowns in gamer fuel~",
                           "I'm so horny.",
                           "Is it normal to pull a muscle playing Mario Party?"]
        
        predefined = {'female': "THOT",
                      'california': "fucking libtards",
                      'woman': "THOT"}

        dick_quote = 'My penis is sore'
        boomer_quote = 'Is that boomer still talking about fIrSt RoBoTiCs?'
        llama_quote = 'If she doesn\'t love a llama onsie, she doesn\'t love me'
        backForth_quote = 'I\'m not another one of your thots, don\'t say that'
        backForthL_quote = 'Degenerate libtard.'
        que_quote = 'QUE PASA???'

        guarenteed_predefined = {'!hb': status_msg,
                                 '!status': status_msg,
                                 'dick': dick_quote,
                                 'penis': dick_quote,
                                 'Pat': boomer_quote,
                                 'McCarthy': boomer_quote,
                                 'onsie': llama_quote,
                                 'llama': llama_quote,
                                 'I\'m just trying to keep you on your toes': backForth_quote,
                                 'What is that supposed to me? I\'m a good holy boy.': backForthL_quote,
                                 'que pasa': que_quote
                                 }
        
        person_specific = {
            "42403488" : "Klug, shut the fuck up."
        }

        predefined_chance = 25
        generic_chance = 3
        person_specific_chance = 1
        mocking_case_chance = 2
        sender_type = content['sender_type']
        if sender_type != "user":
           return
        msg = content['text']
        sender_id = content['sender_id']
        if sender_id in person_specific:
            print("Found sender in person_specific mapping")
            if random.randint(0,100) <= person_specific_chance:
                self._send_message(person_specific[sender_id])
                return
        for key in guarenteed_predefined:
            if key.lower() in msg.lower():
                self._send_message(guarenteed_predefined[key])
                return

        if random.randint(0,100) <= mocking_case_chance:
            self._send_message(mocking_case(msg))
            return
    
        for key in predefined:
            print("Searching for: "+key)
            if key.lower() in msg.lower():
                print("Found: "+key)
                if random.randint(0,100) <= predefined_chance:
                    self._send_message(predefined[key])
                    return

        if random.randint(0,100) <= generic_chance:
            response_msg = generic_choices[random.randint(0, len(generic_choices)-1)]
            self._send_message(response_msg)
        return



class MichaelKlugBot(Bot):
    def on_receive_message(self, content):
        status_msg = "Klug Bot running.\nEnv: {env}\nVersion: {version}".format(env=ENV,version=VERSION)
        
        generic_choices = ["Dude, I love cancer.",
                           "Where the fuck is Carl?",
                           "DiD yOu KnOw I\'m In BmE?",
                           "I just love big personalities",
                           "~tilts head and says we\'ll see~",
                           "~sips daquirriiiiiii and looks dissappointed~",
                           "Fucking pigeons bro, fucking pigeons.",
                           "I'm a masochistic.",
                           "That\'s for me to know and you to find out.",
                           "Demisexuals for the win brah",
                           "~greases up Matt Davis~",
                           "Ok, boomer.",
                           "I\'m a fake, I\'m a fraud",
                           "Anybody got handcuffs?",
                           "WHERE IS NATE???",
                           "~enters in nothing but a towel~",
                           "~jizzes for memes~",
                           "Do you have a boyfriend?",
                           "That\'s why they call me Magic Mike",
                           "Don\'t give me pleasure"]
        
        predefined = {'female': "Yeah, I did that.",
                      'Fortnite': "WANNA PLAY FORT?",
                      'california': "DID YOU KNOW IM FROM CALI????",
                      'Klug, shut the fuck up.': "I\'m just trying to keep you on your toes"}

        weed_quote = 'BRO DONT SMOKE ON MY FLOOR'
        mia_quote = 'I LIKE MIA'
        alc_quote = 'Daquiriiiiiiiiiiiiiiiiiiiiii'
        sex_quote = 'I AM A DEMIXSEXUAL'
        nk_quote = 'Imma have to Nate-Kerr you on that one'
        toes_quote = 'I\'m just trying to keep you on your toes.'
        sig_quote = '~walks to sig delts at 3am to cuddle with Mia~'
        big_quote = 'I like big tits and big brains'
        age_quote = 'Age is only a number'
        church_quote = 'You wanna go to confession?'
        shoes_quote = 'The sig delts stole my shoes. I just know it.'
        basektball_quote = '~loses to Henry in 2K~'
        strip_quote = "~swings on removable stripper pole~"
        pole_quote = "~inserts removable stripper pole~"
        exl_quote = 'Yeah mothafucka, it\'s me'
        backOne_quote = 'What is that supposed to me? I\'m a good holy boy.'

        guarenteed_predefined = {'!mk': status_msg,
                                 '!status': status_msg,
                                 'weed': weed_quote,
                                 'room 31': weed_quote,
                                 'sex': sex_quote,
                                 'drink': alc_quote,
                                 'mia': mia_quote,
                                 'kerr': nk_quote,
                                 'toes': toes_quote,
                                 'cuddle': sig_quote,
                                 'tits': big_quote,
                                 'ass': big_quote,
                                 'boobs': big_quote,
                                 'old': age_quote,
                                 'age': age_quote,
                                 'church': church_quote,
                                 'christian': church_quote,
                                 'god': church_quote,
                                 'shoe': shoes_quote,
                                 'basketball': basektball_quote,
                                 'room': pole_quote,
                                 'pole': strip_quote,
                                 'wtf': exl_quote,
                                 'wth': exl_quote,
                                 'I\'m not another one of your thots, don\'t say that': backOne_quote}
        
        person_specific = {
            "22727730" : "Hi Henry, my name is the Michael Klug Bot."
        }

        predefined_chance = 25
        generic_chance = 3
        person_specific_chance = 1
        mocking_case_chance = 2
        sender_type = content['sender_type']
        if sender_type != "user":
            return
        msg = content['text']
        sender_id = content['sender_id']
        if sender_id in person_specific:
            print("Found sender in person_specific mapping")
            if random.randint(0,100) <= person_specific_chance:
                self._send_message(person_specific[sender_id])
                return
        for key in guarenteed_predefined:
            if key.lower() in msg.lower():
                self._send_message(guarenteed_predefined[key])
                return

        if random.randint(0,100) <= mocking_case_chance:
            self._send_message(mocking_case(msg))
            return
    
        for key in predefined:
            print("Searching for: "+key)
            if key.lower() in msg.lower():
                print("Found: "+key)
                if random.randint(0,100) <= predefined_chance:
                    self._send_message(predefined[key])
                    return

        if random.randint(0,100) <= generic_chance:
            response_msg = generic_choices[random.randint(0, len(generic_choices)-1)]
            self._send_message(response_msg)
        return
