# 2. cleaner.py
# - TextCleaner 클래스 작성
# - remove_special(text): 정규식을 이용하여 특수문자 제거 (re.sub)
# - to_lower(text): 소문자로 변환
# - clean_corpus(corpus): 여러 문장 리스트를 받아 전처리 수행
# - 텍스트 리스트 ["Hello!!!", "Machine-Learning??", "Python123"]를 TextCleaner로 전처리하고 결과 출력


# 텍스트 전처리를 위한 내장모듈
import re

class TextCleaner:
    # 특수문자 제거 메서드 생성
    def remove_special(self, text):
        # r은 정규표현식
        # ^는 not 부정을 의미
        # a-zA-Z: 소문자 a 부터 z 까지, 대문자 A 부터 Z 까지
        # \s는 문자열
        return re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 소문자 변경 메서드
    def to_lower(self, text):
        return text.lower()
    
    # 한번에 구동시킬 수있는 함수를 만들기
    # 위의 특수문자 제거와 소문자 변경 작업을 모두 모으는 메서드
    # ["Hello!!!", "Machine-Learning??", "Python123"]
    def clean_corpus(self, text):
        
        result = []
        for t in text:
            # 특수문자 제거 작업
            t1 = self.remove_special(t)
            # 소문자 제거 작업
            t2 = self.to_lower(t1)
            # result 리스트에 추가
            result.append(t2)

        return result
