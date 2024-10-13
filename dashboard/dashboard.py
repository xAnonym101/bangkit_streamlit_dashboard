import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


days_data = pd.read_csv("dashboard\alldata.csv", delimiter=",")
days_data["dteday"] = pd.to_datetime(days_data["dteday"])        
        
def create_minMax_data(df):
    minMax_df = df.groupby(by="season").agg({
    "instant": "nunique",
    "cnt": ["max", "min"]
    }, inplace=True).reset_index()
    return minMax_df

def create_borrower_data(df):
    borrower_df = df.groupby(by="workingday").agg({
    "instant": "nunique",
    "registered": "mean",
    "casual": "mean"
    }, inplace=True)
    return borrower_df

minMax_data = create_minMax_data(days_data)
filtered_minMax_data = minMax_data.loc[minMax_data["season"].isin([1,4])]
borrower_data = create_borrower_data(days_data)

tab1, tab2 = st.tabs(["Question 1", "Question 2"])
with tab1:
    fig_min, ax_min = plt.subplots(figsize=(8, 6))
    ax_min.bar(["Spring", "Winter"], filtered_minMax_data[("cnt", "min")], color="#FF5733")
    ax_min.set_xlabel("Season", fontsize=12)
    ax_min.set_ylabel("Minimum Count", fontsize=12)
    ax_min.set_title("Minimum Counts per Season", fontsize=14)
    st.subheader("Minimum Counts per Season")
    st.pyplot(fig_min)
    
    fig_max, ax_max = plt.subplots(figsize=(8, 6))
    ax_min.bar(["Spring", "Winter"], filtered_minMax_data[("cnt", "max")], color="#FF5733")
    ax_min.set_xlabel("Season", fontsize=12)
    ax_min.set_ylabel("Maximum Count", fontsize=12)
    ax_min.set_title("Maximum Counts per Season", fontsize=14)
    st.subheader("Maximum Counts per Season")
    st.pyplot(fig_min) 
with tab2:
    fig_min, ax_min = plt.subplots(figsize=(8, 6))
    ax_min.bar(["Spring", "Winter"], borrower_data["registered"], color="#FF5733")
    ax_min.set_xlabel("Season", fontsize=12)
    ax_min.set_ylabel("Minimum Count", fontsize=12)
    ax_min.set_title("Minimum Counts per Season", fontsize=14)

    st.subheader("Minimum Counts per Season")
    st.pyplot(fig_min)