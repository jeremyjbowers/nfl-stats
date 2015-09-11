import os


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
            v = unicode(v.decode('utf-8'))
            if k in fieldnames:
                setattr(self, k, v)

    def __repr__(self):
        return self.__unicode__()

    def __str__(self):
        return self.__unicode__()