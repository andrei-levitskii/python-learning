class Solution:
    def climbStairs(self, n: int) -> int:
        prev, next = 1, 2
        for _ in range(2, n + 1):
            next, prev = next + prev, next
            print(next)
        return prev


def main() -> None:
    inputs = [
        7,
    ]
    s = Solution()
    for n in inputs:
        print(s.climbStairs(n))


if __name__ == "__main__":
    main()
