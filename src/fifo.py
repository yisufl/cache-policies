from collections import deque

def fifo(k : int, m : int, rm : list) -> int:
    
    misses = 0

    cache = deque()
    items = set()

    for r in rm:
        if r in items:
            continue

        misses += 1

        if len(cache) >= m:
            oldest = cache.popleft()
            items.remove(oldest)

        cache.append(r)
        items.add(r)

    return misses