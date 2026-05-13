# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request, redirect
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r",encoding="utf-8") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE


@app.route("/")	
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")

    if keyword == None:
        return redirect("/")

    jobs = load_jobs()
    filtered_jobs = []

    for job in jobs:
        title = job["title"].lower()
        company = job["company_name"].lower()
        description = job["description"].lower()

        if (
            keyword.lower() in title
            or keyword.lower() in company
            or keyword.lower() in description
        ):
            filtered_jobs.append(job)

    return render_template(
        "search.html",
        keyword=keyword,
        jobs=filtered_jobs
    )


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT