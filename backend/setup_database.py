import sqlite3

conn = sqlite3.connect('knowledge_base.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE faq (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Insert sample data
cursor.execute('''
INSERT INTO faq (question, answer) VALUES 
('What is the capital of France?', 'Paris'),
('What is the largest planet in our solar system?', 'Jupiter')
''')

conn.commit()
conn.close()
