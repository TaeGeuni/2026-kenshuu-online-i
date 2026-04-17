# [KR] 날짜와 시간 정보를 다루기 위해 datetime 모듈을 불러옵니다.
# [JP] 日付と時間情報を扱うためにdatetimeモジュールをインポートします。
import datetime

# [KR] datetime.datetime.now()를 사용하여 현재 컴퓨터의 날짜와 시간 정보를 가져옵니다.
# [JP] datetime.datetime.now()を使用して、現在コンピューターの日付と時刻情報を取得します。
now = datetime.datetime.now()

# [KR] strftime()을 사용하여 가져온 시간 정보를 'YYYY-MM-DD HH:MM:SS' 형식의 문자열로 변환합니다.
# [JP] strftime()を使用して、取得した時間情報を 'YYYY-MM-DD HH:MM:SS' 形式の文字列に変換します。
# 💡Point: %Y(연도 4자리), %m(월), %d(일), %H(시간, 24시간제), %M(분), %S(초)
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

# [KR] 포맷팅된 현재 일시를 출력합니다.
# [JP] フォーマットされた現在の日時を出力します。
print(f"現在の日時: {formatted_time}")
