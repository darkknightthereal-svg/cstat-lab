def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0


text = input("Enter a string of brackets: ")
if is_valid(text):
    print("Valid")
else:
    print("Invalid")
