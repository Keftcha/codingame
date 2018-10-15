robbers = int(raw_input())
vaults_number = int(raw_input())
time_for_vaults = []
time_by_robbers = [0 for robber in range(robbers)]
for i in range(vaults_number):
    c, n = [int(j) for j in raw_input().split()]
    time_for_vaults.append((10**n) * (5**(c - n)))

for idx in range(vaults_number):
    time_by_robbers[time_by_robbers.index(min(time_by_robbers))] += time_for_vaults[idx]
    
print(max(time_by_robbers))
