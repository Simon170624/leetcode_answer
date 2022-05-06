class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for item in strs:
            sorted_item = ''.join(sorted(item))
            if sorted_item not in strs_dict.keys():
                strs_dict[sorted_item] = []
                strs_dict[sorted_item].append(item)
            else:
                strs_dict[sorted_item].append(item)
        
        res = []
        for val in strs_dict.values():
            res.append(val)
        
        return res