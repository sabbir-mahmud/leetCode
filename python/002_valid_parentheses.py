def valid_parentheses(string: str):
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    for char in string:
        if char in bracket_map:
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return not stack


if __name__ == "__main__":
    print(valid_parentheses("()[]{}"))  # True
    print(valid_parentheses("()()]]"))
