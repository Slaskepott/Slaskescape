def get_modifier(bonus):
	modifier = 100 / (100 + bonus )
	return modifier
print(str(get_modifier(40)))
print(str(get_modifier(80)))
print(str(get_modifier(160)))
print(str(get_modifier(320)))
print(str(get_modifier(640)))
print(str(get_modifier(1260)))
print(str(get_modifier(2560)))
print(str(get_modifier(5120)))
print(str(get_modifier(10240)))
