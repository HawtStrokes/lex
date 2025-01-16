from flask import Blueprint, render_template, request, jsonify
from .utils.inference_engine import run_inference

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_data = request.form["data"]
        result = run_inference(user_data)
        return jsonify({"inference": result})

    return render_template("index.html")

