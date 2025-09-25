import importlib
import pandas as pd
# from config import GENERATORS
from core.arguments import Arguments

class GeneratorLoader():

    def generateReport(self, data: pd.DataFrame, ordered_stubs: list):
        # ordered_stubs = sorted(GENERATORS.items(), key=lambda x: x[1])

        results = []
        for stubClass in ordered_stubs:
            instance = stubClass()
            results.append(instance.generate(data))

        doc = ""

        for result in results:
            doc += result

        file = open('hello/reporting.md', 'w+')
        file.write(doc)
        file.close()
