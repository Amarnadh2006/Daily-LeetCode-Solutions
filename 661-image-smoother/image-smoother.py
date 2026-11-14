class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = []

        for i in range(m):
            row = []
            for j in range(n):
                total = 0
                count = 0

                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if x >= 0 and x < m and y >= 0 and y < n:
                            total += img[x][y]
                            count += 1

                row.append(total // count)

            res.append(row)

        return res