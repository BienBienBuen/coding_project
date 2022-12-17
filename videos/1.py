def add_brackets(str):
    str_list = list(str)
    new = ''
    for letter in str_list:
        new += '[' + letter + ']'
    return new

print(add_brackets('"title":{"accessibility":{"accessibilityData":{"label":"'))