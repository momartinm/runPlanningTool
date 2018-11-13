# runPlanningTool

Planning tool to run planners and domains creating singularity containers. This tool is based on the code from Florian Pommerening. This tool needs to be configure to work into the correct way. 

### Prerequisites

Installing basic tools:

```
sudo apt-get install automake python-setuptools python-dev build-essential python-pip libtool libarchive-dev bison flex
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
sudo apt-get install virtualbox
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

### Creating benchmark files

It is necessary to configure the different benchmarks in order for them to be executed. A benchmark file must be created with the information of each instance using the same sintax:

```
# DomainID |  folder  | domain file | problem file | domain folder | problem folder | lb | up | b
  AGRICOLA , agricola , domain.pddl , p01.pddl     ,               ,                , 0  , 0  , 0
```
lb: optimal plan cost lower bound
up: optimal plan cost upper bound
b: cost bound

Where the first item is the key of the domain, all the instance of a domain must use the same key, the second is the name of the folder where the domains and instances are stored. The third is the name of domain file. The fourth is the name of the problem file. The fifth is the folder of the domain file. The sixth is the folder of the problem file. The last three are related with the cost of solving a specific instance (These three are not available in this first version). Comments can be includen into the file using the character '#' at the begining of the line.


### Creating planner files

After this, it is necesary to define the different planners which are going to be used to solve the different benchmarks. A planner file must be created by the user in order to include the different planners following the next example:

```
# Planner ID | repo url | planner folder
  OPTIC-Base ,          , OPTIC-Base
```

Where the first item is the name of the planner, the second is the url to the repository (GIT, BITBUCKET) where the planner is stored (this option is not available yet) and the third is the name of the folder where the source code of the planner is stored.


### How to use

Finally the code can be executed using the python program called run_benchmarks.py. For example if we can run the full ipc 2018, we must use the same configuration

```
 run_benchmarks.py -tipc2018 -pn OPTIC-Base
```

There are different options to execute this software:

```
usage: run_benchmarks.py [-h] [-b file path] [-p file path] [-t] [-m] [-tmp] [-ipc2018]
                         [-tipc2018] [-proc cpu numbers]
                         [-pid Planner ID [Planner ID ...]]
                         [-bid Benchmark ID [Benchmark ID ...]] [--v]

```

Planning tool to run planners and domains using singularity containers. These are the different arguments:
```
-h, --help                show this help message and exit.
-b benchmarks domains     a path to the file with the information about the different benchmarks.
-p planners               a path to the file with the information about the different planners which 
                          can be executed.
-t                        a number parameter (integer) which defines the maximum execution time in seconds.
-m                        a number parameter (integer) which defines the maximun RAM memory avaliable in Gigabytes.
-tmp                      a boolean parameter which activate temporal validation.
-ipc2018                  a boolean parameter which run the benchmarks from the ipc 2018.
-tipc2018                 a boolean parameter which run the benchmarks from the temporal ipc 2018.
-proc cpu-numbers         a number parameter which defines the maximum number of cpus (threads). 
                          Default value is value is 20.
-pid [Planner ID ...]     a list parameter which defines the names of the planner which are going 
                          to be executed.
-bid [Benchmark ID ...]   a list parameter which defines the names of the benchmarks which are 
                          going to be used.
--v verbosity             increase output verbosity.
```

More will be created as we continue adding more domains.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
* Florian Pommerening
