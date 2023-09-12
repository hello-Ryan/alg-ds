def naive_suffix_array(s):
    return sorted([x for x in range(len(s))], key = lambda x: s[x:])

def get_bwt(s):
    s += '$'
    suffix_arr = naive_suffix_array(s)


    return "".join([s[x - 1] for x in suffix_arr])
