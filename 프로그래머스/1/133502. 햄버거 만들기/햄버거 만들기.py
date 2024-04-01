def solution(ingredient):
    burger = "1231"
    # map 으로 str 을 만들고, "1231" 을 regex 로 찾기
    ingredientStr = ''.join(map(str, ingredient))
    burgerCount = ingredientStr.find(burger)
    if burgerCount < 0:
        return 0
    else:
        return burgerCount