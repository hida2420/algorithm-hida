from collections import defaultdict

same = defaultdict(int)

#添え字に数字意外の物をつかえる
same[A[i]] = 1
same["そえじ"] = 2

#これで一つ一つ参照
for i in same.values():
    print(i)