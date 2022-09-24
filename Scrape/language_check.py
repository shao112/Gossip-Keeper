def check_chinese(text):
    for alp in text:
        if not '\u4e00' <= alp <= '\u9fa5':
            continue
        return True
    return False