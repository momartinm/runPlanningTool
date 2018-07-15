# runPlanningTool

Planning tool to run planners and domains creating singularity containers. This tool is based on the code from Florian Pommerening. This tool needs to be configure to work into the correct way. 

### Prerequisites

Installing basic tools:

```
sudo apt-get install python-setuptools python-dev build-essential python-pip libtool libarchive-dev git-all
sudo pip install --upgrade virtualenv 
```

Installing singularity:

This repo includes a version of singularity. Then it is not necessary to clone the master repo. 

```
git clone https://github.com/singularityware/singularity.git
cd singularity
./autogen.sh
./configure --prefix=/usr/local
make
sudo make install
```

Installing virtualbox from repository:

```
sudo apt-get install virtualbox-5.1
```

Installing vagrant:

```
sudo apt-get install vagrant
pip install python-vagrant
```

Installing val (PDDL validator):

Val is a tool to validate the plans generate by a planner. A compile version is include to the repo at the main folder. But, I recomend to download and compile a new version.

```
cd val
make
mv validate ../
```

### Configuring the benchmarks

It is necesary to configure the different benchmarks which are going to be executed. The file benchmarks_files.py must be tunned by the user in order to include the different domains and problems which must be executed. A list of the different instances must be created for each domain, following the next example:

```
CUSHING_BENCHMARKS = [
    Benchmark("Cushing", "domain.pddl", "pfile1.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile3.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
]
```

Where the first name is the name of the folder where the domains and instances are stored. This folder must be created inside of the benchmarks folder. The second is the name of domain file. The third is the name of the problem file. The last three are related with the cost of solving a specific instance (These three are not available in this first version). Several domains can be defined using the next structure:

```
ALL_BENCHMARKS = {
    "cushing":CUSHING_BENCHMARKS,
}
```

### Configuring the plannes

After this, it is necesary to configure the different planners which are going to be used to solve the different benchmarks. The file planners.py must be tunned by the user in order to include the different planners. A dict with the planners must be created following the next example:

```
ALL_PLANNERS = {
    "OPTIC-Base": Planner("", "OPTIC-Base"),
}
```

Where the index is the name of the planner, the second is the url to repository where the planner is stored (this option is not available yet) and the third is the name of the folder where the source code of the planner is stored. 

### Configuring the validation system

We must configurate the validation process depending if we are going to use temporal or classical domain. The variable TEMPORAL_DOMAINS can be tunned to support temporal or classical validation. For classical validation its value must be false. 

```
TEMPORAL_DOMAINS = False
```


### How to use

Finally the code can be executed using the python program called run_benchmarks.py. This program will executed each domain for each planner ff the program is running without any parameters. 

```
 run_benchmarks.py
```

But, it is possible to choose the domains and planners which are going to be executed. The next example, it is only going to executed the domain cushing using the planner Optic.  

```
 run_benchmarks.py OPTIC-Base cushing
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
* Florian Pommerening
