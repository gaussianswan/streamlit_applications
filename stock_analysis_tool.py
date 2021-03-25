# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 21:23:46 2020

@author: srerr
"""

import streamlit as st
import pandas as pd 
import numpy as np
import yfinance as yf

st.title("Stock analysis tool")

ticker = st.text_input("Put in a ticker you want to see")
@st.cache
def download(ticker): 
    data = yf.download(ticker)
    return(data)

data = download(ticker)

st.write(data)

st.line_chart(data['Close'])