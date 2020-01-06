from modules.dirlister import DirectoryLister
from modules.environment import EnvironmentDump

runnable_modules = [DirectoryLister(), EnvironmentDump()]
for module in runnable_modules:
    print(module.run())