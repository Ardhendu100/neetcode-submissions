class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        slow, fast = n, self.sumOfSquaresOfDigits(n)

        while slow != fast:
            fast = self.sumOfSquaresOfDigits(fast)
            fast = self.sumOfSquaresOfDigits(fast)
            slow = self.sumOfSquaresOfDigits(slow)

            if fast == 1:
                return True
        return False
         

    def sumOfSquaresOfDigits(self, n):
        output = 0

        while n:
            digit = n%10
            digit = digit ** 2
            output+=digit
            n = n // 10
        return output

        