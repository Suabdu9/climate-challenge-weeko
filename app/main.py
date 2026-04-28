import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="Climate Dashboard", layout="wide")
st.title("🌍 Climate Comparison Dashboard")

# -----------------------
# GOOGLE DRIVE LINKS
# -----------------------
drive_links = {
    "Ethiopia": "https://drive.google.com/uc?id=1Mv9tkVgRMz3O3Pa7LMMtC6y85GDoydB2",
    "Kenya": "https://drive.google.com/uc?id=14-yg9tImS4yVveJm8gc_ZlSjS2lcjPjB",
    "Sudan": "https://drive.google.com/uc?id=1b8qFKKGkZIc0SgsL9ts41z6qecxq4ejo",
    "Tanzania": "https://drive.google.com/uc?id=1HfnpyS-sTMA5SlItPjtNafjfTkZRIsmW",
    "Nigeria": "https://drive.google.com/uc?id=18xvYOiizqDdoMRJt0879EAIUX8qzz6Yq",
}

# -----------------------
# LOAD DATA FUNCTION
# -----------------------
@st.cache_data
def load_data(countries, sample_only=True, sample_rows=5000):
    frames = []

    for country in countries:

        # ---------- TRY LOCAL FIRST ----------
        local_path = f"data/{country.lower()}_clean.csv"

        if os.path.exists(local_path):
            try:
                df = pd.read_csv(local_path)
                df["Country"] = country
                frames.append(df)
                continue
            except Exception as e:
                st.warning(f"Local load failed for {country}: {e}")

        # ---------- FALLBACK TO DRIVE ----------
        try:
            url = drive_links[country]
            df = pd.read_csv(url)

            if sample_only:
                df = df.head(sample_rows)

            df["Country"] = country
            frames.append(df)

        except Exception as e:
            st.warning(f"Drive load failed for {country}: {e}")

    if len(frames) == 0:
        return pd.DataFrame()

    df = pd.concat(frames, ignore_index=True)

    # Date processing
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = df["Date"].dt.year

    return df

# -----------------------
# SIDEBAR
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
    st.error("No data could be loaded. Check local files or Google Drive links.")
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