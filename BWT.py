def naive_suffix_array(s):
    return sorted([x for x in range(len(s))], key = lambda x: s[x:])

def get_bwt(s):
    s += '$'
    suffix_arr = naive_suffix_array(s)
    return "".join([s[x - 1] for x in suffix_arr])

def bwt_to_original(bwt):
    count = [0] * 88

    for letter in bwt:
        count[ord(letter) - 36] += 1

    rank = [0] * 88

    prev_count = 0
    prev_rank = 0
    for i, num in enumerate(count):
        if num == 0:
            continue
        else:
            rank[i] = prev_rank + prev_count

            prev_count = num
            prev_rank = rank[i]

    res = bwt[0]+'$'

    pos = rank[ord(bwt[0]) - 36]

    while True:
        pos = rank[ord(bwt[pos]) - 36] + sum(1 for x in bwt[:pos] if x == bwt[pos])

        print(pos)

        if bwt[pos] == '$':
            break
        
        else:
            res = bwt[pos] + res
        
    return res

def bwt_pattern_match(txt, pat):
    bwt = get_bwt(txt)







print(bwt_to_original(get_bwt('googol')))