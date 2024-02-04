SELECT HISTORY_ID, FLOOR(DAILY_FEE * (DATEDIFF(H.END_DATE, H.START_DATE) + 1) * IFNULL(1 - (DISCOUNT_RATE/100), 1)) AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
JOIN CAR_RENTAL_COMPANY_CAR AS C
ON H.CAR_ID = C.CAR_ID AND C.CAR_TYPE = '트럭'
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
ON C.CAR_TYPE = P.CAR_TYPE AND
((DATEDIFF(H.END_DATE, H.START_DATE) BETWEEN 7 AND 29 AND P.DURATION_TYPE = '7일 이상') OR
(DATEDIFF(H.END_DATE, H.START_DATE) BETWEEN 30 AND 89 AND P.DURATION_TYPE = '30일 이상') OR
(DATEDIFF(H.END_DATE, H.START_DATE) >= 90 AND P.DURATION_TYPE = '90일 이상'))
ORDER BY FEE DESC, HISTORY_ID DESC;