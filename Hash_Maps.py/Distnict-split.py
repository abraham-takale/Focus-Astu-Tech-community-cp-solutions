import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    prefix = [0] * n
    suffix = [0] * n

    seen_prefix = set()
    for i in range(n):
        seen_prefix.add(s[i])
        prefix[i] = len(seen_prefix)

    seen_suffix = set()
    for i in range(n - 1, -1, -1):
        seen_suffix.add(s[i])
        suffix[i] = len(seen_suffix)

    ans = 0
    for i in range(n - 1):
        ans = max(ans, prefix[i] + suffix[i + 1])

    print(ans)
