class Solution:
    def countAndSay(self, n: int) -> str:
        if not n:
            return None
        
        ls = self.helper(n)
        res = ''
        for i in ls:
            res += str(i)
        return res
            
    
    def helper(self, n):
        if n == 1:
            ls = [1]
            return ls
        if n == 2:
            return [1, 1]
        
        curr_ls = self.helper(n - 1)
        
        cnt = 1
        ls = []
        # print(curr_ls)
        for i in range(len(curr_ls) - 1):
            if curr_ls[i] == curr_ls[i + 1]:
                cnt += 1
                if i + 1 == len(curr_ls) - 1:
                    ls.append(cnt)
                    ls.append(curr_ls[i + 1])
            else:
                ls.append(cnt)
                ls.append(curr_ls[i])
                cnt = 1
                if i + 1 == len(curr_ls) - 1:
                    ls.append(1)
                    ls.append(curr_ls[i + 1])
        # print(ls)
        return ls