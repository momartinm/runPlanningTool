# runPlanningTool

Planning tool to run planners and domains creating singularity containers. This tool is based on the code from Florian Pommerening. This tool needs to be configure to work into the correct way. 

### Prerequisites



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

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
* Florian Pommerening
