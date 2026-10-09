# SEVEN ATTACK「3-3ボーナス」のシミュレーション
#
# ルール：4人がそれぞれ 1〜7 の数字を1つ選ぶ。
#         ほかの人と被らなければ、その数字が点数になる。被ったら0点。
#
# 使い方：python seven_attack_simulation.py
# （Python 3 だけで動きます。追加のインストールは不要です）

import random
from itertools import product

NUMBERS = [1, 2, 3, 4, 5, 6, 7]   # 選べる数字
OTHERS = 3                         # 自分以外の人数
TRIALS = 100000                    # シミュレーションの回数


def points(my_number, others_numbers):
    """自分の数字と、ほかの3人の数字から、自分の点数を返す"""
    if my_number in others_numbers:
        return 0          # 被ったら0点
    return my_number      # 被らなければその数字が点数


# ------------------------------------------------------------
# 1. 全部の場合を数える（スライドのステップ2）
# ------------------------------------------------------------
print("=== 1. 全部の場合を数える ===")
all_cases = list(product(NUMBERS, repeat=OTHERS))   # 3人の選び方を全部並べる
safe_cases = [c for c in all_cases if 7 not in c]   # 3人とも7以外の場合
print(f"3人の選び方は全部で {len(all_cases)} 通り")
print(f"3人とも7以外を選ぶのは {len(safe_cases)} 通り")
print(f"7が被らない確率 = {len(safe_cases)}/{len(all_cases)} = {len(safe_cases)/len(all_cases):.3f}")
print()


# ------------------------------------------------------------
# 2. ほかの3人がテキトーに選ぶとき（スライドのステップ3・実験）
# ------------------------------------------------------------
print(f"=== 2. ほかの3人がテキトーに選ぶ（{TRIALS:,}回）===")
prob_safe = (6 / 7) ** 3   # 計算で出した「被らない確率」
print("数字 | シミュレーションの平均点 | 計算した平均点（期待値）")
for my in NUMBERS:
    total = 0
    for _ in range(TRIALS):
        others = [random.choice(NUMBERS) for _ in range(OTHERS)]
        total += points(my, others)
    average = total / TRIALS
    theory = my * prob_safe
    print(f"  {my}  |        {average:.2f}            |        {theory:.2f}")
print("→ 回数が多いと、シミュレーションと計算がほぼ同じになる")
print()


# ------------------------------------------------------------
# 3. ほかの3人がみんな7を選ぶとき（スライドの「みんなが7を選んだら？」）
# ------------------------------------------------------------
print("=== 3. ほかの3人がみんな7を選ぶ ===")
for my in NUMBERS:
    print(f"  {my} を選ぶと {points(my, [7, 7, 7])} 点")
print("→ 7は0点。一番いいのは6")
print()


# ------------------------------------------------------------
# 4. ほかの3人が「読み合いに強い選び方」をするとき（スライドのおまけ）
#    100回なら 3を7回、4を16回、5を21回、6を26回、7を30回 選ぶ
# ------------------------------------------------------------
print(f"=== 4. ほかの3人が「読み合いに強い選び方」をする（{TRIALS:,}回）===")
weights = [0, 0, 7, 16, 21, 26, 30]   # 1〜7をそれぞれ選ぶ回数（100回あたり）
for my in NUMBERS:
    total = 0
    for _ in range(TRIALS):
        others = random.choices(NUMBERS, weights=weights, k=OTHERS)
        total += points(my, others)
    print(f"  {my} を選ぶと 平均 {total / TRIALS:.2f} 点")
print("→ 3〜7のどれを選んでも、だいたい2.4点で同じになる")
