def Descending_Order(num):
    string = str(num)
    sorted_string = sorted(string)[::-1]
    joined_str = ''.join(sorted_string)
    desc_order = int(joined_str)
    return desc_order

# Descending_Order(21445)
# Descending_Order(145263)
# Descending_Order(1254859723)
