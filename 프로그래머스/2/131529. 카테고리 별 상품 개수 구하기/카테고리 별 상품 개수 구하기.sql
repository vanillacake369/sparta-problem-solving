-- 코드를 입력하세요
# 상품 카테고리 코드(PRODUCT_CODE 앞 2자리) 별 상품 개수를 출력
SELECT 
    SUBSTRING(PRODUCT_CODE,1,2) as CATEGORY, # 0부터 시작 X. 1부터 시작
    COUNT(PRODUCT_ID) AS PRODUCTS
FROM 
    PRODUCT
GROUP BY 
    CATEGORY