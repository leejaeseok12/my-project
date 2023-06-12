import numpy as np
import matplotlib.pyplot as plt
import control

# 전달함수 정의
num = [100]
den = [1, 5, 6]
G = control.TransferFunction(num, den)

# 폐루프 전달함수 계산
L = G / (1 + G)

# 단위 계단 입력 생성
t = np.linspace(0, 10, 1000)
u = np.ones_like(t)

# 시스템 응답 계산
t, y = control.step_response(L, T=t, X0=0.0, input=u)

# 응답곡선 그리기
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()
