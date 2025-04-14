def combination_sum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remaining:
                break
            backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])

    backtrack(0, [], target)
    return result
#               сюда писать циферки
#                       ↓
candidates = [10, 1, 2, 7, 6, 1 ,5]
target = 8
print(combination_sum2(candidates, target))