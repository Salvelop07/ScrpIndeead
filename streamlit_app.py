from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud

st.set_page_config(
    page_title="indeed-municipality-reviews",
    page_icon=":speaking_head_in_silhouette:",
)
_, center, _ = st.columns([2, 1, 2])
with center:
    st.image(
        "https://cdn2.iconfinder.com/data/icons/essential-web-4/50/commenting-more-typing-chat-review-512.png",
        use_column_width=True,
    )
st.title("indeed-municipality-reviews")
st.caption("A Streamlit app to showcase municipality reviews from Indeed")


data = Path("data")
city = st.selectbox(
    "municipalities",
    list(data.glob("reviews_*.json")),
)

df = pd.read_json(city)
df = df.drop_duplicates(["id"])
df["year"] = df.apply(lambda r: int(r["date_created"].split(" ")[-1]), axis=1)
st.dataframe(df)

wc_config = {
    "background_color": "white",
    "width": 800,
    "height": 600,
    "max_words": 200,
    "max_font_size": 40,
}

st.subheader("WordCloud")
fig = plt.figure()
wc = WordCloud(**wc_config).generate("\n".join(df.text))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
st.pyplot(fig)

st.subheader("Countplot - Year")
fig = plt.figure()
sns.countplot(x="year", data=df)
st.pyplot(fig)

st.subheader("Countplot - Rating")
fig = plt.figure()
sns.countplot(x="rating", data=df)
st.pyplot(fig)

st.subheader("Countplot - Year over Rating")
fig = plt.figure()
sns.countplot(x="year", hue="rating", data=df)
st.pyplot(fig)

st.subheader("Countplot - Rating over Year")
fig = plt.figure()
sns.countplot(x="rating", hue="year", data=df)
st.pyplot(fig)
