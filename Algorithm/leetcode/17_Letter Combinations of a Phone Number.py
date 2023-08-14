# 2부터 9까지의 숫자가 포함된 문자열이 주어졌을 때, 
# 그 숫자가 나타낼 수 있는 모든 가능한 문자 조합을 반환합니다. 
# 어떤 순서로든 답을 반환합니다.

# 전화 버튼에서와 같이 숫자와 문자를 매핑하는 방법은 다음과 같습니다. 
# 1은 어떤 문자에도 매핑되지 않는다는 점에 유의하세요.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        _dict = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 
                    6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        _tmp = []
        if (0 <= len(digits) or 4 >= len(digits)):
            match len(digits):
                case 0:
                    return _tmp
                case 1:
                    int(digits)
                    for i in _dict[digits]:
                        _tmp.append(i)
                case 2:
                    for i in _dict[int(digits[0])]:
                        for j in _dict[int(digits[1])]:
                            str(i, j)
                            _tmp.append(i + j)
                case 3:
                    for i in _dict[int(digits[0])]:
                        for j in _dict[int(digits[1])]:
                            for k in _dict[int(digits[2])]:
                                str(i, j, k)
                                _tmp.append(i + j + k)
                case 4:
                    for i in _dict[int(digits[0])]:
                        for j in _dict[int(digits[1])]:
                            for k in _dict[int(digits[2])]:
                                for l in _dict[int(digits[3])]:
                                    str(i, j, k, l)
                                    _tmp.append(i + j + k + l)