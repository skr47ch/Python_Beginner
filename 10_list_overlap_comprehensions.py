a = [2, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

# answer  using set
print(set(a) & set(b))

# answer using list
for x in a:
    if x in b and x not in c:
        c.append(x)

print(c)
