import sys
input = sys.stdin.readline


def checking_ppap():
    ppap_case = input().strip()
    stack = []

    for ppap in ppap_case:
        if ppap == "P":
            if len(stack) > 2 and stack[-1] == "A":
                stack.pop()
                if stack.pop() != "P":
                    return False
                if stack.pop() != "P":
                    return False
        stack.append(ppap)

    if len(stack) == 1 and stack[-1] == "P":
        return True
    else:
        return False


if checking_ppap():
    print("PPAP")
else:
    print("NP")

