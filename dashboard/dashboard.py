import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

days_data = pd.read_csv("dashboard/day_data.csv", delimiter=",")
days_data["dteday"] = pd.to_datetime(days_data["dteday"])
hours_data = pd.read_csv("dashboard/hour_data.csv", delimiter=",")
hours_data["dteday"] = pd.to_datetime(hours_data["dteday"])  
        
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
borrowerD_data = create_borrower_data(days_data)
borrowerH_data = create_borrower_data(hours_data)



tab1, tab2 = st.tabs(["Question 1", "Question 2"])
with tab1:
    fig_min, ax_min = plt.subplots(figsize=(8, 6))
    bars_min = ax_min.bar(["Spring", "Winter"], filtered_minMax_data[("cnt", "min")], color=["#ABD8E6", "#D3D3D3"])
    ax_min.set_xlabel("Season", fontsize=12)
    ax_min.set_ylabel("Minimum Count", fontsize=12)
    ax_min.set_title("Minimum Counts per Season", fontsize=14)
    for bar in bars_min:
        yval = bar.get_height()
        ax_min.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=10)
    st.subheader("Minimum Counts per Season")
    st.pyplot(fig_min)
    
    fig_max, ax_max = plt.subplots(figsize=(8, 6))
    bars_max = ax_max.bar(["Spring", "Winter"], filtered_minMax_data[("cnt", "max")], color=["#ABD8E6", "#D3D3D3"])
    ax_max.set_xlabel("Season", fontsize=12)
    ax_max.set_ylabel("Maximum Count", fontsize=12)
    ax_max.set_title("Maximum Counts per Season", fontsize=14)
    for bar in bars_max:
        yval = bar.get_height()
        ax_max.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=10)
    st.subheader("Maximum Counts per Season")
    st.pyplot(fig_max) 
with tab2:
    fig_day, ax_day = plt.subplots(figsize=(8, 6))
    bars_day = ax_day.bar(["Weekend", "Weekday"], borrowerD_data["registered"], color=["#90CAF9", "#FF5733"])
    ax_day.set_xlabel("Day Type", fontsize=12)
    ax_day.set_ylabel("Value", fontsize=12)
    ax_day.set_title("Comparison of Licensed Borrowers Between Weekday and Weekend", fontsize=14)
    for bar in bars_day:
        yval = bar.get_height()
        ax_day.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=10)
    st.subheader("Comparison of Licensed Borrowers (Data/Days)")
    st.pyplot(fig_day)
    
    fig_hour, ax_hour = plt.subplots(figsize=(8, 6))
    bars_hour = ax_hour.bar(["Weekend", "Weekday"], borrowerH_data["registered"], color=["#90CAF9", "#FF5733"])
    ax_hour.set_xlabel("Day Type", fontsize=12)
    ax_hour.set_ylabel("Value", fontsize=12)
    ax_hour.set_title("Comparison of Licensed Borrowers Between Weekday and Weekend", fontsize=14)
    for bar in bars_hour:
        yval = bar.get_height()
        ax_hour.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), va='bottom', ha='center', fontsize=10)
    st.subheader("Comparison of Licensed Borrowers (Data/Hours)")
    st.pyplot(fig_hour)
