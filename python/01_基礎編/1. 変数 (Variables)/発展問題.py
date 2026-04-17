# [KR] 3개의 상품명(문자열)과 가격(정수)을 각각 변수에 저장합니다.
# [JP] 3つの商品名（文字列）と価格（整数）をそれぞれ変数に格納します。
item1_name = "リンゴ"
item1_price = 120

item2_name = "バナナ"
item2_price = 200

item3_name = "オレンジ"
item3_price = 150

# [KR] f-string과 삼중 따옴표(""")를 사용하여 여러 줄의 문자열을 하나의 변수에 포맷팅합니다.
# [JP] f-stringと三重引用符(""")を使用して、複数行の文字列を1つの変数にフォーマットします。
formatted_string = f"""商品リスト:
- {item1_name}: {item1_price}円
- {item2_name}: {item2_price}円
- {item3_name}: {item3_price}円"""

# [KR] 최종적으로 완성된 하나의 문자열을 출력합니다.
# [JP] 最終的に完成した1つの文字列を出力します。
print(formatted_string)
