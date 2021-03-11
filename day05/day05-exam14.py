# 그래프 이용한 미로 찾기

def solve_maze(g, start, end):
    qu = [] # 앞으로 처리해야 할 이동경로
    done = set() # 이미 큐에 추가한 꼭지점 (중복방지)

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        v = p[-1] # 현재 처리해야 할 꼭지점
        if v == end:
            return p
        for x in g[v]:
            if x not in done: # 아직 큐에 추가된적없는 큐를 찾는
                qu.append(p + x)
                done.add(x)

    return "?" # 나갈 수 없는 미로

maze = {
    "a" : ["e"],
    "b" : ["c", "f"],
    "c" : ["b", "d"],
    "d" : ["c"],
    "e" : ["a", "i"],
    "f" : ["b", "g", "j"],
    "g" : ["f", "h"],
    "h" : ["g", "l"],
    "i" : ["e", "m"],
    "j" : ["f", "k", "n"],
    "k" : ["j", "o"],
    "l" : ["h", "p"],
    "m" : ["i", "n"],
    "n" : ["j", "m"],
    "o" : ["k"],
    "p" : ["l"]
}
                    

print(solve_maze(maze, 'a', 'p'))
