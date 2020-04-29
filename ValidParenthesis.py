from collections import deque
class Solution(object):
    def isValid(self, s):
        stack = deque()
        top = ''
        braces_map = {'}': '{', ')': '(', ']': '[' }
        for values in s:
            if values in braces_map.keys():
                if braces_map[values] == top:
                        stack.pop()
                        if len(stack) > 0:
                            top = stack.pop()
                            stack.append(top)
                else:
                    return False
            else:
                stack.append(values)
                top = values
        if len(stack) > 0:
            return False
        return True







