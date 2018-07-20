import os
import csv

def getResultsForPlanner(planner):

    DEFAULT_PATH = os.getcwd()+"/results/"
    plannerResults = {}

    if not os.path.isdir(DEFAULT_PATH+planner):
        print("This is not a valid planner!")

    else:
        domains = [d for d in os.listdir(DEFAULT_PATH+planner) if os.path.isdir(os.path.join(DEFAULT_PATH+planner, d))]

        for domain in domains:
            print(domain)

            domainResults = {}
            problems = [d for d in os.listdir(DEFAULT_PATH+planner+"/"+domain) if os.path.isdir(os.path.join(DEFAULT_PATH+planner+"/"+domain, d))]

            for problem in problems:

                logFiles = [f for f in all_files(DEFAULT_PATH+planner+"/"+domain+"/"+problem)
                             if f.endswith('.log')]

                domainResults[problem] = getProblemResults(problem, returnLog(logFiles))

            plannerResults[domain] = domainResults

            makeResultsCSV(DEFAULT_PATH+planner+"/"+domain+"/results.csv", domainResults)

        coverageList =[]
        for key, res in plannerResults.iteritems():
            coverage = 0

            for key2, problem in res.iteritems():
                coverage += problem[9]

            coverageList.append([key, coverage])


        with open(DEFAULT_PATH + planner + "/coverage.csv", "wb") as r:
            wr = csv.writer(r, quoting=csv.QUOTE_ALL)
            wr.writerow(["Domain", "Coverage"])
            for row in coverageList:
                wr.writerow(row)



def makeResultsCSV(path, domainResults):

    with open(path, "wb") as r:
        wr = csv.writer(r, quoting=csv.QUOTE_ALL)
        wr.writerow(["Problem","Plan length","Expanded","Reopened","Evaluated", "Generated","Dead ends","Search time","Total time","Solution found"])
        for key, value in domainResults.iteritems():
            wr.writerow(value)



def returnLog(path):

    with open(path[0], "r") as f:
        searchLines = f.readlines()
    return searchLines



def getProblemResults(problem, logFile):

    solution = [problem,-1,-1,-1,-1,-1,-1,-1,-1,0]

    for i, line in enumerate(logFile[-30:]):
        lineSpit = line.split(' ')
        if "Plan length:" in line:
            solution[1] = int(lineSpit[2])
        elif ("Expanded" in line) and not ("until" in line):
            solution[2] = int(line[9:-11])
        elif ("Reopened" in line) and not ("until" in line):
            solution[3] = int(line[9:-11])
        elif ("Evaluated" in line) and not ("until" in line):
            solution[4] = int(line[10:-11])
        elif ("Generated" in line) and not (("until" in line) or ("rules" in line)):
            solution[5] = int(line[10:-11])
        elif "Dead ends" in line:
            solution[6] = int(line[11:-11])
        elif "Search time" in line:
            solution[7] = float(line[13:-2])
        elif "Total time" in line:
            solution[8] = float(line[13:-2])
        elif "Solution found" in line:
            solution[9] = 1

    return solution




def all_files(directory):
    for path, dirs, files in os.walk(directory):
        for f in files:
            yield os.path.join(path, f)


#getResultsForPlanner("Complementary1")