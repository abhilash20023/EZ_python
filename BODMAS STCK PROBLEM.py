#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_valid_exp(exp):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in exp:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or brackets[char] != stack.pop():
                return False
    
    return len(stack) == 0

def main():
    while True:
        exp = input("Enter an expression (or 'q' to quit): ")
        if exp.lower() == 'q':
            break
        
        if is_valid_exp(exp):
            print(f"The expression '{exp}' is valid.")
        else:
            print(f"The expression '{exp}' is NOT valid.")

if __name__ == "__main__":
    main()


# In[ ]:




