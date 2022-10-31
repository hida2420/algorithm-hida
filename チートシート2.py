#数字を英単語に
#chr(96) = "a"
#chr(97) = "b"

#文字列に文字を追加
ans = ""
ans += "a"

#重複のない配列
a_set = set(a)
print(len(a_set))

#2重ループ
for i in range(N):
    for j in range(i+1, N):
        print('')

#最大値の比較
#ansよりもvalが大きければ、ansにvalを代入
ans = max(ans, val)

#空配列の宣言
cheese = []

#リストの要素を結合
con_A = "".join(A)
con_B = "".join(B)
temp_ans = int(con_A)*int(con_B)

#pythonの条件式or
if A == [] or B == []:
    continue