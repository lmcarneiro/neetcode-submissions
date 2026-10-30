class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        for sandwich in sandwiches:
            n = len(q)
            i = 0
            while q[0] != sandwich and i < n:
                s = q.popleft()
                q.append(s)
                i += 1
            if q[0] == sandwich:
                q.popleft()
            else:
                break

        return len(q)