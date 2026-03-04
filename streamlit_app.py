import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="FELIZ CUMPLEAÑOS 🎉", layout="centered")

st.title("🎉 !FELIZ CUMPLEAÑOS!")
st.balloons()


components.html("""
<canvas id="cakeCanvas" width="500" height="400"></canvas>

<script>
var canvas = document.getElementById("cakeCanvas");
var ctx = canvas.getContext("2d");

// Draw rectangle
function drawRectangle(x, y, width, height, color) {
    ctx.fillStyle = color;
    ctx.fillRect(x, y, width, height);
}

// Draw cake layers (like turtle version)
function drawCake() {
    drawRectangle(175, 250, 150, 30, "#5A3825"); // chocolate
    drawRectangle(200, 220, 100, 30, "pink");    // middle
    drawRectangle(225, 190, 50, 30, "white");    // top
}

// Draw candle
function drawCandle() {
    drawRectangle(245, 150, 10, 40, "red");
}

// Animate flame
function animateFlame() {
    let flameOn = true;

    setInterval(function() {
        ctx.beginPath();
        ctx.arc(250, 140, 8, 0, Math.PI * 2);
        ctx.fillStyle = flameOn ? "yellow" : "orange";
        ctx.fill();
        flameOn = !flameOn;
    }, 300);
}

// Write message
function writeMessage() {
    ctx.font = "30px Comic Sans MS";
    ctx.fillStyle = "purple";
    ctx.textAlign = "center";
    ctx.fillText("Happy Birthday!", 250, 80);
}

// Run animation
drawCake();
drawCandle();
animateFlame();
writeMessage();

</script>
""", height=420)
