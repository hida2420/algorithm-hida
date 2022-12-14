#尺取り虫みたいに、のびてーちぢんでをくりかえして
#進んでいくアルゴリズム

#条件をみたしている間は右端のインデックスを進める
#条件をみたさないものがあると、右端のインデックスを
#一つもどし、左端のインデックスを一つ進める

#これをどう使うかは問題による
#ABC229Dの場合はfalseになったときに暫定の答えとして記録している

#問題文
#[D - Longest X]
#https://atcoder.jp/contests/abc229/tasks/abc229_d

S = input()
K = int(input())

#0文字目を?にする
S = "?" + S

#今回の問題は文字列の長さを入力するやつがないから
N = len(S)

#要素全部0の「.」を記録する配列
#S[i]までに何個「.」があったかを記録する
sum_dot = [0]*N

#sum_dotの設定
for i in range(1, N):

    #もしS[i]が「.」だったら、S[i-1]までの「.」の数に
    #1加算する
    #S[i]が「X」だったら、S[i-1]までの「.」の数を
    #そのままひきつぐ
    if S[i] == "X":
        sum_dot[i] = sum_dot[i-1]
    else:
        sum_dot[i] = sum_dot[i-1]+1

#最終的な答え
result = 0

#右端のポインタ
r = 1

#lは左端のポインタ
for l in range(1, N):

    #Sの長さ分尺取り法を行う
    while r < N:

        #num_dotは閉区間[l, r]の中にある「.」の数
        num_dot = sum_dot[r] - sum_dot[l-1]
        
        #条件をみたせば、尺取り虫の頭をのばす
        #(すなわち右端のポインタを右にひとつ移動させる)
        #条件をみたさなければ、尺取り虫のけつを縮める
        #(すなわちwhileループからはずれて左端のポインタをひとつ右に移動させる)
        if num_dot <= K:
            r+=1
        else:
            break

    #尺取り虫のけつをのばしたときに、暫定的な結果として保存しておく
    result = max(result, r-l)

#ふぅ
print(result)