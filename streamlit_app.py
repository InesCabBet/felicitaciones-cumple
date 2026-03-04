import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.title("🎉 Dibujando tu tarta...")

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

x = np.linspace(-3, 3, 100)
y = np.zeros(100)

line, = ax.plot([], [])

for i in range(len(x)):
    line.set_data(x[:i], y[:i])
    st.pyplot(fig)
    time.sleep(0.02)
