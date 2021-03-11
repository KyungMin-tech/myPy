# 그래프 탐색 알고리즘

def bfs(g, start):
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d+1))
                done.add(x)

g = {
    1 : [2, 3],
    2 : [1, 4, 5],
    3 : [1],
    4 : [2],
    5 : [2]
}

bfs(g, 1)

# 1 2 3 4 5
