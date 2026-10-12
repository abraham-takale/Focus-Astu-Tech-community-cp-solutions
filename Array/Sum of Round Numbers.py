t = int(input())
for _ in range(t):
    n = input().strip()
    L = len(n)
    parts = []
    for i, ch in enumerate(n):
        if ch != '0':
            parts.append(ch + '0' * (L - i - 1))
    print(len(parts))
    print(*parts)
