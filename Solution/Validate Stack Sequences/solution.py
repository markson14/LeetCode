import sys
def validateStackSequences(self, pushed, popped):
    stack = []
    for push in pushed:
        stack.append(push)
        while popped and stack and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
    return False if stack else True


def main():
    p_push = list(map(int,input()))
    p_stack = list(map(int,input()))
    print(is_pop_order(p_push, p_stack))


if __name__ == '__main__':
    main()
