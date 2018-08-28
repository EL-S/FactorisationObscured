from math import *
t = int(input("number: "))
z = t**(1/2)
p = z%1
f = []
e = 3
s = 2
if t%2 == 0:
    e = 2
    s = 1
if p != 0:
    y = floor(z)
else:
    print("perfect square")
    y = int(z) + 1
q = int(t/2) + 1
print("1","x",t)
for j in range(e,y,s):
    d = (t/j);
    if (t%j) != 0:
        continue
    for k in range(e,q,s):
        if j*k == t:
            print(j,"x",k)
            h = [j,k]
            f.append(h)
            break
if not f:
    f.append([1,t])
    print("prime")

else:
    f.append([1,t])
    print(f)
print("finished")
