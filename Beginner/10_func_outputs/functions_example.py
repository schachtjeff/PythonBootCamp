def format_name(f_name, l_name) -> str:
    # formats something like 'jEfF' to 'Jeff'
    new_f_name = f_name.title()
    new_l_name = l_name.title()
    return new_f_name, new_l_name

un_f_name="eRnIe"
un_l_name="bAnKs"
f_f_name, f_l_name = format_name(f_name=un_f_name, l_name=un_l_name)
print(f"Original: {un_f_name} {un_l_name}")
print(f"Formated: {f_f_name} {f_l_name}")


def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)