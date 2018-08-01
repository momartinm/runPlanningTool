#!/usr/bin/env python

class Planner(object):
    def __init__(self, repo, folder):
        self.repo = repo
        self.folder = folder

    def getRepo(self):
        return self.repo

    def getFolder(self):
        return self.folder


def read_planners_from_file(file_path, names):
    planners = {}
    planners_file = open(file_path, 'r')

    for line in planners_file:
        if len(line) > 1 and line[0] is not '#':
            features = line.split(',')
            if (len(features) == 3):
                key = features[0]
                if names is None or key in names:
                    if (not planners.has_key(key)):
                        planners[key] = Planner(features[1], features[2])

    planners_file.close()

    return planners

ALL_PLANNERS = {
    "OPTIC-Base": Planner("", "OPTIC-Base"),
}
