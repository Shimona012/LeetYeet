class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        arr=list()
        for i in range(1,n+1):
            if i%3==0:
                if i%5==0:
                    arr.append("FizzBuzz")
                    continue
                else:
                    arr.append("Fizz")
                    continue
            elif i%5==0:
                if i%3==0:
                    arr.append("FizzBuzz")
                    continue
                else:
                    arr.append("Buzz")
                    continue
            else:
                arr.append(str(i))
                continue
        return arr

                