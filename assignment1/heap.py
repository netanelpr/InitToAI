import heapq

h = []
heapq.heappush(h, (2,2))
heapq.heappush(h, (1,3))

print(heapq.heappop(h))
print(heapq.heappop(h))