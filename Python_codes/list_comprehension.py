print([[x,y] for x in [1,2,3] for y in [2,3,4]])
results =[]
for x in [1,2,3]:
    for y in [2,3,4]:
        results.append([x,y])

print(results)