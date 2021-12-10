crabs = [int(i) for i in open("AOC_txt_7").read().split(',')]
print(min([sum([abs(crab-k) for crab in crabs]) for k in range(1950)]))
print(min([sum([abs(crab-k)*(abs(crab-k)+1)//2 for crab in crabs]) for k in range(1950)]))
