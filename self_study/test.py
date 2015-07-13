import re

# String에서 정규식으로 특정 string 제거하는 예제
# Python 2.7.6버전에서 동작 확인

def alphabet_translate():
	value = "a1b2c3d4e5f6g7h8i9"

	value = re.sub(r"\d", "", value)
	# r"\D"의 경우 숫자를 제외한 나머지 string들을 삭제한다.
	print(value)

alphabet_translate();