#%%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from tqdm import tqdm
from wordcloud import WordCloud


data = Path("data")
result = Path("result")
static = Path("static")
result.mkdir(exist_ok=True)


def custom_read_json(json_file):
    company = json_file.stem.lstrip("reviews_")
    df = pd.read_json(json_file)
    df["company"] = [company] * df.shape[0]
    return df


try:
    df = pd.concat(
        map(custom_read_json, data.glob("reviews_*.json")), ignore_index=True
    )
except ValueError:
    raise
else:
    df = df.drop_duplicates(["id"])
    df = df.assign(
        year=df.apply(lambda r: int(r["date_created"].split(" ")[-1]), axis=1)
    )
    companies = df["company"].unique()

#%%
for company in tqdm(companies):
    data = df[df["company"] == company]

    plt.clf()
    wc_config = {
        "background_color": "white",
        "width": 800,
        "height": 600,
        "max_words": 200,
        "max_font_size": 40,
    }
    text = "\n".join(data.text)
    wc = WordCloud(**wc_config).generate(text)
    fig = plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    fig.savefig(result / f"{company}-wordcloud", bbox_inches="tight", dpi=300)
    fig.savefig(static / f"{company}-wordcloud", bbox_inches="tight", dpi=300)

    plt.clf()
    ax = sns.countplot(x="rating", data=data)
    ax.get_figure().savefig(result / f"{company}-countplot-rating", dpi=300)

    plt.clf()
    ax = sns.countplot(x="year", data=data)
    ax.get_figure().savefig(result / f"{company}-countplot-year", dpi=300)

    plt.clf()
    ax = sns.countplot(x="year", hue="rating", data=data)
    plt.legend(loc="upper left")
    ax.get_figure().savefig(result / f"{company}-countplot-year-per-rating", dpi=300)
    ax.get_figure().savefig(static / f"{company}-countplot-year-per-rating", dpi=300)

    plt.clf()
    ax = sns.countplot(x="rating", hue="year", data=data)
    plt.legend(loc="upper left")
    ax.get_figure().savefig(result / f"{company}-countplot-rating-per-year", dpi=300)
    ax.get_figure().savefig(static / f"{company}-countplot-rating-per-year", dpi=300)

#%%
plt.clf()
ax = sns.barplot(
    x="company", y="rating", data=df.groupby("company").mean().reset_index()
)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", fontsize=7)
ax.get_figure().savefig(
    result / f"overall-countplot-rating", bbox_inches="tight", dpi=300
)
ax.get_figure().savefig(
    static / f"overall-countplot-rating", bbox_inches="tight", dpi=300
)
