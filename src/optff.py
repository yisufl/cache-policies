def optff(k : int, rm : list):

    misses = 0

    cache = []

    for i, r in enumerate(rm):
        if r in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.append(r)
            continue

        farthest = -1
        remove = -1

        for j, cached in enumerate(cache):
            try:
                nextUsed = rm[i+1:].index(cached)
            except ValueError:
                remove = j
                break

            if nextUsed > farthest:
                farthest = nextUsed
                remove = j

        cache[remove] = r
    
    return misses