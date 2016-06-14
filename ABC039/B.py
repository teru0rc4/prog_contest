# -*- coding: utf-8 -*-
# 整数の入力 1<=x<=10^9
x = int(raw_input())
# 1<=n<=176
# 出力
for n in range(1,178):
    if x == n**4:
        break
print str(n)
