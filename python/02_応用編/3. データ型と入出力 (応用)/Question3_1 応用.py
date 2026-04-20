# [KR] input()으로 문자열 형태의 신발 사이즈를 입력받습니다.
# [JP] input()で文字列形式の靴のサイズを入力してもらいます。
size_input = input("靴のサイズを入力してください: ")

# [KR] 입력받은 문자열을 소수점 계산이 가능한 실수(float) 형태로 변환합니다.
# [JP] 入力された文字列を、小数点計算が可能な浮動小数点数(float)に変換します。
size_float = float(size_input)

# [KR] 변환된 값과 f-string을 사용하여 결과를 출력합니다.
# [JP] 変換された値とf-stringを使用して結果を出力します。
print(size_float)
print(f"サイズが{size_float}の靴を購入します")
