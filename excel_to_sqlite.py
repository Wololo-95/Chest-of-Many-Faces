import pandas as pd
import sqlite3

arctic = pd.read_excel('encounter_sheets/arctic.ods', sheet_name='arctic', header=0)

con = sqlite3.connect("encounter_sheets/arctic.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE arctic (CR REAL, Monster TEXT NOT NULL, Xp INTEGER, Type TEXT NOT NULL)")

arctic.to_sql('arctic', con, if_exists='append', index=False)