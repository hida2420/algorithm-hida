#Union Find
#グラフ上で
# 2つの頂点の連結(Union)と
# 連続であるかの判定(Find)を高速で行える

#これをコピペして毎回使う
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
    def same(self,a,b):
        return self.leader(a) == self.leader(b)
    def size(self,a):
        return abs(self.parent_size[self.leader(a)])
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]

N, Q = map(int, input().split())

#これでunionfindを用意する
UF = UnionFind(N+1)

for i in range(Q):

    P, A, B = map(int, input().split())

    if P == 0:
        #これで頂点ABを連結する
        UF.merge(A, B)
    else:
        #これで頂点ABが連結しているかどうかを判別する
        if UF.same(A, B):
            print("Yes")
        else:
            print("No")
