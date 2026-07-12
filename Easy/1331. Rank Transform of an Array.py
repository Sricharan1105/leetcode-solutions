class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        sorted_arr = sorted(set(arr))

        r = 1
        for num in sorted_arr:
            rank[num] = r
            r += 1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]

        return arr
