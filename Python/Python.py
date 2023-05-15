import numpy as np
x = np.array([0,1])
w = np.array([0.5,0.5])
b = -0.7

print(x*w)#各配列番号番号ごとかけ合わせる
print(np.sum(x*w))#かけ合わせた総和
print(np.sum(w*x)+b)#総和にバイアスを導入したもの