def solution(s):
    words = s.split(" ")
    w = []

    for word in words:
        str = ''
        for idx,alp in enumerate(word):
            if(idx % 2 == 0):
                str += alp.upper()
            else :
                str += alp.lower()
        w.append(str)

    return " ".join(w)

