class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        word_to_idx = {}
        idx_sum, ans = len(list1) + len(list2), []

        for i in range(max(len(list1), len(list2))):
            if i > idx_sum:
                break

            for listi in [list1, list2]:
                if i < len(listi):
                    w = listi[i]
                    if (iw := word_to_idx.get(w)) is not None:
                        cur_idx_sum = i + iw
                        if cur_idx_sum < idx_sum:
                            idx_sum, ans = cur_idx_sum, [w]
                        elif cur_idx_sum == idx_sum:
                            ans.append(w)
                    else:
                        word_to_idx[w] = i

        return ans