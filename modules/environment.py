import os
from modules.module import Module


class EnvironmentDump(Module):
    def run(self, **args):
        print("[*] Starting environment dump module.")
        return str(os.environ)