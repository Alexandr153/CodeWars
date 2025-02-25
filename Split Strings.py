def solution(s):
    return [''.join([s[i], s[i+1] if i + 1 < len(s) else '_']) for i in range(0, len(s), 2)]
print(solution('abc'))