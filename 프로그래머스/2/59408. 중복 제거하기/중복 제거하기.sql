-- 코드를 입력하세요
# https://dzzienki.tistory.com/39
SELECT COUNT(dis.NAME)
FROM (SELECT DISTINCT NAME
        FROM ANIMAL_INS) as dis
