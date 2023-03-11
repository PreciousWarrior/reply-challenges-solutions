from math import ceil

def time(length, speed, turbo_speed, turbo_cooldown, turbo_duration):
    distance = 0
    total_time = 0
    turbo_activated_already = False
    while distance < length:
        if turbo_activated_already:
            expected_distance = speed*turbo_cooldown
            if expected_distance + distance > length:
                dt = (length-distance)/speed
                return total_time + dt
            total_time += turbo_cooldown
            distance += expected_distance
            turbo_activated_already = False
        else:
            expected_distance = turbo_speed*turbo_duration
            if expected_distance + distance > length:
                dt = (length-distance)/turbo_speed
                return total_time + dt
            total_time += turbo_duration
            distance += expected_distance
            turbo_activated_already = True
    return total_time


lines = open("input.txt").read().split("\n")
lines = lines[1:-1]
output_lines = []
i = 0
case = 1
while i < len(lines):
    [length, car_count] = lines[i].split(" ")
    end = i + int(car_count) + 1
    times = []
    for carline in range(i+1, end):
        stats = [int(x) for x in lines[carline].split(" ")]
        times.append(ceil(time(int(length), stats[1], stats[2], stats[3], stats[4])))
    fastest = times.index(min(times))
    output_lines.append(f"Case #{case}: {fastest}")
    i = end
    case += 1

with open("output.txt", "w") as of:
    of.write("\n".join(output_lines))
