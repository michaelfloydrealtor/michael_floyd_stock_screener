import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from indicators import sma, rsi

st.set_page_config(
    page_title="Michael Floyd's Stock Screener",
    page_icon="📈",           # optional, but looks great
    layout="wide"
)

# Personalized title
st.title("📈 Michael Floyd's Stock Screener")
st.write("A clean, professional stock analysis tool built by Michael Floyd.")

# User input for ticker selection
ticker = st.text_input("Enter a stock ticker:", "AAPL")

if st.button("Run Screener"):
    # Load 1 year of historical price data
    df = yf.download(ticker, period="1y")
    df.reset_index(inplace=True)

    # Apply indicators
    df = sma(df, 50)
    df = rsi(df, 14)

    st.subheader("📊 Latest Stock Data (Last 5 Days)")
    st.dataframe(df.tail(5))

    # Plot closing price and SMA50
    st.subheader("📉 Price Chart with SMA50")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df["Date"], df["Close"], label="Closing Price")
    ax.plot(df["Date"], df["SMA_50"], label="50-Day SMA", linestyle="--")
    ax.legend()
    st.pyplot(fig)

    # Plot RSI
    st.subheader("📉 RSI Indicator")
    fig2, ax2 = plt.subplots(figsize=(10, 2))
    ax2.plot(df["Date"], df["RSI"], label="RSI (14)", color="purple")
    ax2.axhline(70, color="red", linestyle="--", label="Overbought")
    ax2.axhline(30, color="green", linestyle="--", label="Oversold")
    ax2.legend()
    st.pyplot(fig2)

    st.success("Analysis completed successfully!")
