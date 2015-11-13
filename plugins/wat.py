import random

import requests

__commands__ = '''
    wat - provides link to random WAT image
'''

local_wats = (
    'http://s.telegraph.co.uk/graphics/html/Years/2013/images/owl4.gif',
    'https://s3-eu-west-1.amazonaws.com/alex-random/rella.gif',
)


def plugin(bot):
    @bot.hear('wat$')
    def wat(response):

        # my approximation
        remote_wats_number = 50

        if random.randint(1, remote_wats_number + len(local_wats)) <= remote_wats_number:
            r = requests.get('http://watme.herokuapp.com/random')
            wat_link = r.json()['wat']
        else:
            wat_link = random.choice(local_wats)

        return wat_link
