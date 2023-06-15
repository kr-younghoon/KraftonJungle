class Solution:
    def isValid(self, s: str) -> bool:
    # 방법 1 - 대 실패 : 답안을 만들어서 비교하려 했지만, 형식이 안맞음 ['()'] != "()"
        # if (1 <= len(s) and len(s) <= 10^4):
        #     s_ans = []
        #     for i in range(len(s)):
        #         if (s[i] == "("):
        #             s_ans.append("()")
        #         elif (s[i] == "["): 
        #             s_ans.append("[]")
        #         elif (s[i] == "{"):
        #             s_ans.append("{}")
        #     print(s_ans)
        # return s_ans == s
    # 방법2 - ans 리스트에 하나씩 추가했다가 없으면 패스 하는 케이스
        s_ans = []
        # char를 하나씩 꺼내야할지? num으로 꺼낼지? -> char로 ㄱㄱ
        for i in s:
            # ans에 일단 추가한다.
            if i == "(" or i == "{" or i == "[":
                s_ans.append(i) 
            # ) } ] 일때 ans를 하나씩 삭제
            else:
                if not s_ans:
                    return False
                # 하나하나 케이스를 다 해줘야하나?
                if i == ")" and s_ans[-1] == "(":
                    s_ans.pop()
                elif i == "]" and s_ans[-1] == "[":
                    s_ans.pop()
                elif i == "}" and s_ans[-1] == "{":
                    s_ans.pop()
        return not s_ans