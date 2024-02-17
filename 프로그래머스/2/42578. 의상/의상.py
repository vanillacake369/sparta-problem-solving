def solution(clothes):
    outfits = {}
    for item, category in clothes:
        outfits[category] = outfits.get(category, 0) + 1
    
    total_combinations = 1
    for category in outfits:
        total_combinations *= (outfits[category] + 1)  # 각 카테고리별 의상 수에 입지 않는 경우를 추가한 후 곱합니다.
    
    return total_combinations - 1  # 모든 의상을 입지 않는 경우를 제외합니다.
