def count_jewels(J, S):
    jewels = set(J)
    return sum(1 for char in S if char in jewels)

J = input("Драгоценности:").strip()
S = input("Камни:").strip()
print(count_jewels(J, S))