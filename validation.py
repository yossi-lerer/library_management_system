def validation_text(text):
    if text.strip():
        return True
    return False

def validation_positive_num(num):
    try:
        num = int(num)
        if num < 0:
            return False
        return True
    except:
        return False