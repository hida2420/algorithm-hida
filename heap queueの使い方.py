#heapq 高速でリストから最小値を取り出す構造
import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

#heap queueの準備
que = []

for i in range(K):
    #キューにデータをプッシュしていく
    heapq.heappush(que, P[i])

#que[0]が最小値
print(que[0])

for i in range(K, N):

    #キューの中から最小値を取り出す
    x_min = heapq.heappop(que)

    #取り出す前の最小値とK番目の要素を比較し、
    #大きい方をpushする
    #規則性：小さいほうはK+1番目に大きい要素
    #　　　　すなわちもう使うことはない
    heapq.heappop(que, max(x_min, P[i]))
    print(que[0])

