import sqlite3
import pandas as pd

import util.project_resource_path as project_resource_path

# 1. CSV 읽기
if __name__ == "__main__":
    df = pd.read_csv(project_resource_path.project_path+'/csv_file/student_performance.csv')

    # 2. DB 연결
    conn = sqlite3.connect(project_resource_path.project_path+'/fastdb.db')


    # 3. 데이터 로드 (if_exists='append' 사용)
    try:
        df.to_sql('student_stats', conn, if_exists='replace', index=False)
        print("DB 로드 성공!")
    except Exception as e:
        print(f"에러 발생: {e}")

    conn.close()