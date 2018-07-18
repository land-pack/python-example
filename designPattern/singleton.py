class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] =  super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instances[cls]


class Logger(object):
 #   __metaclass__ = Singleton

    def __init__(self, name):
        self._name = name
    
    def name(self):
        return id(self)

if __name__ == '__main__':
    print(Logger('x').name())
    print(Logger('e').name())
    print(Logger('r').name())
    print(Logger('t').name())
