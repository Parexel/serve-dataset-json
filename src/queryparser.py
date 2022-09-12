

def logicBinary(log1, log2, cond):
    return (cond == "and" and log1 and log2) or (cond == "or" and (log1 or log2))


def evaluateFilter(words_list: list, varList: list):

    n = len(words_list)
    # print(words_list)
    if n == 3:
        var1 = words_list[0]
        mark = words_list[1]
        var2 = words_list[2]

        number1 = -1
        number2 = -1
        tmp = 0
        for i in varList:
            # print(var1)
            # print(i)
            if var2 == i:
                number2 = tmp
            if var1 == i:
                number1 = tmp
            else:
                tmp += 1

        if number1 == -1:
            print("Error in case 1")
            return 0
        else:
            var1 = number1

        if number2 >= 0:
            var2 = number2
        elif var2[0] == "'":
            var2 = str(var2)
        else:
            var2 = float(var2)
        if mark == '=':
            def resultFunction(row: list):
                #print("Enter 1")

                if type(var2) == int and row[var1] == row[var2]:
                    return True
                elif type(var2) == str and row[var1] == var2:
                    return True
                elif type(var2) == float and row[var1] == var2:
                    return True
                else:
                    return False

        elif mark == '<=':
            def resultFunction(row: list):
                #print("Enter 2")

                if type(var2) == int and row[var1] <= row[var2]:
                    return True
                elif type(var2) == str and row[var1] <= var2:
                    return True
                elif type(var2) == float and row[var1] <= var2:
                    return True
                else:
                    return False
        elif mark == '>=':
            def resultFunction(row: list):
                #print("Enter 3")

                if type(var2) == int and row[var1] >= row[var2]:
                    return True
                elif type(var2) == str and row[var1] >= var2:
                    return True
                elif type(var2) == float and row[var1] >= var2:
                    return True
                else:
                    return False

        elif mark == '!=':
            def resultFunction(row: list):
                #print("Enter 4")

                if type(var2) == int and row[var1] != row[var2]:
                    return True
                elif type(var2) == str and row[var1] != var2:
                    return True
                elif type(var2) == float and row[var1] != var2:
                    return True
                else:
                    return False
        elif mark == '<':
            def resultFunction(row: list):
                #print("Enter 5")

                if type(var2) == int and row[var1] < row[var2]:
                    return True
                elif type(var2) == str and row[var1] < var2:
                    return True
                elif type(var2) == float and row[var1] < var2:
                    return True
                else:
                    return False

        elif mark == '>':
            def resultFunction(row: list):
                #print("Enter 6")

                if type(var2) == int and row[var1] > row[var2]:
                    return True
                elif type(var2) == str and row[var1] > var2:
                    return True
                elif type(var2) == float and row[var1] > var2:
                    return True
                else:
                    return False

        else:
            print("Error with eqv. mark")

    return resultFunction


def parse(filter: str, varList: list):

    words_list = list()
    operator_list = list()
    functions_list = list()

    temp_str = ""
    for i in filter:

        if i != " ":
            temp_str += i
        else:
            words_list.append(temp_str)
            temp_str = ""

        if len(words_list) == 3:
            variable = evaluateFilter(words_list, varList)
            functions_list.append(variable)
            variable = ""
            words_list = []
        if words_list != []:
            if words_list[0] == "and":
                words_list = []
                oper = "and"
                operator_list.append(oper)
                oper = ""
            elif words_list[0] == "or":
                words_list = []
                oper = "or"
                operator_list.append(oper)
                oper = ""

    def resultForMain(row: list):
        result_list = []
        for i in functions_list:
            tmp = i(row)
            result_list.append(tmp)   # [True, False, True, ...]
        n = len(operator_list) + 1

        check_and_list = []
        check_or_list = []
        for j in range(n-1):
            if operator_list[j] == "and":
                check_and_list.append(j)
            elif operator_list[j] == "or":
                check_or_list.append(j)

        result_list_new = []
        t = 0
        for k in check_and_list:
            binar = logicBinary(result_list[k-t], result_list[k+1-t], "and")
            result_list[k] = binar
            for h in range(n-t-1):
                if h > k:
                    result_list[h] = result_list[h+1]
            result_list[n-t-1] = 10
            # print(result_list)
            t += 1
        for y in result_list:
            if y != 10:
                result_list_new.append(y)
                # print(result_list_new)

        t = 0
        for k in check_or_list:
            binar = logicBinary(
                result_list_new[k-t], result_list_new[k+1-t], "or")
            result_list_new[k] = binar
            for h in range(n-t-1):
                if h > k:
                    result_list_new[h] = result_list_new[h+1]
            result_list[n-t-1] = 10
            t += 1
            # print(result_list_new)
        res = result_list_new[0]
        return res

    return resultForMain
