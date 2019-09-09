from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print("{}\n{}\n{}".format(ruby, python, visual_basic))

    programming_languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for programming_language in programming_languages:
        if programming_language.is_dynamic():
            print(programming_language.name)


main()
