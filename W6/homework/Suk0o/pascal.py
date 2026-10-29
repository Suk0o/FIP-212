def pascal(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    L0 = pascal(n-1)
    return [1] + [L0[i] + L0[i-1] for i in range(1,n)] + [1]
def pascal_bad(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    return [1] + [pascal_bad(n-1)[i] + pascal_bad(n-1)[i-1] for i in range(1,n)] + [1]
def pascal_iter(n):
    ans0 = [1]
    for i in range(n):
        ans1 = [1]
        for j in range(1, i):
            ans1.append(ans0[j] + ans0[j-1])
        ans0 = ans1 + [1]
    return ans0
import time
#n =0,1,3,4验证皆通过
n = int(input("Enter the number of rows: "))
t0 = time.time()
a = pascal_bad(n)
t1 = time.time()
a = pascal(n)
t2 = time.time()
a = pascal_iter(n)
t3 = time.time()
print('bad pascal',t1-t0)
print('good pascal',t2-t1)
print('iterative pascal',t3-t2)
