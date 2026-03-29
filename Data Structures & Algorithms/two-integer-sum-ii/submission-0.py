class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)
        for i in range(len(numbers)):
            hash_map[numbers[i]] = i
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if hash_map[diff]>i:
                return [i+1,hash_map[diff]+1]
        return []
