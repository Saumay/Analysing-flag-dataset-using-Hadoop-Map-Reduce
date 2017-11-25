import random
import bisect
import collections

def choice(population, weights):
    assert len(population) == len(weights)
    x = random.random()
    idx = bisect.bisect(cdf_vals, x)
    #print(population[idx])
    return population[idx]

weights=[0.1, 0.1, 0.1]
population = 'ABC'
counts = collections.defaultdict(int)
for i in range(10000):
    print(choice(population, weights))
    counts[choice(population, weights)] += 1

print(counts)
