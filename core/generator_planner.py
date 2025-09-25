from config import GENERATORS
from core.arguments import Arguments
from core.report_name_mapper import ReportNameMapper

class GeneratorPlanner():
    plannedStubs = []

    def __init__(self):
        self.stubs = sorted(GENERATORS)
        self.args = Arguments().getArgs()
        self.mapper = ReportNameMapper()


    def getStubs(self):
        if(self.args.O):
            mappedClass = self.__tryMapClass(self.args.O)
            self.plannedStubs.append(mappedClass)
        else:
            for stub in self.stubs:
                mappedClass = self.__tryMapClass(stub)
                self.plannedStubs.append(mappedClass)


        return self.plannedStubs

    def __tryMapClass(self, value):
        if (not self.mapper.keyExists(value)):
            raise ValueError('There is no parts called ', value)
        return self.mapper.getKey(value)
