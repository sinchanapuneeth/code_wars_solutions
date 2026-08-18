def delete_nth(order,max_e):
    final_list = []
    dict_final_list = {}
    
    for a in order:
        if a not in final_list:
            dict_final_list[a] = 0
        else:
            continue

    for a in order:
        if dict_final_list[a] < max_e:
            final_list.append(a)
            dict_final_list[a] += 1
            
    return(final_list)

#def delete_nth(order,max_e):
#    ans = []
#    for o in order:
#        if ans.count(o) < max_e: ans.append(o)
#    return ans

#differences between efficient code and mine:
#combined my two loops in one
#did not use many nested ifs
#BUT, my code runs in O(n), while the second one runs in O(n ^2)!
