def find_minimum_pairs(pairs) -> int:
    current_max, count = -1, 0
    for start, end in sorted(pairs, key=lambda x:x[1]):
        if current_max < start and start < end:
            current_max = end
            count += 1
    return count

# Input stream :
t = int(input())
for _ in range(t):
    n = int(input())
    dump = list(map(int, input().split()))
    pairs = []
    for i in range(0, n*2, 2):
        pairs.append((dump[i], dump[i + 1]))
    print(find_minimum_pairs(pairs))