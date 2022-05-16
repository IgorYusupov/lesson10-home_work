from flask import Flask

import visualizer

import utils


app = Flask(__name__)


@app.route("/")
def page_all_candidates():
    candidates = utils.candidates_get_all()
    html_code = visualizer.build_html_for_some_candidates(candidates)

    return html_code


@app.route("/skills/<skill>")
def page_candidates_by_skill(skill):
    candidates = utils.candidates_get_by_skill(skill)

    if len(candidates) == 0:

        return "Таких кандидатов нет"

    html_code = visualizer.build_html_for_some_candidates(candidates)

    return html_code


@app.route("/candidates/<int:pk>")
def page_candidates_by_pk(pk):
    candidate = utils.candidates_get_by_pk(pk)

    if candidate is None:
        return "Такого кандидата нет"

    html_code = visualizer.build_html_for_one_candidate(candidate)
    return html_code


if __name__ == "__main__":
    app.run()
