# app.py
import numpy as np

import matplotlib.pyplot as plt

from scipy import signal

import streamlit as st

st.set_page_config(
    page_title="leechaewon page",
)

# Streamlit 앱 구성
st.title('202021053 이채원')

def main():
    st.header('Step and Bode Plot')
    
    # 전달함수 계수
    num = [100]
    den = [1, 5, 106]

    # 시스템 응답
    t, y = signal.step(signal.TransferFunction(num, den))

    # 응답곡선 그리기
    fig1 = plt.figure()
    plt.plot(t, y)
    plt.xlabel('Time')
    plt.ylabel('Output')
    plt.title('Step Response')
    plt.grid(True)
    st.pyplot(fig1)
    
    # 주파수 응답
    w, mag, phase = signal.bode(signal.TransferFunction(num, den))

    # Bode plot 그리기
    fig2 = plt.figure()
    plt.semilogx(w, mag)
    plt.ylabel('Gain (dB)')
    plt.title('Bode Plot (Gain)')
    plt.grid(True)
    st.pyplot(fig2)
    
    fig3 = plt.figure()
    plt.semilogx(w, phase)
    plt.xlabel('Frequency (rad/s)')
    plt.ylabel('Phase (degrees)')
    plt.title('Bode Plot (Phase)')
    plt.grid(True)
    st.pyplot(fig3)

if __name__ == '__main__':
    main()