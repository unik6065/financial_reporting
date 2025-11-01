from pathlib import Path
import re

class Generator:

    def __init__(self, stubName=None):
        self.stubName = stubName if stubName else self.name
        self.stubName = self.to_snake_case(self.stubName)
        self.p = Path(f'./stubs/{self.stubName}.md')
        self.stub = open(self.p).read()


    def replaceStub(self):
        for text in self.replace:
            self.stub = self.stub.replace('{{'+text+'}}', self.replace[text])


    def to_snake_case(self,value):
        value = re.split('(?<=.)(?=[A-Z])', value)
        return "_".join(value).lower()
