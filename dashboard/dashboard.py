import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_total_df(df):
    total_df = df.groupby(by="dteday").agg({"cnt": "sum"}).reset_index()
    total_df.rename(columns={
        "dteday": "date",
        "cnt": "total_count"
    }, inplace=True)
    return total_df

def create_registered_df(df):
    registered_df = df.groupby(by="dteday").agg({"registered": "sum"}).reset_index()
    registered_df.rename(columns={
        "dteday": "date",
    }, inplace=True)
    return registered_df

def create_casual_df(df):
    casual_df = df.groupby(by="dteday").agg({"casual": "sum"}).reset_index()
    casual_df.rename(columns={
        "dteday": "date",
    }, inplace=True)
    return casual_df


days_data = pd.read_csv("dashboard/alldata.csv", delimiter=",")
days_data["dteday"] = pd.to_datetime(days_data["dteday"])
days_data.sample(n=10)

min_date = days_data["dteday"].min()
max_date = days_data["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image(r"dashboard/calendar_image.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
    
main_days = days_data[(days_data["dteday"] >= str(start_date)) & 
                (days_data["dteday"] <= str(end_date))]
    
total_data = create_total_df(main_days)
registered_data = create_registered_df(main_days)
casual_data = create_casual_df(main_days)
    
st.header('Graph of Bicycle Borrowers :chart:')

fig, ax = plt.subplots(figsize=(16, 8))
st.subheader('Total Borrowers')
ax.plot(
    total_data["date"],
    total_data["total_count"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)
col1, col2 = st.columns(2)
with col1:
    total_max = total_data["total_count"].max()
    st.metric("Maximum", value=total_max)
with col2:
    total_min = total_data["total_count"].min()
    st.metric("Minimum", value=total_min)

tab1, tab2 = st.tabs(["Registered Borrowers", "Casual Borrowers"])
with tab1:
    fig,ax = plt.subplots(figsize=(16,8))
    st.subheader("Registered Borrowers")
    ax.plot(
        registered_data["date"],
        registered_data["registered"],
        marker="o",
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)
    col1, col2 = st.columns(2)
    with col1:
        registered_max = registered_data["registered"].max()
        st.metric("Maximum", value=registered_max)
    with col2:
        registered_min = registered_data["registered"].min()
        st.metric("Minimum", value=total_min)
with tab2:
    fig,ax = plt.subplots(figsize=(16,8))
    st.subheader("Casual Borrowers")
    ax.plot(
        casual_data["date"],
        casual_data["casual"],
        marker="o",
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)
    col1, col2 = st.columns(2)
    with col1:
        casual_max = casual_data["casual"].max()
        st.metric("Maximum", value=casual_max)
    with col2:
        casual_min = casual_data["casual"].min()
        st.metric("Minimum", value=casual_min)
        