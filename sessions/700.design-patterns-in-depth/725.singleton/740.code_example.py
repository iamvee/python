class SingletonMeta(type):

    _instance = None
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance

class Singleton(metaclass=SingletonMeta):
	
    def some_logic(self):
        pass



if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print('Singleton works')
    else:
        print('singleton failed')
 
