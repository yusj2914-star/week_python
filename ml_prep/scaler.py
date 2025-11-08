# print(list(zip([ [10, 20, 30], [20, 30, 40], [30, 40, 50] ])))

class Datasclaer:
    # fit 함수에서 최댓값/최소값을 구하기 위해 
    # 최대/최소값 초기화 작업을 먼저 진행(변수를 선언)
    def __init__(self):
        self.min = None
        self.max = None

    # 각 열의 최대값, 최소값을 구하는 함수 생성
    # [[12, 25, 37], [15, 27, 39], [16, 30, 45]]
    # zip([[12, 25, 37], [15, 27, 39], [16, 30, 45]]) -> [([12, 15, 16],), ([25, 27, 30],), ([37, 39, 45],)]
    def fit(self, data):
        self.min = [min(col) for col in zip(*data)] # -> [12, 25, 37]
        self.max = [max(col) for col in zip(*data)] # -> [16, 30, 45]

    # min-max scaling
    def transform(self, data):
        scaled = []

        for row in data: # [12, 25 ,37], [15, 27, 39], [16, 30, 45]
            new_row = []
            for i, value in enumerate(row):
                new_row.append((value - self.min[i])/(self.max[i] - self.min[i]))
                # new_row.append((12 - self.min[0])/(self.max[0] - self.min[0]))
                # 12 - 12 / 16 - 12
            scaled.append(new_row)

        return scaled
    
    # fit, transform 한번에 수행
    def fit_transform(self, data):
        # 클래스 내부의 fit() 함수를 불러왔기 때문에 self. 를 앞에 붙여서 호출
        self.fit(data)
        # transform() 함수를 호출한 경과를 전달함
        return self.transform(data)