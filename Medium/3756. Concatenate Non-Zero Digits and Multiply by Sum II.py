from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD

        digit_sum = [0] * (n + 1)
        nonzero_count = [0] * (n + 1)
        pref_num = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')

            digit_sum[i + 1] = digit_sum[i] + d
            nonzero_count[i + 1] = nonzero_count[i]
            pref_num[i + 1] = pref_num[i]

            if d != 0:
                nonzero_count[i + 1] += 1
                pref_num[i + 1] = (pref_num[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            cnt = nonzero_count[r + 1] - nonzero_count[l]
            sm = digit_sum[r + 1] - digit_sum[l]

            x = (pref_num[r + 1] - pref_num[l] * pow10[cnt]) % MOD
            ans.append(x * sm % MOD)

        return ans
