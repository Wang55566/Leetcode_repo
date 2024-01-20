class Solution:
  def climbStairs(self, n: int) -> int:

    dp = {}

    def recursion(step):

        if step in dp:
            return dp[step]

        if step <= 3:
            answer = step
        else:
            answer = recursion(step - 1) + recursion(step - 2)

        dp[step] = answer

        return answer

    return recursion(n)
