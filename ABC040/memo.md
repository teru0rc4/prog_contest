<!-- 画像挿入についてhttp://cartman0.hatenablog.com/entry/2015/03/31/164836 -->
## AtCoder Beginner Contest 039 memo
1. [結果](#intro)
1. [A 赤赤赤赤青](#anchor1)
1. [B □□□□□](#anchor2)
1. [C 柱柱柱柱柱](#anchor3)
1. [D 道路の老朽化対策について](#anchor4)
1. [おわりに](#outro)

<a id="intro"></a>
#### <a href="#intro">結果</a>
「A 赤赤赤赤青」, 「B □□□□□」, 「C 柱柱柱柱柱」は解けた.
「D 道路の老朽化対策について」は問題といて, 半分くらいまで書いて「あれこれだと……」ってケースが見つかってダメでした.~~まぁ調べたところ, 少し改良すれば行けたらしい…?~~

D問題についてありがたいお話をいただいたので, それについても今回は追記する.

<a id="anchor1"></a>
#### <a href="#anchor1">A 赤赤赤赤青</a>
問題は[こちら](http://abc040.contest.atcoder.jp/tasks/abc040_a).

特にいう事はない. 小さいほうから数えるのと、大きい方から数えるのどっちのがいいのというお話.
``` python
n, x = map(int, raw_input().split())
if x > (n/2):
    print str(n-x)
else:
    print str(x-1)
 ```

と以下そこまで考えられているなら, min使った方が効率的じゃないか?と思った.~本番でそういう風に思考が置き換えられる余裕がまだない~
``` python
n, x = map(int, raw_input().split())
print str(min(n-x,x-1))
 ```


<a id="anchor2"></a>
#### <a href="#anchor2">B □□□□□</a>
問題は[こちら](http://abc040.contest.atcoder.jp/tasks/abc040_b).

正方形を意識して、あとはそこから足りない辺と, 補った時縦横の差の小さい方をとればよい
``` python
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
```

というかこれもmin使った方がいいし、なぜ同じサイズのwhileをに買いまわしたのか理解に苦しむ……
``` python
n = int(raw_input())
x = 1
num = n
while (x+1)**2 <= n:
    y = n/x
    z = n%x
    if num > y-x+z:
        num = (y-x+z)

    x +=1
print str(num)
```


<a id="anchor3"></a>
#### <a href="#anchor3">C 柱柱柱柱柱</a>
問題は[こちら](http://abc040.contest.atcoder.jp/tasks/abc040_c).

グラフチックな問題.
ある柱から見て, 1つ手前からと, 2つ手前から,どちらの方が移動コストが小さいかを計算し, 最初の柱から順に最小コストの移動を考えてやればよい

``` python
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
 ```

だからmin使えよ!!!!
``` python
n = int(raw_input())
a = map(int, raw_input().split())
b=[]
b.append(0)
b.append( abs(a[0]-a[1]) )
if n!=2 :
    count=2
    while count<n:
            b.append( min(b[count-1]+ abs(a[count]-a[count-1]),b[count-2]+ abs(a[count]-a[count-2]) ) )
        count += 1
print str(b[n-1])
 ```

サイズがわかっているならリストのappendではなく,それだけ準備した方がいいかもしれない


<a id="anchor4"></a>
#### <a href="#anchor4">D 道路の老朽化対策について</a>
問題は[こちら](http://abc040.contest.atcoder.jp/tasks/abc040_d).
途中まで書いて、あああああってなってやめた.
どうやら、もう少し改良すれば行けたらしい?

これに関してありがたいいくつかのリンクをいただいたので, それについても
- http://algs4.cs.princeton.edu/lectures/15UnionFind.pdf
- http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A&lang=jp 


<a id="outro"></a>
#### <a href="#outro">おわりに</a>
余裕がなくて忙しい><
