#座標圧縮
#「数列の要素」を「小さい順から何番目」というものに変換する

H, W, N = map(int, input().split())

cards = []
row = []
col = []

for i in range(N):
    A, B = map(int, input().split())

    cards.append([A, B])
    row.append(A)
    col.append(B)

#set:重複の削除
row = set(row)

#ソート用にリストに変換
row = list(row)
row.sort()

#圧縮後の座標を記録する連想配列
#(小さい順にした値を格納する配列)
row_conv = dict()

#元々のリストの値を添え字として使いたい→連想配列
for i in range(len(row)):
    row_conv[row[i]] = i+1
    #元々の値→小さい順にした値を
    #元々の値=小さい順にした値という形で表している

#####################以下列の処理########################

col = set(col)
col = list(col)
col.sort()

col_conv = dict()

for i in range(len(col)):
    col_conv[col[i]] = i+1

for row_i, col_i in cards:
    ans_row = row_conv[row_i]
    ans_col = col_conv[col_i]
    print(ans_row, ans_col)




