from flask import Flask, render_template, request

app = Flask(__name__)

# Quiz questions
questions = [
    {"question": "What’s your favorite activity?", "options": ["Reading", "Traveling", "Gaming", "Cooking"]},
    {"question": "Choose a color you like:", "options": ["Blue", "Red", "Green", "Yellow"]},
    {"question": "How do you spend your weekends?", "options": ["Relaxing", "Adventuring", "Learning", "Partying"]},
]

# Personality types and video links
personalities = {
    "Explorer": "static/explorer.mp4",
    "Thinker": "static/thinker.mp4",
    "Adventurer": "static/adventurer.mp4",
    "Socialite": "static/socialite.mp4",
}

@app.route("/")
def index():
    return render_template("index.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
    answers = request.form.getlist("answers")
    # Simple logic to determine personality
    personality = ""
    if "Traveling" in answers or "Adventuring" in answers:
        personality = "Explorer"
    elif "Reading" in answers or "Learning" in answers:
        personality = "Thinker"
    elif "Gaming" in answers or "Partying" in answers:
        personality = "Socialite"
    else:
        personality = "Adventurer"
    video_url = personalities.get(personality, "")
    return render_template("result.html", personality=personality, video_url=video_url)

if __name__ == "__main__":
    app.run(debug=True)
