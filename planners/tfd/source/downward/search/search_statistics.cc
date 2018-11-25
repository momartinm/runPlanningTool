#include "search_statistics.h"
#include "globals.h"
#include <stdio.h>
#include <stdlib.h>

SearchStatistics::SearchStatistics()
{
    generated_states = 0;

    lastDumpClosedListSize = 0;
    lastDumpGeneratedStates = 0;
    lastDumpTime = time(NULL);
    startTime = lastDumpTime;
}

SearchStatistics::~SearchStatistics()
{
}

void SearchStatistics::countChild(int openListIndex)
{
    generated_states++;
    childrenPerOpenList[openListIndex]++;
}

void SearchStatistics::finishExpansion()
{
    int numChildren = 0;
    for(std::map<int, int>::iterator it = childrenPerOpenList.begin(); it != childrenPerOpenList.end(); it++) {
        std::map<int, Statistics<double> >::iterator statIt = branchingFactors.find(it->first);
        if(statIt == branchingFactors.end()) {
            char* buf = new char[1024];
            sprintf(buf, "Open List %d", it->first);
            branchingFactors[it->first] = Statistics<double>(buf);
        }
        branchingFactors[it->first].addMeasurement(it->second); // count
        numChildren += it->second;
        it->second = 0; // reset for next expansion
    }
    overallBranchingFactor.addMeasurement(numChildren);
}

int SearchStatistics::parseLine(char* line){
    // This assumes that a digit will be found and the line ends in " Kb".
    int i = strlen(line);
    const char* p = line;
    while (*p <'0' || *p > '9') p++;
    line[i-3] = '\0';
    i = atoi(p);
    return i;
}

int SearchStatistics::getValue(){ //Note: this value is in KB!
    FILE* file = fopen("/proc/self/status", "r");
    int result = -1;
    char line[128];

    while (fgets(line, 128, file) != NULL){
        if (strncmp(line, "VmRSS:", 6) == 0){
            result = parseLine(line);
            break;
        }
    }
    fclose(file);
    return result;
}

void SearchStatistics::dump(unsigned int numberOfExpandedNodes, time_t & current_time)
{
    double dt = current_time - lastDumpTime;
    double dTotal = current_time - startTime;

    cout << "Memory : " << getValue() << " in Kbs " << endl;
    cout << "Expanded Nodes: " << numberOfExpandedNodes << " state(s)." << endl;
    double dClosedList = numberOfExpandedNodes - lastDumpClosedListSize;
    printf("Rate: %.1f Nodes/s (over %.1fs) %.1f Nodes/s (total average)\n", dClosedList/dt, dt,
            double(numberOfExpandedNodes)/dTotal);

    cout << "Generated Nodes: " << generated_states << " state(s)." << endl;
    double dGeneratedNodes = generated_states - lastDumpGeneratedStates;
    printf("Rate: %.1f Nodes/s (over %.1fs) %.1f Nodes/s (total average)\n", dGeneratedNodes/dt, dt,
            double(generated_states)/dTotal);

    cout << "Overall branching factor by list sizes: " << (generated_states / (double) numberOfExpandedNodes) << endl;
    printf("Averaged overall branching factor: ");
    overallBranchingFactor.print();
    printf("Branching factors by open list:\n");
    for(std::map<int, Statistics<double> >::iterator it = branchingFactors.begin();
            it != branchingFactors.end(); it++) {
        it->second.print();
    }

    lastDumpGeneratedStates = generated_states;
    lastDumpClosedListSize = numberOfExpandedNodes;
    lastDumpTime = current_time;
}

