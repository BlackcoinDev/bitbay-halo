from typing import TYPE_CHECKING

if TYPE_CHECKING:
    firstform = 1
    showform = 1
    acceptform = 1

    def QuestionBox(msg, btn):
        pass


try:
    x = firstform + 1
    QuestionBox(
        "Welcome to your quick tutorial on Python contracts! This is where you can customize your offer forms. This area is for your initial forms when constructing the contract.",
        " OK ",
    )
except:
    pass
try:
    x = showform + 1
    QuestionBox("Here is where the coder can customize all of his forms for interacting with offers and contracts.", " OK ")
except:
    pass
try:
    x = acceptform + 1
    QuestionBox(
        "Here is where the coder can set all of the rules for accepting and countering offers in Python contracts.",
        " OK ",
    )
except:
    pass
