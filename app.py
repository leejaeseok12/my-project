import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from scipy import signal
import streamlit as st

# 전달 함수 정의
num = [100]
den = [1, 5, 6]
system = ctrl.tf(num, den)

# step response
t, y = ctrl.step_response(system)
st.line_chart(y)

# Bode plot
w, mag, phase = ctrl.bode(system, dB=True, Plot=False)
st.line_chart(mag)
st.line_chart(phase)
