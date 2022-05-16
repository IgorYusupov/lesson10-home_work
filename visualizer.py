def build_html_for_one_candidate(candidate):
    """
    Формируем html файл для одного кандидата
    """
    code_of_candidate = ""

    code_of_candidate += f"<img src=\'{candidate['picture']}\'>\n"
    code_of_candidate += f"Имя кандидата - {candidate['name']}\n"
    code_of_candidate += f"Позиция кандидата - {candidate['position']}\n"
    code_of_candidate += f"Навыки через запятую - {candidate['skills']}\n"
    code_of_candidate += "\n"

    return "<pre>" + code_of_candidate + "<pre>"


def build_html_for_some_candidates(candidates):
    """
    Формируем html файл для всех кандидатов
    """
    code_of_candidates = ""

    for candidate in candidates:
        code_of_candidates += f"Имя кандидата - {candidate['name']}\n"
        code_of_candidates += f"Позиция кандидата - {candidate['position']}\n"
        code_of_candidates += f"Навыки через запятую - {candidate['skills']}\n"
        code_of_candidates += "\n"

    return "<pre>" + code_of_candidates + "<pre>"
