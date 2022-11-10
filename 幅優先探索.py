N, M = map(int, input().split())

#道路情報
#添え字がスタート地点　要素がゴール地点
#Ex) connect[1]={2,3,4}なら都市①から都市②③④にいけるよ
ways = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())

    #入力にある道路情報を保存
    ways[A].append(B)

from collections import deque

#幅優先探索
#緑dif以下の問題で木構造を使ってシュミレーションできるものは
#幅優先探索か深さ優先探索を使おう
# １：スタート地点を決める
# ２：waysリスト(入力から得た、訪問可能な経路を保存したリスト)
#     を使って、その地点からとある地点へまだ行ったことがないかどうか(未訪問かどうか)を調べる
# ３：未訪問の場所を発見次第、カウントする変数の数を増やしていく
# ※全て探索したかどうかはキューを用いる
# 　えんきゅー→デキューを繰り返し、何もえんきゅーされなくなってキューが空になると探索が終了する　
def BFS(start):

    #最終的に返す、移動可能な場所の数
    movable_place = 1

    #訪問済み=true
    #未訪問=false
    visited = [False]*(N+1)

    #スタート地点からスタート地点へは絶対いける
    visited[start]=True

    #キューの準備
    que=deque()

    #キューにスタート地点を追加
    que.append(start)

    #キューが空になるまでwhileを回す
    #キューが空→全ての場所を訪問したってこと
    #１：訪問可能な場所を発見次第その場所をキューに追加する
    #２：キューに挿入した順に場所を訪問していき、訪問したらキューからとりだしていく
    #３：訪問可能な場所が見つからなくなったら何も追加されなくなるから、whileは終了する
    while 0<len(que):
        #キューから取り出した場所が訪問中の場所になる
        visiting_place = que.popleft()

        #入力から得た訪問可能な場所の中から
        #1つの場所を取り出して訪済みかどうか調べる
        for next_move in ways[visiting_place]:
            #もし未訪問の場所だったら、
            #・移動可能な経路のカウントを増やす
            #・その場所を訪問済みにする
            #・キューにその場所を追加する
            if visited[next_move] == False:
                movable_place+=1
                visited[next_move]=True
                que.append(next_move)

    #探索で数えた移動可能な経路の数を返す
    return movable_place

ans = 0

for i in range(1, N+1):
    ans += BFS(i)

print(ans)
















