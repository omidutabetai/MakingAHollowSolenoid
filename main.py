import numpy as np
from scipy.optimize import fsolve
from scipy.special import ellipk, ellipe

# 透磁率
MU = 4 * np.pi * 10 ** -7

# ソレノイドコイルの半径（m）を入力
r = float(input("ソレノイドコイルの半径を入力してください（m）："))

# ソレノイドコイルの長さ（m）を入力
l = float(input("ソレノイドコイルの長さを入力してください（m）："))

# ソレノイドコイルのインダクタンス（H）を入力
L = float(input("ソレノイドコイルのインダクタンスを入力してください（μH）："))
L = L * 10 ** (-6)

# コイルの断面積（m^2）
A = np.pi * r ** 2

# コイルの長岡係数を計算する関数
def calc_k(l, r):
    s = l / (2 * r)
    k = 1 / np.sqrt(1 + s ** 2)
    k2 = k ** 2
    c = 4.0 / (3.0 * np.pi * np.sqrt(1.0 - k2))
    kn = c * (((1.0 - k2) / k2) * ellipk(k2) - ((1.0 - 2.0 * k2) / k2) * ellipe(k2) - k)
    print(kn)
    return kn

# コイルの巻数を計算する関数
def calc_turns(L, A, l, r):
    kn = calc_k(l, r)
    def equation(N):
        return L - kn * MU * A * N ** 2 / l
    N = fsolve(equation, 1)
    return int(N[0])

# コイルの巻数を計算する
turns = calc_turns(L, A, l, r)
print("ソレノイドコイルの巻数：{.5}".format(turns))
