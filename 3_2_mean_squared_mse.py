import numpy as np

# 임의의 기울기 a, y절편 b
fake_a_b = [3, 76]

# data set
data=[[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

# y = ax + b 에 a와 b 값을 대입하여 결과를 출력하는 함수
def predict(x):
    return fake_a_b[0] * x + fake_a_b[1]

# 평균 제곱오차 MSE
def mse(y_hat, y):
    return ((y_hat-y)**2).mean()

# MSE 함수를 각 y값에 대입, 최종값 반환
def mse_val(predict_result, y):
    return mse(np.array(predict_result), np.array(y))

predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print('공부한 시간=%.f, 실제 점수=%.f, 예측 점수=%.f'%(x[i], y[i], predict(x[i])))

print(f'mse 최종값: {str(mse_val(predict_result, y))}')
