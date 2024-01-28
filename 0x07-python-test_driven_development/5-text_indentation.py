#!/usr/bin/python3

def text_indentation(text):
    final_str = ""
    idx = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    while idx < len(text):
        final_str += text[idx]
        if text[idx] == '.' or text[idx] == '?' or text[idx] == ':':
            final_str += '\n' * 2
            idx = idx + 1
        idx = idx + 1
    print(final_str, end="")
