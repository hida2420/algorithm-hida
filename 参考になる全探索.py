N, X = list(map(int, input().split()))

L = []
a = []

#N行分の入力
for i in range(N):
    temp = list(map(int, input().split()))

    #0番目のものをLに
    L.append(temp[0])

    #1～最後までのものをaに
    #3 1 8 4
    #2 10 5が入力だった場合
    #a[0] = 1, 8, 4になる
    a.append(temp[1:])

#計算結果を挿入するリスト
result = [1]

for i in range(N):
    temp_res = []

    #i番目のふくろ
    for a_i in a[i]:

        #掛け算の結果を一次的なリストに挿入
        for r in result:
            #resultの要素とふくろの要素をかけることで、すべての要素をもれなく掛け算することができる
            temp_res.append(a_i*r)

    result = temp_res

ans = result.count(X)

print(ans)
