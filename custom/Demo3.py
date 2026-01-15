import webbrowser
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    def QuestionBox(msg, btn):
        pass


try:
    QuestionBox(
        "This is the escrow panel of a Python contract. Here is where you can code all kinds of great things. "
        "There is no limit to how creative these contracts can be. For this demo, try to see how many points you and your counterparty can get in the Dogeminer game.",
        " OK ",
    )
    webbrowser.open("https://dogeminer.se/")
except Exception:
    pass
