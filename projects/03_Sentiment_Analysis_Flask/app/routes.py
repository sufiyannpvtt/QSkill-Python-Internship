from flask import Blueprint, render_template, request, jsonify
from app.nlp.sentiment_engine import analyze_sentiment

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/how-it-works")
def how_it_works():
    return render_template("how_it_works.html")

@main.route("/api-docs")
def api_docs():
    return render_template("api_docs.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json()
    text = data.get("text", "")
    return jsonify(analyze_sentiment(text))
