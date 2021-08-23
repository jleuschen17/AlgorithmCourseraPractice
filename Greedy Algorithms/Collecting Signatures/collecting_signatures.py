# python3

# python3
n = int(input())
lst = []

for _ in range(n):
    a, b = [int(i) for i in input().split()]
    lst.append((a,b))
lst.sort()
end_stops = []
for x in range(len(lst)):
    end_stops.append(lst[x][1])
end_stops.sort()
indexs = []
num_of_lines = 0
checker = 0
for x in range(len(lst)):
    if len(indexs) > 0:
        for y in range(len(indexs)):
            if lst[x][0] < indexs[y] and lst[x][1] > indexs[y]:
                cheker = 1
                break
        if checker == 1:
            indexs.append(lst[x][1])
            num_of_lines += 1
    else:
        indexs.append(end_stops[0])
        num_of_lines += 1


print(num_of_lines)
print(indexs)
