def check_list(list):
    
    customized_list = []
    
    for element in list:
    
        if (element.isnumeric()) and (int(element) % 3 == 0):
            customized_list.append(element)
    
        elif (element.isalpha()) and ('a' in element.lower()):
            customized_list.append(element)

    return customized_list
    
print(check_list(["1", "3", "99", "Dad", "5", "9", "abba", "dudu"]))
