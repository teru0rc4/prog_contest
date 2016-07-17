# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に書く!!
def solve():
    a, b, c = list(map(int, input().split()))
    print('%s' % str(a*b*2+b*c*2+c*a*2))


test_path = '*****'
FILES = os.listdir(test_path)
print('%s' % FILES)
for FILE in FILES:
    fdr = os.open(test_path + '/' + FILE, os.O_RDONLY)
    os.dup2(fdr, sys.stdin.fileno())
    solve()

print("finish")
