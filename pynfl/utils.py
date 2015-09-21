import os

# One day, this should be algorithmic.
GAME_WEEKS = [
    {"start_date":datetime.date(2015,9,8), "end_date":datetime.date(2015,9,14), "week":1},
    {"start_date":datetime.date(2015,9,15), "end_date":datetime.date(2015,9,21), "week":2},
    {"start_date":datetime.date(2015,9,22), "end_date":datetime.date(2015,9,28), "week":3},
    {"start_date":datetime.date(2015,9,29), "end_date":datetime.date(2015,10,5), "week":4},
    {"start_date":datetime.date(2015,10,6), "end_date":datetime.date(2015,10,12), "week":5},
    {"start_date":datetime.date(2015,10,13), "end_date":datetime.date(2015,10,19), "week":6},
    {"start_date":datetime.date(2015,10,20), "end_date":datetime.date(2015,10,26), "week":7},
    {"start_date":datetime.date(2015,10,27), "end_date":datetime.date(2015,11,2), "week":8},
    {"start_date":datetime.date(2015,11,3), "end_date":datetime.date(2015,11,9), "week":9},
    {"start_date":datetime.date(2015,11,10), "end_date":datetime.date(2015,11,16), "week":10},
    {"start_date":datetime.date(2015,11,17), "end_date":datetime.date(2015,11,23), "week":11},
    {"start_date":datetime.date(2015,11,24), "end_date":datetime.date(2015,11,30), "week":12},
    {"start_date":datetime.date(2015,12,1), "end_date":datetime.date(2015,12,7), "week":13},
    {"start_date":datetime.date(2015,12,8), "end_date":datetime.date(2015,12,14), "week":14},
    {"start_date":datetime.date(2015,12,15), "end_date":datetime.date(2015,12,21), "week":15},
    {"start_date":datetime.date(2015,12,22), "end_date":datetime.date(2015,12,28), "week":16},
    {"start_date":datetime.date(2015,12,29), "end_date":datetime.date(2015,1,4), "week":17}
]

def get_game_week(date):
    for week in GAME_WEEKS:
        if date >= week['start_date']:
            if date <= week['end_date']:
                return week
    return None

class BaseModelClass(object):

    DATA_DIRECTORY = os.path.join(os.path.realpath(__file__).split(__file__.split('/')[-1])[0], 'data')

    def set_data_directory(self):
        if not os.path.exists(self.DATA_DIRECTORY):
            os.system('mkdir -p %s' % self.DATA_DIRECTORY)


class DataModelClass(BaseModelClass):

    def set_fields(self, **kwargs):
        fieldnames = self.__dict__.keys()
        for k,v in kwargs.items():
            k = k.lower().strip()
            if k in fieldnames:
                setattr(self, k, v)

    def __repr__(self):
        return self.__unicode__()

    def __str__(self):
        return self.__unicode__()
