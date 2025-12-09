
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("fema_small.csv")

st.title("FEMA Disaster Relief Dashboard")
st.write("Creator: Claytis Egbulem")

st.subheader("Histogram of Repair Amount")
fig1 = px.histogram(df, x="repairAmount", nbins=40)
st.plotly_chart(fig1)

st.subheader("Boxplot: Repair Amount by TSA Eligibility")
fig2 = px.box(df, x="tsaEligible", y="repairAmount")
st.plotly_chart(fig2)



