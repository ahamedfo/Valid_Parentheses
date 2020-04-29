from collections import deque
class Solution(object):
    def isValid(self, s):
        stack = deque()
        top = ''
        top_map = {}
        braces_map = {'}': '{', ')': '(', ']': '[' }
        for values in s:
            if values in braces_map.keys():
                if braces_map[values] == top:
                    top = top_map[stack.pop()]
                else:
                    return False
            else:
                stack.append(values)
                top_map[values] = top
                top = values
        stack.
        return True







