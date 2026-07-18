class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+-*/"
        for tok in tokens:
            if tok in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                if tok == "+":
                    stack.append(num2 + num1) 
                elif tok == "-":
                    stack.append(num2 - num1) 
                elif tok == "/":
                    stack.append(int(num2 / num1))
                elif tok == "*":
                    stack.append(num2 * num1) 
            else:
                stack.append(int(tok))
            print(stack)
            
        return int(stack[0])