# 친구의 친구 찾기

def print_all_friends(g, start):
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu:
        (p, d) = qu.pop(0)
        print(p, d)
        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)
    
fr_info = {
	"Summer" : ["John", "Justine", "Mike"],
	"John" : ["Summer", "Justine"],
	"Justine" : ["John", "Summer", "Mike", "May"],
	"Mike" : ["Summer", "Justine"],
	"May" : ["Justine", "Kim"],
	"Kim" : ["May"],
	"Tom" : ["Jerry"],
	"Jerry" : ["Tom"]
}

print_all_friends(fr_info, "Summer")
print()
print_all_friends(fr_info, "Jerry")
