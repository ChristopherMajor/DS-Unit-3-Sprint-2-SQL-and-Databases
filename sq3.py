"""contains solutions (in the development sense, a diet of copypasta 
doesn't make for strong programmers) for interactions with sqlite3 
databases
---
Extras:

Why does Brian have all sorts of different characters next to the 
octothorpe in his comments?

Better Comments extension allows you to get more mileage out of comments
by creating specific comment styles, which yield different color schemes
I consider it essential when in VS Code.
https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments



# ! PROTIP:
If something should normally get documentation, at the very least set 
aside the space for it, even better write something, anything for the 
time being even if its just \"\"\" simple query function \"\"\". In my 
small experience thus far while I might laugh at myself for silly 
docstrings when I read them weeks later I have never regretted a single 
one. What I do regret is when I come back to a clever function and it 
has 0 documentation accompanying it, and I then have to spend precious 
time discombobulating my spaghetti.

Code is only good if it can be used. Even the most clever function is 
useless if to implement it means deciphering the Rosetta stone.

# *Always a single space here then external imports first grouped by purpose or
# *library. Followed by any internal imports. Absolute paths > relative
# *paths every day of the week. Pythonic code is code that another dev
# *can skim through and make use of in seconds or minutes. Everything 
# *else is for your ego.
"""

#! Also I may be weird for this but I leave comments justifying my imports
from sqlite3 import connect, Row  # * sqlite3 db interaction
import pandas as pd  # * data formatting & manipulation

from .config import load_config

# These are super handy dandy as well especially in teams
# TODO average, how many Items does each Character have?
# TODO On average, how many Weapons does each character have?

sl3_config = load_config("sqlite")


class SqLiteHelper:
    """RPG SQLITE Database Helper
    """

    registered_queries = []
    registered_answers = []

    def __init__(self, db_path: str = None) -> None:
        self.db_path = db_path

    def register_query(self, query: str = None):
        """Register a query with the database helper
        
        Keyword Arguments:
            query {str} -- Query to register with the helper
            (default: {None})
        """
        self.registered_queries.append(query)

    def execute_query(self, query: str):
        db = connect(self.db_path)
        db.row_factory = Row
        cur = db.cursor()

        cur.execute(query)
        data = cur.fetchall()

        return pd.DataFrame(data, columns=data[0].keys()).to_string(index=False)

    def get_answer(self, query):
        self.registered_answers.append(self.execute_query(query))

    @property
    def print_answers(self):
        for ans in self.registered_answers:
            print(ans)
