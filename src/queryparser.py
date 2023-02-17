import re


def parse(query: str, var_names: list):
    query = re.sub(
        r'=(?=(?:[^\"\']*[\"\'][^\"\']*[\"\'])*[^\"\']*$)', '==', query)

    def predicate(row: list):
        for i, var in enumerate(var_names):
            exec(var + " = row[i]")
        return bool(eval(query))

    return predicate
