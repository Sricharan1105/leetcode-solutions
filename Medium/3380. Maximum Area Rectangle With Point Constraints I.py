from typing import List

class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple, points))
        n = len(points)
        answer = -1

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue

                if (x1, y2) in point_set and (x2, y1) in point_set:
                    valid = True

                    for x, y in points:
                        if x1 <= x <= x2 or x2 <= x <= x1:
                            if y1 <= y <= y2 or y2 <= y <= y1:
                                if (x, y) not in [
                                    (x1, y1),
                                    (x2, y2),
                                    (x1, y2),
                                    (x2, y1)
                                ]:
                                    valid = False
                                    break

                    if valid:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        answer = max(answer, area)

        return answer
