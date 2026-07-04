from typing import List

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        answer = events[0][0]
        longest = events[0][1]

        for i in range(1, len(events)):
            button = events[i][0]
            time = events[i][1] - events[i - 1][1]

            if time > longest or (time == longest and button < answer):
                longest = time
                answer = button

        return answer
