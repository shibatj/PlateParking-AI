import requests
from datetime import datetime
import sqlite3

url = "https://api.aiforthai.in.th/lpr-v2"
payload = {'crop': '1', 'rotate': '1'}
files = {'image': open('img/1.jpg','rb')}
headers = {'Apikey': "CWE1H6FszNEK276yVQSuJ4NRFsm2FiS4"}

response = requests.post(url, files=files, data=payload, headers=headers)
data = response.json()
print("Data is : ", data[0]['lpr'])

conn = sqlite3.connect('database\license_plates.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS plates (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PlateNumber TEXT UNIQUE,
    TimeIn TEXT,
    TimeOut TEXT
)
''')

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
license_plate_number = data[0]['lpr']

c.execute('SELECT * FROM plates WHERE PlateNumber = ?', (license_plate_number,))
result = c.fetchone()

if result:
    print("Plate Add Fail")
else:
    c.execute('INSERT INTO plates (PlateNumber, TimeIn) VALUES (?, ?)', (license_plate_number, current_time))
    conn.commit()
    print("Plate Added")

conn.close()

