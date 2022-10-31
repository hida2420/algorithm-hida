N = int(input())

#2次元配列の宣言
Mts = []

for i in range(N):

    S, T = map(str, input().split())

    #文字列で受け取ってから整数に変換
    T = int(T)

    #ソート用2次元配列に追加
    Mts.append([T, S])

#Mtsの第一要素に対して、大きい順にソート
#小さい順ならMts.sort()
Mts.sort(reverse = True)

print(Mts[1][1])