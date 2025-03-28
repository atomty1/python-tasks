def compare_lists(first, second):
    result = []
    for val in first:
        for second_val in second:
            if(val == second_val and val not in result):
                result.append(val)
    
    return result
                

    

print(compare_lists([5, 10, 30, 20], [5, 10, 15, 20, 5]))