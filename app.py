import numpy as np
import matplotlib.pyplot as plt
import control
import streamlit as st

def plot_response(G):
    # 폐루프 전달함수 계산
    H = 1  # 단위 피드백
    T = control.feedback(G, H)

    # Step 응답
    t_step, y_step = control.step_response(T)

    # 주파수 응답 (보드선도)
    omega, mag, phase = control.bode(T)

    # Step 응답 그래프
    fig_step, ax_step = plt.subplots()
    ax_step.plot(t_step, y_step)
    ax_step.set_xlabel('Time')
    ax_step.set_ylabel('Output')
    ax_step.set_title('Step Response')

    # 주파수 응답 보드선도 그래프
    fig_bode, (ax_mag, ax_phase) = plt.subplots(2, 1)
    ax_mag.semilogx(omega, mag)
    ax_mag.set_xlabel('Frequency')
    ax_mag.set_ylabel('Magnitude (dB)')
    ax_mag.set_title('Bode Plot - Magnitude')

    ax_phase.semilogx(omega, phase)
    ax_phase.set_xlabel('Frequency')
    ax_phase.set_ylabel('Phase (degrees)')
    ax_phase.set_title('Bode Plot - Phase')

    # 그래프를 리스트로 반환
    return [fig_step, fig_bode]

# 전달 함수 정의
num = [100]
den = [1, 5, 6]
G = control.TransferFunction(num, den)

# Streamlit 앱 구성
st.title('202021052 이재석')
st.subheader('폐루프 전달함수')
st.write(G)

# Step 응답 및 주파수 응답 그래프 플로팅
response_figs = plot_response(G)

# 그래프를 Streamlit에 표시
for fig in response_figs:
    st.pyplot(fig)
