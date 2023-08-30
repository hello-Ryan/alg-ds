def naive_z_values(text):
    text_size = len(text)
    z_array=[]
    z_array.append(text_size)

    for i in range(1,text_size):
        z_value = 0
        j = 0
        while i < text_size and j<text_size and text[j] == text[i]:
            z_value += 1
            j += 1
            i += 1
        z_array.append(z_value)

    return z_array

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