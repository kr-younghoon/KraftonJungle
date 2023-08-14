class Solution:
    def romanToInt(self, s: str) -> int:
        lst = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        n = len(s)
        total = 0
        print(n)
        for i in s:
            curr = lst[s[i]]
            total += curr
            print(total)
        return total

solution = Solution()  # Solution 클래스의 인스턴스 생성
result = solution.romanToInt("III")  # romanToInt 메서드 호출
print(result)  # 결과 출력