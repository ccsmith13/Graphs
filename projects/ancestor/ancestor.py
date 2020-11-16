
def earliest_ancestor(ancestors, starting_node, current_searching_values = []):
    ''' find edges in ancestors where second value of tuple is equal to the starting node value
        then, take the first value of those node(s) and search ancestors to see where those are the second node value
        repeat until there are no values resulting from your search inside of ancestors 
        if there are two+ values left with no results, pick the lower value to return 
        else return the value the search breaks on
    '''

    '''NOTE: bug = all test run individually but will fail as values refuse to reset themselves when running subsequent tests'''
    
    if current_searching_values == []:
        current_searching_values.append(starting_node)
    

    for pair in ancestors:
        print('pair', pair)
        if pair[1] in current_searching_values:
            current_searching_values.remove(pair[1])
            current_searching_values.append(pair[0])
            print('current_searching_values', current_searching_values)
            earliest_ancestor(ancestors, current_searching_values)

    
    if current_searching_values[0] == starting_node:
        return -1 
    elif len(current_searching_values) > 1:
        return min(current_searching_values)
    else:
        return current_searching_values[0]
        

                