import random
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)

images = [
    img.name
    for img in Path(app.static_folder or "./static").iterdir()
    if img.suffix.lower()
    in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg", ".avif"}
]


@app.route("/")
def index():
    random.shuffle(images)
    return render_template("index.html", images=images)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
