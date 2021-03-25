# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:58:28 2020

@author: srerr
"""

import streamlit as st
import numpy as np

st.title('Streamlit application with columns')
data = np.random.randn(10, 1)
col1, col2, col3 = st.beta_columns(3)

col1.line_chart(data)
col2.write(data)
col3.text_input("Please put in some text", value = "Here you go")

st.write("Now this is at the end")
color = st.beta_color_picker('Pick a color')
st.write("The color is ", color)