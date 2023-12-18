-- 코드를 입력하세요
# https://stackoverflow.com/questions/367863/find-records-from-one-table-which-dont-exist-in-another
SELECT 
    ins.NAME,
    ins.DATETIME
FROM 
    ANIMAL_INS ins
LEFT JOIN 
    ANIMAL_OUTS outs
ON
    ins.ANIMAL_ID = outs.ANIMAL_ID
WHERE 
    outs.ANIMAL_ID IS NULL
ORDER BY 
    ins.DATETIME ASC
LIMIT
    3