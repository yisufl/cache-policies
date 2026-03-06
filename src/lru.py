from collections import OrderedDict

def lru(k : int, rm : list) -> int:

    misses = 0

    cache = OrderedDict()

    for r in rm:
        if r in cache:
            cache.move_to_end(r)
            continue

        misses += 1

        if len(cache) >= k:
            cache.popitem(False)

        cache[r] = True

    return misses