import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# LOAD DATA
# -----------------------
@st.cache_data
def load_data():
    ethiopia = pd.read_csv("data/ethiopia_clean.csv")
    kenya = pd.read_csv("data/kenya_clean.csv")
    sudan = pd.read_csv("data/sudan_clean.csv")
    tanzania = pd.read_csv("data/tanzania_clean.csv")
    nigeria = pd.read_csv("data/nigeria_clean.csv")

    datasets = {
        "Ethiopia": ethiopia,
        "Kenya": kenya,
        "Sudan": sudan,
        "Tanzania": tanzania,
        "Nigeria": nigeria
    }

    df_list = []
    for country, data in datasets.items():
        data["Country"] = country
        df_list.append(data)

    df = pd.concat(df_list)
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year

    return df

df = load_data()

# -----------------------
# TITLE
# -----------------------
st.title("🌍 Climate Comparison Dashboard")

# -----------------------
# SIDEBAR FILTERS
# -----------------------
countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR"]
)

# -----------------------
# FILTER DATA
# -----------------------
filtered_df = df[
    (df["Country"].isin(countries)) &
    (df["Year"].between(year_range[0], year_range[1]))
]

# -----------------------
# TEMPERATURE TREND
# -----------------------
st.subheader("Temperature Trend")

temp = filtered_df.groupby(["Date", "Country"])["T2M"].mean().reset_index()
pivot = temp.pivot(index="Date", columns="Country", values="T2M")

st.line_chart(pivot)

# -----------------------
# PRECIPITATION BOXPLOT
# -----------------------
st.subheader("Precipitation Distribution")

fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x="Country", y="PRECTOTCORR", ax=ax)
st.pyplot(fig)