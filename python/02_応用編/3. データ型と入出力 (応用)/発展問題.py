# [KR] 사용자로부터 취미를 쉼표(,)로 구분하여 한 번에 입력받습니다.
# [JP] ユーザーから趣味をカンマ(,)区切りで一度に入力してもらいます。
hobbies_str = input("趣味をカンマ区切りで入力してください: ")

# [KR] split() 메서드를 사용하여 쉼표(',')를 기준으로 문자열을 쪼개어 리스트로 만듭니다.
# [JP] split() メソッドを使用して、カンマ(',')を基準に文字列を分割し、リストにします。
hobbies_list = hobbies_str.split(",")

print("あなたの趣味:")

# [KR] enumerate(리스트, 시작번호)를 쓰면 인덱스(번호)와 값을 동시에 깔끔하게 꺼낼 수 있습니다!
# [JP] enumerate(リスト, 開始番号) を使うと、インデックス（番号）と値を同時にすっきり取り出せます！
for index, hobby in enumerate(hobbies_list, 1):

    # 💡Point: 사용자가 "読書, 映画鑑賞" 처럼 공백을 넣었을 경우를 대비해 strip()으로 양옆 공백을 없애줍니다.
    # 💡Point: ユーザーが "読書, 映画鑑賞" のように空白を入れた場合に備え、strip()で両端の空白を消します。
    clean_hobby = hobby.strip()

    # [KR] 번호와 취미를 출력합니다.
    # [JP] 番号と趣味を出力します。
    print(f"{index}: {clean_hobby}")
