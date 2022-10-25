import itertools#順列列挙用ライブラリ

#型が左右で違う場合の入力
S, K = map(str, input().split())
K = int(K)

#重複あるかもしてない
set_S = set()

# 例えばlen(S)=3の場合、
# 0, 1, 2の順列を片っ端から参照していく
#p[0] = (0, 1, 2), p[1] = (0, 2, 1), ...
#このpの要素を添え字として使う
for p in itertools.permutations(range(len(S))):

    temp_S = ""
    
    #p[1]の場合、i=0, i=2, i=1の順で参照される
    for i in p:
        temp_S += S[i]

    set_S.add(temp_S)

#辞書順じゃない可能性があるからソートしたい
#けどsetクラスに辞書順ソートするメソッドが備わっていない
#てことでlistに変換して使おう
ans = list(set_S)

ans.sort()

print(ans[K-1])