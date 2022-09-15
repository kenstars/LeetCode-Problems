class Solution:
    def convert(self, val):
        prev = None
        result = []
        count = 0
        for i in val:
            if prev == None or prev == i:
                count +=1
            else:
                result.append(str(count))
                result.append(prev)
                count = 1
            prev = i
        else:
            result.append(str(count))
            result.append(prev)
        return "".join(result)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.convert(self.countAndSay(n-1))
                
                
               