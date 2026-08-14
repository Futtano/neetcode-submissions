class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            match ch:
                case '(' | '[' | '{':
                    stack.append(ch)

                case ')' | ']' | '}':
                    if not stack:
                        return False

                    top = stack.pop()

                    if (ch == ')' and top != '(') or \
                       (ch == ']' and top != '[') or \
                       (ch == '}' and top != '{'):
                        return False

                case _:
                    return False

        return not stack