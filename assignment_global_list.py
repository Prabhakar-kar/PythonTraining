g_list = [10, 20, 30]
def g_list_mod():
    global g_list
    g_list.append(40)
    g_list+=[50, 60]

g_list_mod()
print("Modified list: ", g_list)