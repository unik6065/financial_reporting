import argparse

class Arguments:

    _instances = {}

    def __init__(self):
        parser = argparse.ArgumentParser(prog="financial analysis", description='Analyse a file and give back a resume',)
        parser.add_argument("financial_file", help="The path of the file that need to be analysed.", type=argparse.FileType('r', encoding='latin1'))
        parser.add_argument("--O", help="generate only one specific report part.", type=str)
        self.args = parser.parse_args()

    def __call__(self, *args, **kwds):
        if self not in self._instances:
            instance = super().__call__(*args, **kwds)
            self._instances[self] = instance
        return self._instances[self]

    def getArgs(self):
        return self.args
