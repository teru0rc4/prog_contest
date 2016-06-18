# n = int(raw_input())
# a = map(int, raw_input().split())
n = 9
a = [314, 159, 265, 358, 979, 323, 846, 264, 338]

n = int(raw_input())
a = map(int, raw_input().split())
b=[]
b.append(0)
b.append( abs(a[0]-a[1]) )
if n!=2 :
    count=2
    while count<n:
        if (b[count-1]+ abs(a[count]-a[count-1])) < (b[count-2]+ abs(a[count]-a[count-2])) :
            b.append( b[count-1]+ abs(a[count]-a[count-1]) )
        else:
            b.append( b[count-2]+ abs(a[count]-a[count-2]) )
        count += 1
print str(b[n-1])
