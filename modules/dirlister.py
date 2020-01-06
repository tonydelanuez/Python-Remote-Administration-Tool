import os
from modules.module import Module


class DirectoryLister(Module):
    def run(self, **args):
        print("[*] Starting directory listing module.")
        return str(os.listdir("."))
