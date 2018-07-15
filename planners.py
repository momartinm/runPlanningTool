#!/usr/bin/env python

class Planner(object):
    def __init__(self, repo, folder):
        self.repo = repo
        self.folder = folder

    def getRepo(self):
        return self.repo

    def getFolder(self):
        return self.folder


ALL_PLANNERS = {
    "OPTIC-Base": Planner("", "OPTIC-Base"),
}
