from flask import Flask, render_template, request

app = Flask(__name__)

# Quiz questions
questions = [
    {"question": "What’s your favorite activity?", "options": ["Reading", "Traveling", "Gaming", "Cooking"]},
    {"question": "Choose a color you like:", "options": ["Blue", "Red", "Green", "Yellow"]},
    {"question": "How do you spend your weekends?", "options": ["Relaxing", "Adventuring", "Learning", "Partying"]},
    {"question": "Which environment do you prefer?", "options": ["Mountains", "Beach", "City", "Countryside"]},
]

# Points assigned to each answer for personality types
personality_points = {
    "Explorer": {"Traveling", "Adventuring", "Beach", "City", "Yellow"},
    "Thinker": {"Reading", "Learning", "Blue", "Mountains"},
    "Socialite": {"Gaming", "Partying", "Red", "City"},
    "Adventurer": {"Cooking", "Relaxing", "Green", "Countryside"},
}

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
    
    # Check if the user has answered all the questions
    if len(answers) < len(questions):
        # Redirect back to the quiz with an error message
        return render_template(
            "index.html", 
            questions=questions, 
            error="Please answer all the questions before submitting!"
        )
    
    # Initialize scores for each personality type
    scores = {personality: 0 for personality in personalities.keys()}

    # Assign points based on answers
    for answer in answers:
        for personality, traits in personality_points.items():
            if answer in traits:
                scores[personality] += 1

    # Determine the personality with the highest score
    personality = max(scores, key=scores.get)

    # Get the video URL for the determined personality
    video_url = personalities.get(personality, "")
    return render_template("result.html", personality=personality, video_url=video_url)

if __name__ == "__main__":
    app.run(debug=True)
