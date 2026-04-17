# [KR] random 모듈을 불러옵니다. (난수 생성 관련 함수들을 사용할 수 있습니다.)
# [JP] randomモジュールをインポートします。（乱数生成関連の関数を使用できます。）
import random

# [KR] random.randint(a, b)를 사용하여 1부터 100 사이(1과 100 포함)의 무작위 정수를 생성합니다.
# [JP] random.randint(a, b)を使用して、1から100まで（1と100を含む）のランダムな整数を生成します。
random_number = random.randint(1, 100)

# [KR] 생성된 무작위 정수를 출력합니다. (실행할 때마다 값이 바뀝니다.)
# [JP] 生成されたランダムな整数を出力します。（実行するたびに値が変わります。）
print(random_number)
