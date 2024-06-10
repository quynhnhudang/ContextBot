import sqlite3

class KnowledgeBase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_answer(self, question):
        self.cursor.execute("SELECT answer FROM faq WHERE question=?", (question,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return "Sorry, I don't have an answer for that."

