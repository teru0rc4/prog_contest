<!-- 画像挿入についてhttp://cartman0.hatenablog.com/entry/2015/03/31/164836 -->
## AtCoder Beginner Contest 039 memo
1. [結果](#intro)
1. [A 高橋直体](#anchor1)
1. [B エージェント高橋君](#anchor2)
1. [C ピアニスト高橋君](#anchor3)
1. [D 画像処理高橋君](#anchor4)
1. [おわりに](#outro)

<a id="intro"></a>
#### <a href="#intro">結果</a>
「A 高橋直体」, 「B エージェント高橋君」は解けた.
「C ピアニスト高橋君」で沼った挙句, 制約を見逃す悲しみ.
「D 画像処理高橋君」は問題すら見れませんでした……気づいたら2時間終わってたよ.
次回以降は頑張りましょう.

<a id="anchor1"></a>
#### <a href="#anchor1">A 高橋直体</a>
問題は[こちら](http://abc039.contest.atcoder.jp/tasks/abc039_a).

特にいう事はなく標準入力受け取って演算するだけ.~~標準入力普段使わないので, 一瞬「えっ」ってなりました.~~
``` python
# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
a, b, c = map(int, raw_input().split())
# 出力
print str(a*b*2+b*c*2+c*a*2)
```


<a id="anchor2"></a>
#### <a href="#anchor2">B エージェント高橋君</a>
問題は[こちら](http://abc039.contest.atcoder.jp/tasks/abc039_b).

4乗する前の値を求めればよい. 範囲が10^9なので, Nの候補は1~177まで調べれば十分.
それとも普通に1/4乗できたりするのか？
``` python
-*- coding: utf-8 -*-
x = int(raw_input())
for n in range(1,178):
    if x == n**4:
        break
print str(n)
```

<a id="anchor3"></a>
#### <a href="#anchor3">C ピアニスト高橋君</a>
問題は[こちら](http://abc039.contest.atcoder.jp/tasks/abc039_c).

やっちゃった系の問題. 問題の制約を正しく理解できていないせいで色々沼った…….
ここにきて実行時間とか性能が気になってきてしまい,
入力文字のうち4,5文字調べて場所がわかればかなり効率よさそうと, 欲張った結果, 「高橋君は白鍵盤にいる」という情報をすっかり忘れてしまった.

備忘録として, 公式で解説していた実装に従ってのpythonコードを記述しておく.
``` python
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

```

<a id="anchor4"></a>
#### <a href="#anchor4">D 画像処理高橋君</a>
問題は[こちら](http://abc039.contest.atcoder.jp/tasks/abc039_d).

全　く　見　て　な　か　っ　た.
余裕ないなー, 次回は気を付けます.

そのうち公式のやり方実装します.

<a id="outro"></a>
#### <a href="#outro">おわりに</a>
標準入力周りとかが弱いので, 次回までにその辺をまとめて確認しておきたいです.
