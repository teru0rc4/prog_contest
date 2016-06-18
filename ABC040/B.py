n = int(raw_input())
x = 1
while (x+1)**2 <= n:
    x += 1
num = n

while x>=1:
    y = n/x
    z = n%x
    if num > y-x+z:
        num = (y-x+z)

    x -=1
print str(num)
