import os
import time


class Watch:
    def __init__(self, repo):
        self.file = f'images/{repo}/captions.js'
        self._stamp = 0

    def __start(self):


    def __check(self):
        try:
            stamp = os.stat(self.file).st_mtime
            if stamp != self._stamp:
