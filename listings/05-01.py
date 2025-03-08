import json
import xml.etree.ElementTree as ET


class DB:
    @staticmethod
    def start_transaction():
        print("Transaction started")

    @staticmethod
    def load_next_job():
        # ダミーデータを返す
        return {"Source": "source.json", "Destination": "destination.xml"}

    @staticmethod
    def mark_job_as_completed(job):
        print(f"Job {job} marked as completed")

    @staticmethod
    def commit():
        print("Transaction committed")


def load_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def convert_json_to_xml(json_obj):
    root = ET.Element("root")
    for key, value in json_obj.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    return ET.ElementTree(root)


def write_file(filepath, xml_tree):
    xml_tree.write(filepath)


if __name__ == "__main__":
    # トランザクション開始
    DB.start_transaction()

    # 次のジョブをロード
    job = DB.load_next_job()

    # ファイルをロード
    json_data = load_file(job["Source"])

    # JSONをXMLに変換
    xml_data = convert_json_to_xml(json_data)

    # ファイルに書き込み
    write_file(job["Destination"], xml_data)

    # ジョブを完了としてマーク
    DB.mark_job_as_completed(job)

    # トランザクションをコミット
    DB.commit()
