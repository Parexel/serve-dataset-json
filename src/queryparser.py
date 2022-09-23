
def parse(filter: str, varList: list):

    len_varList = len(varList)
    adaptetd_var_list = []
    for i in varList:
        adaptetd_var_list.append(i.lower())

    def resultParse(row: list):
        len_rowList = len(row)
        if len_rowList != len_varList:
            return 0
        else:
            n = len_rowList

        for i in range(n):
            exec(adaptetd_var_list[i] + " = row[i]")
        return eval(filter)

    return resultParse
