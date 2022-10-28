
def parse(filter: str, varList: list):

    len_varList = len(varList)
    n = len_varList
    adaptetd_var_list = []
    for i in varList:
        adaptetd_var_list.append(i.lower())

    def resultParse(row: list):

        for i in range(n):
            exec(adaptetd_var_list[i] + " = row[i]")
        return bool(eval(filter))

    return resultParse
