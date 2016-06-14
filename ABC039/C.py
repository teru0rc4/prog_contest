# -*- coding: utf-8 -*-
x = raw_input()
key = "WBWBWWBWBWBW"
key = key+key+key
ans_s = ["Do","Re","Mi","Fa","So","La","Si"]
pos = [0,2,4,5,7,9,11]
for n in range(0,7):
    if key[pos[n]:20+pos[n]] == x :
        print ans_s[n]
        break
