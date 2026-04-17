# [KR] 각각의 데이터 타입(정수, 실수, 불리언, 문자열)에 맞는 값을 변수에 대입합니다.
# [JP] それぞれのデータ型（整数、浮動小数点数、ブール、文字列）に合う値を変数に代入します。
int_data = 42
float_data = 3.14
bool_data = True
str_data = "Hello, Python!"

# [KR] f-string과 type() 함수를 사용하여 각 변수의 값과 데이터 타입을 출력합니다.
# [JP] f-stringとtype()関数を使用して、各変数の値とデータ型を出力します。
print(f"Value: {int_data}, Type: {type(int_data)}")
print(f"Value: {float_data}, Type: {type(float_data)}")
print(f"Value: {bool_data}, Type: {type(bool_data)}")
print(f"Value: {str_data}, Type: {type(str_data)}")
