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

        self.set_fields()

    def __unicode__(self):
        return str(self.id)

class Team(utils.DataModelClass):

    def __init__(self, **kwargs):
        self.id = None
        self.name = None
        self.mascot = None
        self.abbr = None

        self.set_fields()

    def __unicode__(self):
        return self.abbr


class Load(utils.BaseModelClass):

    def __init__(self, *args, **kwargs):
        self.weeks = range(1, 18)
        self.schedule_url = 'http://www.nfl.com/schedules/2015/REG%s'
        self.games = []

        self.set_data_directory()

    def get_data(self):
        for week in self.weeks:
            r = requests.get(self.schedule_url % week)
            soup = BeautifulSoup(r.content, 'lxml')

            list_items = soup.select('ul.schedules-table li')

            current_date = None

            print "Week %s" % week

            for li in list_items:

                # Decide if this is a DATE item or a GAME item.
                if ("schedules-list-date" in li.attrs['class']) and ("next-game" not in li.attrs['class']):
                    current_date = li.text.strip()

                if current_date and ("schedules-list-matchup" in li.attrs['class']):
                    """
                    <div class="schedules-list-content post expandable primetime type-reg pro-legacy" data-gameid="2015091000" data-away-abbr="PIT" data-home-abbr="NE" data-away-mascot="Steelers" data-home-mascot="Patriots" data-gamestate="POST" data-gc-url="http://www.nfl.com/gamecenter/2015091000/2015/REG1/steelers@patriots" data-localtime="20:30:00" data-shareid="sb-liu2s52c" data-site="Gillette Stadium">
                    """
                    g = Game()
                    game = li.select('div.schedules-list-content')[0]
                    g.id = game.attrs['data-gameid']
                    g.week = week
                    g.date = current_date
                    g.time = li.select('div.schedules-list-hd span.time')[0].text.strip()
                    g.site = game.attrs['data-site']

                    g.home_team = Team()
                    g.home_team.abbr = game.attrs['data-home-abbr']
                    g.home_team.mascot = game.attrs['data-home-mascot']
                    g.home_team = g.home_team.__dict__

                    g.away_team = Team()
                    g.away_team.abbr = game.attrs['data-away-abbr']
                    g.away_team.mascot = game.attrs['data-away-mascot']
                    g.away_team = g.away_team.__dict__

                    self.games.append(g.__dict__)

    def write_data(self):
        with open('%s/schedule.json' % self.DATA_DIRECTORY, 'w') as writefile:
            writefile.write(json.dumps(self.games))

if __name__ == "__main__":
    l = Load()
    l.get_data()
    l.write_data()
