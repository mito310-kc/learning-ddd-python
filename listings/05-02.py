import sqlite3
from datetime import datetime


class LogVisit:
    def __init__(self, db_connection):
        self._db = db_connection

    def execute(self, user_id, visited_on):
        self._db.execute("UPDATE Users SET last_visit=? WHERE user_id=?", (visited_on, user_id))
        self._db.execute("INSERT INTO VisitsLog(user_id, visit_date) VALUES(?, ?)", (user_id, visited_on))


if __name__ == '__main__':
    # データベース接続の作成
    conn = sqlite3.connect('example.db')
    log_visit = LogVisit(conn)

    # サンプルデータ
    user_id = 'some-unique-user-id'
    visited_on = datetime.now()

    # 実行
    log_visit.execute(user_id, visited_on)
