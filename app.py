import pandas as pd
from flask import Flask, render_template, request

resume_data = pd.read_csv("cleaned_resume.csv")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        skills = request.form.get("skills")
        skills_list = [
            skill.strip() for skill in skills.split(",")
        ] 
        filtered_resumes = resume_data
        for skill in skills_list:
            filtered_resumes = filtered_resumes[
                filtered_resumes["Cleaned_Resume"].str.contains(skill, case=False)
            ]
        return render_template("result.html", resumes=filtered_resumes)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
