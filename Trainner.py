class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value

    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value


class Engine:
    def __init__(self, name):
        self.name = name

class Manufacturing:
    def __init__(self, name):
        self.name = name

fusca = Car('Fusca')
engine_1_0 = Engine('1.0')
volkswagen = Manufacturing('Volkswagen')
fusca.engine = engine_1_0
fusca.manufacturer = volkswagen
print(fusca.name, fusca.manufacturer.name, fusca.engine.name)

uno = Car('uno')
engine_1_0 = Engine('1.0')
fiat = Manufacturing('fiat')
uno.engine = engine_1_0
uno.manufacturer = fiat
print(uno.name, uno.manufacturer.name, uno.engine.name)
