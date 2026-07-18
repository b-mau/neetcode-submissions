class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "[":
                stack.insert(0,"[")
            elif i == "(":
                stack.insert(0,"(")
            elif i == "{":
                stack.insert(0,"{")
            elif i == "]":
                if stack and stack[0] == "[":
                    stack = stack[1:]
                else:
                    return False
            elif i == ")":
                if stack and stack[0] == "(":
                    stack = stack[1:]
                else:
                    return False
            elif i == "}":
                if stack and stack[0] == "{":
                    stack = stack[1:]
                else:
                    return False
            else:
                pass
        return (len(stack) == 0)

        