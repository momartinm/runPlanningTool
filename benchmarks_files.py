from benchmarks import Benchmark

CUSHING_BENCHMARKS = [
    Benchmark("Cushing", "domain.pddl", "pfile1.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile3.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile6.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile7.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile9.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile11.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile12.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile14.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile16.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
    Benchmark("Cushing", "domain.pddl", "pfile19.pddl", optimal_plan_cost_lower_bound=0, optimal_plan_cost_upper_bound=0, cost_bound=0),
]

ALL_BENCHMARKS = {
    "cushing":CUSHING_BENCHMARKS,
}