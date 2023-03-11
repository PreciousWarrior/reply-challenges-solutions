def dist(p1, p2):
    [x1, y1] = p1
    [x2, y2] = p2
    return abs(x1-x2) + abs(y1-y2)


def get_min_dist(n, flowers):
    print(flowers)
    minimum = 2*(n-1)
    for i in flowers:
        for j in [x for x in flowers if x!=i]:
            if dist(i, j) < minimum:
                minimum = dist(i, j)
    return minimum

def min_dist_flower(n, flowers, flower):
    minimum = 2*(n-1)
    for f in [x for x in flowers if x!=flower]:
        if dist(flower, f) < minimum:
            minimum = dist(flower, f)
    return minimum

def find_optimum_relocation(n, patches, flowers, flower):
    maxmin = get_min_dist(n, flowers)
    relocation_point = flower
    for i in range(0, n**2):
        x = i%n
        y = i//n
        if [x, y] not in patches or [x, y] in flowers:
            continue
        minimum_dist = min_dist_flower(n, flowers, [x, y])
        if minimum_dist > maxmin: 
            maxmin = minimum_dist
            relocation_point = [x, y]
    return relocation_point

def find_maxmin(n, n_flowers, patches):
    flowers = []
    # Fill in the flowers
    i = 0
    while len(flowers) < n_flowers:
        x = i%n
        y = i//n
        if [x, y] in patches:
            flowers.append([x, y])
        i += 1
    k = 0
    while True:
        k+=1
        relocated_one = False
        for flower in flowers:
            relocation_point = find_optimum_relocation(n, patches, flowers, flower)
            if relocation_point != flower:
                relocated_one = True
            flowers[flowers.index(flower)] = relocation_point
        if not relocated_one:
            break
    return get_min_dist(n, flowers)

n = 5
patches = [
[0, 0],
[0, 1],
[0, 2],
[0, 4],
[1, 0],
[1, 4],
[2, 1],
[2, 3],
[3, 0],
[3, 1],
[3, 2],
[3, 4],
[4, 2],
[4, 3],
[4, 4]]

n_flowers = 4

print(find_maxmin(n, n_flowers, patches))
