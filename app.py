from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("cleaned_animes.csv")

@app.route("/random-anime")
def random_anime(): 
    random_df = df.sample(n=9)
    return jsonify(random_df.to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True, port=8000)