def profit(machine):
    return machine[1] - machine[0]
# machines will be tuples with (cost, reward)
def find_optimal_machine(budget, machines):
    possible_machines = []
    for machine in machines:
        if machine[0] <= budget:
            possible_machines.append(machine)
    return sorted(possible_machines, key=lambda machine: profit(machine), reverse=True)[0]

def find_optimal_solution(machines, bi, bf):
    budget = bi
    i = 0
    optimal_machine = sorted(machines, key=lambda machine: profit(machine), reverse=True)[0]
    while budget < bf:
        if budget > optimal_machine[0]:
            optimal = optimal_machine
        else:
            optimal = find_optimal_machine(budget, machines)
        budget += profit(optimal)
        i += 1
    return i

lines = open("input.txt").read().split("\n")
lines = lines[1:-1]
output_lines = []
i = 0
case = 1
while i < len(lines):
    [machine_count, bf, bi] = [int(x) for x in lines[i].split(' ')]
    end = i + machine_count + 1
    machines = []
    for machineline in range(i+1, end):
        machines.append([int(x) for x in lines[machineline].split(" ")])
    output = find_optimal_solution(machines, bi, bf)
    output_lines.append(f"Case #{case}: {output}")
    i = end
    case += 1

with open("output.txt", "w") as of:
    of.write("\n".join(output_lines))
