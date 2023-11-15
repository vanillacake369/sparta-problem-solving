def switch(digStr):
    if(digStr == "zero"):
        return '0'
    elif(digStr == "one"):
        return '1'
    elif(digStr == "two"):
        return '2'
    elif(digStr == "three"):
        return '3'
    elif(digStr == "four"):
        return '4'
    elif(digStr == "five"):
        return '5'
    elif(digStr == "six"):
        return '6'
    elif(digStr == "seven"):
        return '7'
    elif(digStr == "eight"):
        return '8'
    elif(digStr == "nine"):
        return '9'
    return None


def solution(s):
    result = []
    digStr = ""
    
    for ch in s:
        # 문자가 숫자이면 :: result 리스트에 추가
        if(ch.isdigit()):
            result.append(str(ch))
            continue
        
        # 문자가 영문이면 :: digStr에 concat
        digStr += ch
        
        # digStr가 3을 넘었고, 숫자변환이 가능하다면 :: 숫자변환값 result 리스트에 추가
        if(len(digStr) >= 3):
            if(switch(digStr) != None):
                result.append(switch(digStr))
                digStr = ""
                
    # 문자로 이루어진 result를 문자열로 만든 뒤, int로 형변환
    return int("".join(result))