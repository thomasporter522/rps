import itertools


def generate(n):

    def p(grid):
        for r in grid: print("".join([str(i) for i in r]))
        print("")

    if n == 0 or n == 1: 
        re = [[[0]]]*n
        if n: p(re[0])
        return re

    grid = [[int(i < j) for j in range(n)] for i in range(n)]
    position = (0,1)

    def increment(position):
        if position[1] < n-1: return (position[0],position[1]+1)
        if position == (n-2, n-1): return None
        return (position[0]+1, position[0]+2)

    def swap(grid, position):
        grid[position[0]][position[1]] = 1-grid[position[0]][position[1]]
        grid[position[1]][position[0]] = 1-grid[position[1]][position[0]]

    def interesting(grid):
        for i in range(n):
            for j in range(i+1,n):
                over = True
                under = True
                for l in range(n):
                    over = over and grid[i][l] >= grid[j][l]
                    under = under and grid[i][l] <= grid[j][l]
                if over or under: return False
        return True

    def rec(grid, position):
        if position == None: 
            if interesting(grid): return [ [[grid[i][j] for j in range(n)] for i in range(n)] ]
            else: return []
        else:
            re = rec(grid, increment(position))
            swap(grid, position)
            return re + rec(grid, increment(position))

    results = rec(grid, position)

    def permute(grid, perm): return [[grid[perm[i]][perm[j]] for j in range(n)] for i in range(n)]

    new_results = []
    for i in range(len(results)):
        redundant = False
        for perm in itertools.permutations([i for i in range(n)]):
            permuted = permute(results[i], perm)
            for previous in new_results:
                if permuted == previous: 
                    redundant = True
                    break
        if not redundant: 
            p(results[i])
            new_results += [results[i]]
    return new_results

for i in range(8,9):
    print(i,"has", len(generate(i)), "games.\n")
