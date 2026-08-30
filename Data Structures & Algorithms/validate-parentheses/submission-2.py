class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        op = ['(', '{', '[']
        cl = [')', '}', ']']
        for i in s:
            if i in op:
                stack.append(i)
            if i in cl:
                if len(stack) == 0:
                    return False
                elif op.index(stack[-1]) == cl.index(i):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0