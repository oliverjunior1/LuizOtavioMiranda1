class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufaturator= None

    @property
    def engine(self):
        return self._engine
    
    @engine.getter
    def engine(self, value):
        self._engine = value
        
    @property
    def manufaturator(self):
        return self._manufaturator
    
    @manufaturator.getter
    def manufaturator(self, value):
        self._manufaturator = value
        
class Engine:
    def __init__(self, name):
        self.name = name

class Manufaturator:
    def __init__(self, name):
        self.name = name

fusca = Car('Fusca')
engine_1_0 = Engine('1.0')
volkswagen = Manufaturator('Volkswagen')
fusca.engine= engine_1_0
fusca.manufaturator = volkswagen

print(fusca.engine.name, fusca.name, fusca.manufaturator.name)


