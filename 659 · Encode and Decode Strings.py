# lintcode not leetcode
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encode_str = ''
        for i in range(len(strs)):
            if strs[i] != ':' and i != len(strs) - 1:
                encode_str += strs[i] + ':;'
            if strs[i] == ':':
                encode_str += ':' + strs[i] + ':;'
            if i == len(strs) - 1:
                encode_str += strs[i]

        return encode_str

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res = str.split(':;')
        if '::' not in res:
            return res
        else:
            for i in range(len(res)):
                if res[i] == '::':
                    res[i] = ':'
            return res