import os
import importlib
import inspect
from glob import glob

class ReportNameMapper:
    def __init__(self):
        self.classes = {}

        for file in glob("report_generator/**/*.py", recursive=True):
            if file.endswith("__init__.py"):
                continue

            module_path = file.replace("/", ".").replace("\\", ".")
            module_name = os.path.splitext(module_path)[0]

            module = importlib.import_module(module_name)

            for name, obj in inspect.getmembers(module, inspect.isclass):
                if obj.__module__ == module_name and hasattr(obj, 'name'):
                    if obj.name in self.classes:
                        raise KeyError('The name ', obj.name, ' exists in both classes', self.classes[obj.name], ' and ', module_path)
                    self.classes[obj.name] = obj

    def keyExists(self, key):
        return key in self.classes

    def getKey(self, key):
        return self.classes.get(key)
