SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM SKILLCODES AS S
JOIN DEVELOPERS AS D
ON S.CATEGORY = 'Front End'
AND SUBSTR(REVERSE(BIN(D.SKILL_CODE)), LENGTH(BIN(S.CODE)), 1) = '1'
ORDER BY D.ID;