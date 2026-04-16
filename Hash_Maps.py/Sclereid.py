import sys
input = sys.stdin.readline

N, K = map(int, input().split())
c = list(map(int, input().split()))

from collections import defaultdict

freq = defaultdict(int)

# Initialize first window
for i in range(K):
    freq[c[i]] += 1

max_distinct = len(freq)

# Sliding window
for i in range(K, N):
    # Add new element
    freq[c[i]] += 1

    # Remove old element
    freq[c[i - K]] -= 1
    if freq[c[i - K]] == 0:
        del freq[c[i - K]]

    # Update answer
    max_distinct = max(max_distinct, len(freq))

print(max_distinct)
