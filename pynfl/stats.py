import json

from bs4 import BeautifulSoup
import requests

from pynfl import utils


class Game(utils.DataModelClass):

    def __init__(self, **kwargs):
        self.id = None
        self.location = None
        self.time = None
        self.date = None
        self.week = None
        self.site = None
        self.home_team = None
        self.away_team = None

        self.home = {}
        self.away = {}
        self.drives = {}
        self.scrsummary = {}
        self.qtr = None
        self.down = None
        self.togo = None
        self.clock = None
        self.possession = None
        self.redzone = None

        self.set_fields(**kwargs)

    def __unicode__(self):
        return str(self.id)

class Team(utils.DataModelClass):

    def __init__(self, **kwargs):
        self.id = None
        self.name = None
        self.mascot = None
        self.abbr = None

        self.set_fields(**kwargs)

    def __unicode__(self):
        return self.abbr


class Load(utils.BaseModelClass):

    def __init__(self, *args, **kwargs):
        self.data_url = 'http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json'
        self.set_data_directory()
        self.game_id = kwargs.get('game_id', '2015091700')
        self.game_obj = None

    def get_data(self):
        with open('%s/schedule.json' % self.DATA_DIRECTORY, 'r') as readfile:
            games = json.loads(readfile.read())

        for game in games:
            if game['id'] == self.game_id:
                g = Game(**game)
                break

        r = requests.get(self.data_url % (self.game_id, self.game_id))

        try:
            game_dict = json.loads(r.content)[self.game_id]

            g.set_fields(**game_dict)

            self.game_obj = g

        except:
            pass

    def write_data(self):
        try:
            file_slug = '%s/game-%s-%s-%s.json' % (
                self.DATA_DIRECTORY,
                self.game_obj.id,
                self.game_obj.qtr,
                self.game_obj.clock.replace(':', ''))
            with open(file_slug, 'w') as writefile:
                writefile.write(json.dumps(self.game_obj.__dict__))
        except:
            pass


if __name__ == "__main__":
    l = Load()
    l.get_data()
    l.write_data()
