import sqlite3

file_name = "note.db"

def connect():
   
    conn = sqlite3.connect(file_name)
    cursor = conn.cursor()
   
    cursor.execute("""CREATE TABLE IF NOT EXISTS TASK(
                   id_no INTEGER PRIMARY KEY AUTOINCREMENT,
                   task TEXT NOT NULL,
                   status TEXT NOT NULL
                   )
""")
    
    conn.commit()
    conn.close()

connect()    