def is_valid_id(student_id: str) -> bool:
    # to check if it's not blank and that it is numbers & letters
    return student_id.strip() != "" and student_id.isalnum()


def is_valid_name(name: str) -> bool:
    # alphabetical & no space
    return name.strip() != "" and all(x.isalpha() or x.isspace() for x in name)


def is_valid_department(dept: str) -> bool:
    # alphabetical & no space
    return dept.strip() != "" and all(d.isalpha() or d.isspace() for d in dept)


def is_valid_marks(marks: str) -> bool:
    try:
        value = float(marks)
        return 0 <= value <= 100
    except ValueError:
        return False


def is_valid_thesis(thesis: str) -> bool:
    return thesis.strip() != ""


def is_valid_choice(choice: str, options: list) -> bool:
    return choice.isdigit() and int(choice) in options
