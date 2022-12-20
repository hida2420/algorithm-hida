# 思いついたもの順に番号つけてくよ
# 規則性の発見、プログラム完成後のシミュレーションは
# 流石にめんどいから書かない

#問題文
#[D - Rectangles]
#https://atcoder.jp/contests/abc218/tasks/abc218_d

#1：まずは入力
N = int(input())

#3:入力を格納する場所をつくらねば
points = []

#5:連想配列宣言しておいてー
from collections import defaultdict
input_points = defaultdict(int)

#2:もう一個入力あるからそれも
for i in range(N):
    x, y = map(int, input().split())

    #4:座標は連想配列使うとよさげだな
    #  対角線上に一致しているかどうか
    #  をどんどん確かめていく感じにしたいからね。
    points.append([x, y])

    #6:とりま座標がある場所を1とするか(定期)
    input_points[(x, y)] = 1

#12:出力するやつ定義するのわすれとった
output = 0

#7:よし、全探索はじめていくぞ
#8:座標の名前は
#(p1_x, p1_y)-----(p1_x, p2_y)
# |                         |
# |                         |
# |                         |
# |                         |
# |                         |
#(p2_x, p1_y)-----(p2_x, p2_y)
#こんな感じにしたいということで
#対角線上の座標はp1, p2にしまーす
for p1 in range(N):

    #9:対角線上の2点を用いて探索するから2重のループやな
    for p2 in range(p1+1, N):
        
        #11:数える前に座標の定義せねば
        p1_x, p1_y = points[p1]
        p2_x, p2_y = points[p2]

        #15:p1とp2が同じ位置にあるときも数えちゃってたわコレ...
        #   座標どっちか一方でもあってたら飛ばさなきゃ
        if p1_x == p2_x or p1_y == p2_y:
            continue

        #10:正方形だった回数を数えたい
        #   上のやつみながら考えると、
        #   p1_xとp2_yの組み合わせがあり、
        #   その上p2_xとp1_yの組み合わせ
        #   があるって感じの条件文にすると
        #   よさげだな
        #   入力された座標の中から探していくか
        if input_points[p1_x, p2_y] == 1 and input_points[p2_x, p1_y] == 1:
                output += 1
    
#14:出力したらなんか二重に数えてるの忘れてた
#   出力の数半分にせねば
output //= 2

#13:これで出力して終了かなぁ
print(output)

