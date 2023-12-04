from functools import reduce
import operator
# A slightly efficient superset of primes.
def PrimesPlus():
  yield 2
  yield 3
  i = 5
  while True:
    yield i
    if i % 6 == 1:
      i += 2
    i += 2
# Returns a dict d with n = product p ^ d[p]
def GetPrimeDecomp(n):
  d = {}
  primes = PrimesPlus()
  for p in primes:
    while n % p == 0:
      n /= p
      d[p] = d.setdefault(p, 0) + 1
    if n == 1:
      return d
def NumberOfDivisors(n):
  d = GetPrimeDecomp(n)
  powers_plus = map(lambda x: x+1, d.values())
  print(d)
  return reduce(operator.mul, powers_plus, 1)



def generate_candidates(pole):
    if len(pole) == 0:
        return []
    if len(pole) == 1:
        return [pole[0]]
    t = generate_candidates(pole[1:])
    return [pole[0]] + t + [i*pole[0] for i in t]
    
        
def create_candidates(dic):
    res = []
    for k,v in dic.items():
        for i in range(v):
            res.append(k)
    return res

house = 831600
def get_presents(elves, house):
    ret = 0
    for elf in elves:
        if elf*50 > house:
            ret+= elf*11
    return ret
pres = 0
while (True or pres<34000000):
    dic = GetPrimeDecomp(house)
    cand = create_candidates(dic)
    all = set(generate_candidates(cand))
    pres = get_presents(all, house)
    if house%10000 == 0:
        ""
        print(f'Walkit: house {house},presents {pres}')
    if pres>=34000000:
        print(f'Over: house {house},presents {pres}')
    house-=1
print(house-1,pres)
    