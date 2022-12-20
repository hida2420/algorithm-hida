#deque
#先頭と末尾へ要素を代入する操作をO(1)でできるやつ
#アルゴリズムとデータ構造で習ったキュー
from collections import deque

N = int(input())
S = input()

#キューはこうやって宣言する
#[]ではない
que = deque()

#末尾に挿入
que.append(N)

#末尾から先頭の要素にかけて、-1ずつ下がっていく
for i in range(N-1, -1, -1):
    if S[i] == 'R':
        #先頭に挿入
        que.appendleft(i)
    elif S[i] == 'L':
        #末尾に挿入
        que.append(i)

print(*que)