from flask import Flask

import json


app = Flask(__name__)


with open("candidates.json", "r", encoding="utf-8") as file:
    data = json.load(file)


@app.route("/")
def page_index():
    page = ""
    for i in data:
        page += "Имя кандидата - " + i["name"] + "\n"
        page += "Позиция кандидата - " + i["position"] + "\n"
        page += "Навыки через запятую - " + i["skills"] + "\n"
        page += "\n"

    return "<pre>" + page + "<pre>"


@app.route("/candidates/<int:user_id>")
def page_candidates(user_id):
    page = ""
    for i in data:
        if user_id == i["id"]:
            page += "Имя кандидата - " + i["name"] + "\n"
            page += "Позиция кандидата - " + i["position"] + "\n"
            page += "Навыки через запятую - " + i["skills"] + "\n"

            return "<img src=" + i["picture"] + ">" + "\n" + "<pre>" + page + "</pre>"


@app.route("/skills/<skill>")
def page_skills(skill):
    page = ""
    for i in data:
        skills_list = i["skills"].split(",")
        for item in skills_list:
            if skill == item.lower():
                page += "Имя кандидата - " + i["name"] + "\n"
                page += "Позиция кандидата - " + i["position"] + "\n"
                page += "Навыки через запятую - " + i["skills"] + "\n"
                page += "\n"

    return "<pre>" + page + "<pre>"


app.run()
