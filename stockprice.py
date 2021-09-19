import yfinance as yf
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ETF-Charts", page_icon=":bar_chart:", layout="wide")

option = st.sidebar.selectbox("Welcher ETF?", ('World', 'EM', 'ESPO'))
clovol = ['Schlusskurs', 'Volumen', 'Schlusskurs & Volumen']


if option == 'World':
    st.write("""
    # iShares MSCI World
    """)

    tickerSymbol = 'URTH'
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1m', start='2015-1-1', end='2020-8-31')

    page = st.radio('Schlusskurs oder Volumen?', clovol)
    st.write("""
    
    """)

    if page == 'Schlusskurs':
        st.line_chart(tickerDf.Close)
    elif page == 'Volumen':
        st.line_chart(tickerDf.Volume)
    else:
        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)

if option == 'EM':
    st.write("""
    # Lyxor MSCI Emerging Markets
    """)

    tickerSymbol = 'E127.DE'
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='1m', start='2015-1-1', end='2020-8-31')

    page = st.radio('Schlusskurs oder Volumen?', clovol)
    st.write("""
    
    """)

    if page == 'Schlusskurs':
        st.line_chart(tickerDf.Close)
    elif page == 'Volumen':
        st.line_chart(tickerDf.Volume)
    else:
        st.line_chart(tickerDf.Close)
        st.line_chart(tickerDf.Volume)




