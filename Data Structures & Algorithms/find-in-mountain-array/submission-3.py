class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 1, length - 2

        while l <= r:
            m = l + (r - l) // 2

            l_peak = mountainArr.get(m - 1)
            r_peak = mountainArr.get(m + 1)
            m_peak = mountainArr.get(m)

            if l_peak < m_peak < r_peak:
                l = m + 1
            elif l_peak > m_peak > r_peak:
                r = m - 1
            else:
                peak = m
                break
        
        l, r = 0, peak - 1
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        l, r = peak, length - 1
        while l <= r:
            m = l + (r - l) // 2
            val = mountainArr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m
        
        return -1