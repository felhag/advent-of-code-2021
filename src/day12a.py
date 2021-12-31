input = '''xx-end
EG-xx
iy-FP
iy-qc
AB-end
yi-KG
KG-xx
start-LS
qe-FP
qc-AB
yi-start
AB-iy
FP-start
iy-LS
yi-LS
xx-AB
end-KG
iy-KG
qc-KG
FP-xx
LS-qc
FP-yi'''

nodes = [line.split('-') for line in input.splitlines()]
completed = []


def other(current, node):
    return node[1 if node.index(current) == 0 else 0]


def find_next(current, visited):
    connected = filter(lambda node: current in node, nodes)
    for connect in connected:
        next_cave = other(current, connect)

        if next_cave == 'start':
            continue
        elif next_cave == 'end':
            completed.append(visited[:] + [next_cave])
        elif next_cave not in visited or next_cave.isupper():
            find_next(next_cave, visited[:] + [next_cave])


find_next('start', ['start'])


print(f'Completed {len(completed)} paths:')
for c in completed:
    print(c)
