import random
import bisect
import collections

def cdf(weights):
    total = sum(weights)
    result = []
    cumsum = 0
    for w in weights:
        cumsum += w
        result.append(cumsum / total)
    return result

def choice(population, weights):
    assert len(population) == len(weights)
    cdf_vals = cdf(weights)
    x = random.random()
    idx = bisect.bisect(cdf_vals, x)
    return population[idx]

weights=[0.5, 0.6, 0.1]

population = 'ABC'
counts = collections.defaultdict(int)
for i in range(10000):
    print(choice(population, weights))
    counts[choice(population, weights)] += 1
print(counts)
