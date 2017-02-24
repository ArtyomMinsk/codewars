def braces(values):
    yes_no_list = []
    temp_list = []
    close_list = ["}", ")", "]"]

    for string in values:
        if string[0] in close_list or len(string) == 0:
            yes_no_list.append("NO")
        else:
            for item in string:
                if item == "{" or item == "(" or item == "[":
                    temp_list.append(item)
                elif item == "}" and temp_list[-1] == "{":
                    temp_list.pop(-1)
                elif item == ")" and temp_list[-1] == "(":
                    temp_list.pop(-1)
                elif item == "]" and temp_list[-1] == "[":
                    temp_list.pop(-1)

            if len(temp_list) == 0:
                yes_no_list.append("YES")
            else:
                yes_no_list.append("NO")

    return yes_no_list

print(braces(["()[]{}", ")(", "{([])}", "({()[]})", "()[{()}]", "{[(]})", "[]{[(]})", "}{[(]})", "{[}]}", "}"]))
