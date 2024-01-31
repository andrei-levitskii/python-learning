class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) <= 1:
            return s
        max_str = s[0]
        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)
            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        return max_str


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 1
        max_str = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        max_str = s[j : i + 1]
        return max_str


class Solution22:
    def longestPalindrome(self, s: str) -> str:
        res = [0, 0]
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            if dp[i][i + 1]:
                res = [i, i + 1]
        for length in range(3, n + 1):
            i = 0
            for j in range(length - 1, n):
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j]:
                    res = [i, j]
                i += 1
        return s[res[0] : res[1] + 1]


# https://ru.wikipedia.org/wiki/Алгоритм_Манакера
class Solution3:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 1
        max_str = s[0]
        s = "#" + "#".join(s) + "#"
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < len(s) and s[i - dp[i] - 1] == s[i + dp[i] + 1]:
                dp[i] += 1
            if i + dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i - dp[i] : i + dp[i] + 1].replace("#", "")
        return max_str


if __name__ == "__main__":
    inputs = [
        # "babad",
        # "cbbd",
        "peeweep",
    ]
    s = Solution22()
    for string in inputs:
        print(s.longestPalindrome(string))
