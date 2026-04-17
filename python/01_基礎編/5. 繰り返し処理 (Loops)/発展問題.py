# [KR] 과일과 색상이 담긴 두 개의 리스트를 선언합니다.
# [JP] 果物と色が含まれた2つのリストを宣言します。
fruits = ["apple", "banana"]
colors = ["red", "yellow"]

# [KR] 바깥쪽 루프: 먼저 과일(fruits) 리스트에서 하나씩 꺼냅니다.
# [JP] 外側のループ: まず果物(fruits)リストから1つずつ取り出します。
for fruit in fruits:

    # [KR] 안쪽 루프: 선택된 과일에 대해 색상(colors) 리스트를 하나씩 꺼내어 조합합니다.
    # [JP] 内側のループ: 選択された果物に対して、色(colors)リストを1つずつ取り出して組み合わせます。
    for color in colors:
        # [KR] f-string을 사용하여 색상과 과일의 이름을 조합하여 출력합니다.
        # [JP] f-stringを使用して、色と果物の名前を組み合わせて出力します。
        print(f"{color} {fruit}")
