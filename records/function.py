
def get_sort_array(text):
    d = {}
    for i in range(len(text)):
             key = text[i]
             if key != ' ':
                quont = d.get(key, 0)+1
                d[key]=quont
    array=sorted(d.values(), reverse=True)
    return array