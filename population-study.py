def population(data,repeated=[]):
    for i in range(len(data)):
        k = i + 1
        for j in range(k,len(data)):
            if data[i] == data[j] and data[i] not in repeated:
                repeated.append(data[i])
    return min(repeated)

print(population([1,1,1,2,2,3,3,3,4,5]))
