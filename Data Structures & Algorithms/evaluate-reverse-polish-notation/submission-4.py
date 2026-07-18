import operator 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '*' : operator.mul,
            '/' : lambda a, b: int(a / b),
            '+' : operator.add,
            '-' : operator.sub
        }

        result = 0 
        stack = []

        for token in tokens:
            if token not in ops.keys():
                stack.append(int(token))
            else:
                result = (ops[token])(stack[-2],stack[-1])
                stack = stack[:-2] + [result]
        
        return stack[0]