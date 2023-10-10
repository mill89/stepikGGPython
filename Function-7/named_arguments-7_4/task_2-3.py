# 1
def get_rect_value(a: int, b: int, type=0) -> int:
    return 2 * (a + b) if type == 0 else a * b


# 2
def check_password(password: str, chars='$%!?@#') -> bool:
    return True if len(password) >= 8 and set(password) & set(chars) else False

