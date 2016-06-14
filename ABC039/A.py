# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
a, b, c = map(int, raw_input().split())
# 出力
print str(a*b*2+b*c*2+c*a*2)
