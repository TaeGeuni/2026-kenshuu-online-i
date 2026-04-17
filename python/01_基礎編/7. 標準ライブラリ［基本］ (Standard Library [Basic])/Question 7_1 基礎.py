# [KR] math 모듈을 불러옵니다. (수학 관련 함수들을 사용할 수 있게 됩니다.)
# [JP] mathモジュールをインポートします。（数学関連の関数を使用できるようになります。）
import math

# [KR] 입력값 16을 변수에 대입합니다.
# [JP] 入力値16を変数に代入します。
num = 16

# [KR] math.sqrt() 함수를 사용하여 변수 num의 제곱근을 계산합니다.
# [JP] math.sqrt()関数を使用して、変数numの平方根を計算します。
# 💡Point: sqrt는 Square Root(제곱근)의 약자입니다.
sqrt_result = math.sqrt(num)

# [KR] f-string을 사용하여 계산 결과를 요구사항에 맞게 출력합니다.
# [JP] f-stringを使用して、計算結果を要件に合わせて出力します。
print(f"{num}の平方根は{sqrt_result}です。")
