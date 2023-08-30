def reverse_string(text):
    string = ""
    for i in range(len(text)-1, -1, -1):
        string += text[i]

    return string

def z_values(text):
    text_size = len(text)
    z_array = [0] * text_size
    z_array[0] = text_size
    l,r = 0,0
    k = 0

    for i in range(1,text_size):

        # * case 1 naive pattern matching
        if i > r:
            l,r = i, i

            while r < text_size and text[r-l] == text[r]:
                r += 1
            z_array[i] = r - l
            r -= 1

        # * case 2
        else:
            k = i - l
            
            # * case 2A (z box less than right boundary)
            if z_array[k] < r - i + 1:
                z_array[i] = z_array[k]
            
            # * case 2B (at the right boundary or over)
            else:
                l = i
                while r < text_size and text[r-l] == text[r]:
                    r += 1
                z_array[i] = r - l
                r -= 1

    return z_array

def z_alg(pattern,text):
    new_string = pattern +'$'+ text

    pattern_size = len(pattern)

    # O(m + n) where m and n are the length of the pattern and text respectively
    z_vals = z_values(new_string)

    matches = []

    # O(n) where n is the length of the text
    for i in range(pattern_size, len(new_string)):

        if z_vals[i] == pattern_size:
            matches.append([i-pattern_size-1, i-2])

    return matches

def preprocessing(pattern):
    pattern_length = len(pattern)

    # * initialising preprocessing table contents
    ZiSuffixValues = z_values(reverse_string(pattern))
    ZiSuffixValues.reverse()
    goodSuffixValues = [0] * (pattern_length + 1)

    ALPHABET_SIZE = 26
    badCharacter = []
    badCharacter.append([-1]*ALPHABET_SIZE)
    for i in range(len(pattern) - 1):
        lst = [-1] * ALPHABET_SIZE
        lst[ord(pattern[i]) - 97] = i
        badCharacter.append(lst)

    for i in range(ALPHABET_SIZE):
        for j in range(len(pattern)-1):
            badCharacter[j+1][i] = max(badCharacter[j+1][i] ,badCharacter[j][i])
        
    # * good suffix values
    for p in range(pattern_length - 1):
        j = pattern_length - ZiSuffixValues[p]
        goodSuffixValues[j] = p

    # * matched prefix values
    matchedPrefixValues = z_values(pattern)
    for i in range(len(matchedPrefixValues) - 1, 0, -1):
        matchedPrefixValues[i-1] = max(matchedPrefixValues[i],matchedPrefixValues[i-1])
    matchedPrefixValues.append(0)
    
    return badCharacter, goodSuffixValues, matchedPrefixValues

def boyer_moore(txt, pat):
    r, gs, mp = preprocessing(pat)
    n = len(txt)
    m = len(pat)
    j = 0
    res = []

    while j < n - m + 1:
        k = m - 1
        # * loop from right to left
        while k >= 0:
            if pat[k] == txt[k + j]:
                k-=1
            else:
                if r[k][ord(txt[k+j])-97] == -1:
                    bc_shift = k
                else:
                    bc_shift = k - r[k][ord(txt[k+j])-97]

                gs_shift = m - gs[k + 1]

                if gs[k+1] == 0:
                    mp_shift = m - mp[k+1]
                    j += mp_shift - 1
                    break
                else:
                    j += (max(bc_shift, gs_shift) - 1)
                    break
        if k < 0:
            res.append(j + 1)
            j += m - mp[1]

