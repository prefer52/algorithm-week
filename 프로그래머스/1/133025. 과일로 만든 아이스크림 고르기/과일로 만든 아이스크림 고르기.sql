SELECT FH.FLAVOR
FROM FIRST_HALF AS FH
JOIN ICECREAM_INFO AS II
ON FH.FLAVOR = II.FLAVOR
WHERE TOTAL_ORDER >= 3000 AND INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC;