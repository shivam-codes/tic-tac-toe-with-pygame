import sqlite3

conn = sqlite3.connect('scores.s3db')
cur = conn.cursor()

cur.execute('CREATE TABLE if not exists score (id INTEGER, player TEXT, scores INTEGER DEFAULT  0);')
conn.commit()

def insert_score(player, val):
    cursor = conn.execute('SELECT id, player, scores from score')
    count = 0
    #print(player, val)
    cur.execute('SELECT COUNT(*) from score')
    coun = cur.fetchall()[0][0]
    print(coun)
    if coun < 5:
        sqlcommand = 'INSERT INTO score (id, player, scores) values (?,?,?)'
        data = (1, player, val)
        cur.execute(sqlcommand, data)
        conn.commit()
    else:
        for data in cursor:
            #print(data[0], data[1], data[2])
            if val > data[2]:
                cur.execute('DELETE from score where scores=data[2]')
                sqlcommand = 'INSERT INTO score (id, player, scores) values (?,?,?)'
                data = (1, player, val)
                cur.execute(sqlcommand, data)
                conn.commit()
def display():
    cursor = conn.execute('SELECT id, player, scores from score')
    list = []
    for data in cursor:
        list.append([data[1], data[2]])
        print(data[1], data[2])
    return list




