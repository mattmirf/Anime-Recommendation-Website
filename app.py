from flask import Flask, render_template, url_for, request
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("cleaned_animes.csv")

# Page
@app.route("/random-anime")
def random_anime(): 
    anime_list = df.sample(n=6)
    anime_list = anime_list.to_dict(orient='records')

    anime_list = clean_alternative_titles(anime_list)

    return render_template('index.html', anime=anime_list)

@app.route("/home")
def anime():
    query = request.args.get("search","").lower()
    if query:
        anime_searched = df[df["title"].str.lower().str.contains(query, na=False)]
        anime_list = anime_searched.to_dict(orient="records")
        anime_list = clean_alternative_titles(anime_list)
    else:
        anime_list = []

    
    return render_template('index1.html', anime=anime_list,query=query)

def clean_alternative_titles(clean_list):
    for data in clean_list:
        if pd.isna(data.get("alternative_title")):
            data["alternative_title"] = ""
    return clean_list

if __name__ == '__main__':
    app.run(debug=True, port=8000)