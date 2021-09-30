import numpy as np

x = [2, 4, 6, 8]
y = [81, 93, 91, 97]

mean_x = np.mean(x)
mean_y = np.mean(y)

print(f'\nx의 평균값: {mean_x}\ny의 평균값: {mean_y}')

# 기울기 분모
divisor = sum([(mean_x-i)**2 for i in x])
# 기울기 분자
def top(x, mean_x, y, mean_y):
    # 기울기 분자
    d = 0
    for i in range(len(x)):
        d += (x[i]-mean_x) * (y[i]-mean_y)
    return d

dividend = (top(x, mean_x, y, mean_y))
print(f'\n분모: {divisor}\n분자: {dividend}')

# 기울기와 y절편
a = dividend / divisor
b = mean_y - (mean_x * a)

print(f'\n기울기 a: {a}\ny절편: {b}')