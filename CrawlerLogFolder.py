'''
The Leetcode file system keeps a log each time some user performs a change folder operation.
The operations are described below:
- "../": Move to the parent folder or the current folder. (If you are already in the main folder, remain in the same folder).
- "./": Remain in the same folder.
- "x/": Move to the child folder named x (This folder is guaranteed to always exist).

You are given a list of strings logs where logs[i] is the operation performed by the user at the i-th step.
The file system starts in the main folder, then the operations in logs are performed.
Return the minimum number of operations needed to go back to the main folder after the change folder operations.
'''

from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = []
        for i in logs:
            if i == "../" and len(count) > 0:
                count.pop()
                continue
            elif i == "./" or i == "../":
                continue
            else:
                count.append(i)
        return len(count)