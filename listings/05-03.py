import sqlite3
from datetime import datetime


class LogVisit:
    """ユーザーの訪問ログを記録するクラス"""
    def __init__(self, db_connection):
        """コンストラクタ

        Args:
            db_connection : データベース接続オブジェクト
        """
        self._db = db_connection

    def execute(self, user_id, visited_on):
        """訪問ログを記録する

        Notes:
            ユーザーの最終訪問日時を更新し、訪問ログを記録する
            もし、エラーが発生した場合は、ロールバックする
        """
        try:
            self._db.execute("BEGIN TRANSACTION")

            self._db.execute("UPDATE Users SET last_visit=? WHERE user_id=?", (visited_on, user_id))
            self._db.execute("INSERT INTO VisitsLog(user_id, visit_date) VALUES(?, ?)", (user_id, visited_on))

            self._db.execute("COMMIT")
        except Exception as e:
            self._db.execute("ROLLBACK")
            raise e


if __name__ == '__main__':
    # データベース接続の作成
    conn = sqlite3.connect('example.db')
    log_visit = LogVisit(conn)

    # サンプルデータ
    user_id = 'some-unique-user-id'
    visited_on = datetime.now()

    # 実行
    log_visit.execute(user_id, visited_on)
