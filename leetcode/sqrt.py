class Solution:
    def mySqrt(self, x: int) -> int:
        bigger, now, smaller = x, max(x // 2, 1), 0
        while True:
            if now * now == x or smaller == now or bigger == now:
                return now
            else:
                if (now)**2 < x:
                    smaller, now = now, (now + bigger)//2
                else:
                    bigger, now = now, (now + smaller)//2
    mySqrt(4)
