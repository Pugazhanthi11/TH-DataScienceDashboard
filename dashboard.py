import streamlit as st
import pandas as pd

# Load Dataset
df = pd.read_csv("featured_covid_data.csv")

# Dashboard Title
st.title("COVID-19 Dashboard")

st.write(
    "This dashboard displays insights from the COVID-19 dataset."
)

# Show Dataset
st.header("Dataset Preview")
st.dataframe(df.head())

# Summary Statistics
st.header("Summary Statistics")
st.write(df[['cases', 'deaths', 'recovered', 'active']].describe())

# Top Countries
st.header("Top 10 Countries by Cases")

top_cases = df[['country', 'cases']].sort_values(
    by='cases',
    ascending=False
).head(10)

st.bar_chart(
    top_cases.set_index('country')
)

# Feature Engineering Results
st.header("Feature Engineering Results")

st.dataframe(
    df[['country', 'death_rate', 'recovery_rate', 'active_rate']].head()
)

st.success("Dashboard loaded successfully!")