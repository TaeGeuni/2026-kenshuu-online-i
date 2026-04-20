# [KR] 3개의 상품 가격을 순서대로 입력받아 정수로 변환합니다.
# [JP] 3つの商品の値段を順番に入力してもらい、整数に変換します。
price1 = int(input("1つ目の値段: "))
price2 = int(input("2つ目の値段: "))
price3 = int(input("3つ目の値段: "))

# [KR] 입력받은 3개의 가격을 각각 출력합니다.
# [JP] 入力された3つの値段をそれぞれ出力します。
print(price1)
print(price2)
print(price3)

# [KR] 각 가격에 0.7을 곱해 할인가를 구한 뒤, 모두 더하고 int()로 소수점을 버립니다.
# [JP] 各値段に0.7を掛けて割引価格を求め、すべて足してからint()で小数点以下を切り捨てます。
total_discounted = int((price1 * 0.7) + (price2 * 0.7) + (price3 * 0.7))

# [KR] 총합을 3으로 나누어 평균을 구합니다. 버림 나눗셈(//)을 사용하면 자동으로 소수점이 버려집니다.
# [JP] 合計を3で割り平均を求めます。切り捨て除算(//)を使うと自動的に小数点以下が切り捨てられます。
average_discounted = total_discounted // 3

# [KR] 총합과 평균을 출력합니다.
# [JP] 合計と平均を出力します。
print(f"合計{total_discounted}円")
print(f"平均{average_discounted}円")
