import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="Climate Dashboard", layout="wide")

# -----------------------
# TITLE
# -----------------------
st.title("🌍 Climate Comparison Dashboard")

# -----------------------
# LOAD DATA FUNCTION
# -----------------------
@st.cache_data
def load_data(countries, data_dir="data", sample_only=False, sample_rows=5000):
    df_list = []

    file_map = {
        "Ethiopia": "ethiopia_clean.csv",
        "Kenya": "kenya_clean.csv",
        "Sudan": "sudan_clean.csv",
        "Tanzania": "tanzania_clean.csv",
        "Nigeria": "nigeria_clean.csv"
    }

    for country in countries:
        file_path = os.path.join(data_dir, file_map[country])

        try:
            df = pd.read_csv(file_path)

            if sample_only:
                df = df.head(sample_rows)

            df["Country"] = country
            df_list.append(df)

        except FileNotFoundError:
            st.warning(f"{country} data not found in {data_dir}")

    if len(df_list) == 0:
        return pd.DataFrame()

    df = pd.concat(df_list)

    # Date processing
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year

    return df

# -----------------------
# SIDEBAR FILTERS
# -----------------------
all_countries = ["Ethiopia", "Kenya", "Sudan", "Tanzania", "Nigeria"]

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=all_countries,
    default=all_countries
)

sample_only = st.sidebar.checkbox("Use sample data", value=True)

# -----------------------
# LOAD DATA
# -----------------------
df = load_data(selected_countries, sample_only=sample_only)

# -----------------------
# HANDLE EMPTY DATA
# -----------------------
if df.empty:
    st.error("No data found. Ensure CSV files exist in the data/ directory.")
    st.stop()

# -----------------------
# YEAR FILTER
# -----------------------
year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (int(df["Year"].min()), int(df["Year"].max()))
)

df = df[df["Year"].between(year_range[0], year_range[1])]

# -----------------------
# TEMPERATURE TREND
# -----------------------
st.subheader("🌡️ Temperature Trend (T2M)")

temp = df.groupby(["Date", "Country"])["T2M"].mean().reset_index()
pivot_temp = temp.pivot(index="Date", columns="Country", values="T2M")

st.line_chart(pivot_temp)

# -----------------------
# PRECIPITATION BOXPLOT
# -----------------------
st.subheader("🌧️ Precipitation Distribution (PRECTOTCORR)")

fig, ax = plt.subplots()
sns.boxplot(data=df, x="Country", y="PRECTOTCORR", ax=ax)
ax.set_xlabel("Country")
ax.set_ylabel("Precipitation")
st.pyplot(fig)

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")
st.caption("Climate Analysis Dashboard — KAIM Week 0")