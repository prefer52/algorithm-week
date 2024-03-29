SELECT YEAR(OS.SALES_DATE) AS YEAR, MONTH(OS.SALES_DATE) AS MONTH,
COUNT(DISTINCT UI.USER_ID) AS PUCHASED_USERS,
ROUND(COUNT(DISTINCT UI.USER_ID)/(
    SELECT COUNT(USER_ID)
    FROM USER_INFO
    WHERE YEAR(JOINED) = '2021'), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE AS OS
JOIN USER_INFO AS UI
ON OS.USER_ID = UI.USER_ID AND YEAR(UI.JOINED) = '2021'
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;