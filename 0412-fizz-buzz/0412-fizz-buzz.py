class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = ['' for _ in range(n)]
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                res[num-1] = 'FizzBuzz'

            elif num % 3 == 0:
                res[num-1] = 'Fizz'
            elif num % 5 == 0:
                res[num-1] = 'Buzz'
            else:
                res[num-1] = str(num)

            
        return res