# 標準入出力のテンプレまとめ
python3に以降した関係で旧テンプレが使用できなくなったので, これを機に新しく書き直してまとめることとする.
(参考 : [Python3で標準入出力（競技プログラミング用](http://qiita.com/chuck0523/items/8e703a307333f91c209f))
### テストコードテンプレ
ローカルにあるフォルダを対w象に、その中にあるファイルの内容を標準出力にして、テストを行う.
`solve()`の中身を実際のコードにすればよいぞ.
`**********`は対象のフォルダへのpathを書くべし.

``` python
# -*- coding: utf-8 -*-
import sys
import os

##### solveの中に書く!!
def solve():
    a, b, c = list(map(int, input().split()))
    print('%s' % str(a*b*2+b*c*2+c*a*2))

test_path = '**********'
FILES = os.listdir(test_path)
print('%s' % FILES)
for FILE in FILES:
    fdr = os.open(test_path + '/' + FILE, os.O_RDONLY)
    os.dup2(fdr, sys.stdin.fileno())
    solve()

print("finish")
```

### 入力が1行で1つだけの場合
#### 文字・文字列
`input`
```
S
```
Sは文字列
``` python
s = input()
```
#### 数値(整数または浮動小数点数)
`input`
```
N
```
Nは整数または浮動小数点数.
``` python
n = int(input()) # 整数
n = float(input()) # 浮動小数点数
```

- `raw_input()`が削除され, `input()`に一本化された
  - python2では, 文字列は`row_input()`であった
- 数値を`input()`する場合は, それぞれの状態に応じてキャストしてやる必要がある.
  - 小数点数を`int`でキャストすると値が切れるので注意

### 入力が1行で複数ある場合
#### 文字・文字列
`input`
```
A B C
```
A,B,Cはいずれも文字列
``` python
s = input().split()
a, b, c = input().split()
```
- 分割された文字列は`input().split()`でOK
  - 異なる変数に代入したい場合は`a,b,c`のようにすれば, スペース区切りで各変数に入力される.

#### 数値(整数または浮動小数点数)
`input`
```
A B C
```
A,B,Cはいずれも整数または浮動小数点数.
``` python
n = list(map(int, input().split())) # 整数
n = list(map(float, input().split())) # 浮動小数点数
n1, n2, n3 = list(map(int, input().split())) # 整数
n1, n2, n3 = list(map(float, input().split())) # 浮動小数点数
```
- python2の頃と見た目はそんなに変わらないが実態が異なる
  - 前は`map(int, raw_input().split()`であった
  - その原因は`map`の仕様変更である
    - map objectを返すようになり, 以前のようにlistを直接返してくれなくなった.
    - 参考 : [Python3でmapがmap objectを返す（ようになった）件](http://swimmingpython.net/ja/?p=565)

### 入力が複数行で1つずつ与えられる場合
#### 最初に入力する個数(N)が与えられて, そこからN個の入力が与えられる場合
`input`
```
N
a1
a2
...
aN
```
a1,a2,...,aNはN個の入力.
``` python
N = int(input())
a = []
for i in range(N):
  a.append(input())
```
あるいは
``` python
N = int(input())
a = [input() for i in range(N)]
```
- まず個数Nを受け取って, そのあとN個の入力を格納する
- listの内包表記を使うと美しい……
  - `int`で取り扱いたいなら`input()`をキャストすること

#### 終了フラグが来るまで入力を格納し続ける
``` python
a = []
while True:
    num = input()
    if num == -1: # 終了フラグ
        break
    a.append(num)
```
- 判定の部分を文字か数字かでわしゃわしゃする必要はある
  - EOFの場合はどうすればいいんですかね……

### 入力が複数行にわたって複数与えられる場合
`input`
```
N M
a11 a12 a13 ... a1M
a21 a22 a23 ... a2M
a31 a32 a33 ... a3M
...
aN1 aN2 aN3 ... aNM
```
``` python
N, M = list(map(int, input().split())) # 整数
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
```
