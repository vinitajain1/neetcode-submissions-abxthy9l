class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string not in sorted_dict:
                sorted_dict[sorted_string] = []
            sorted_dict[sorted_string].append(s)
        all_values = []
        for value in sorted_dict.values():
            all_values.append(value)
        return all_values
        