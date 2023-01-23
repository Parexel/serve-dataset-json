import re


def parse(query: str, var_list: list):

    query = re.sub(
        r'=(?=(?:[^\"\']*[\"\'][^\"\']*[\"\'])*[^\"\']*$)', '==', query)

    len_var_list = len(var_list)
    n = len_var_list
    adapted_var_list = []

    for i in var_list:
        adapted_var_list.append(i.lower())

    def result_parse(row: list):

        for i in range(n):
            exec(adapted_var_list[i] + " = row[i]")
        return bool(eval(query))

    return result_parse
