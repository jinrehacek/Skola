--jeste exituje SUM, AVG, MAX, MIN, COUNT


-- Select all columns from the 'lockers' table and join it with the 'user' table based on the 'id' column
SELECT * FROM `lockers` INNER JOIN user ON user.id=lockers.user;

-- Select all columns from the 'lockers' table and join it with the 'user' table based on the 'id' column,
-- then join it with the 'class' table based on the 'class' column in the 'user' table
SELECT * FROM `lockers` INNER JOIN user ON user.id=lockers.user INNER JOIN class ON user.class=class.id;

-- Select the 'number' column from the 'lockers' table and join it with the 'user' table based on the 'id' column,
-- then join it with the 'class' table based on the 'class' column in the 'user' table
SELECT lockers.number FROM `lockers` INNER JOIN user ON user.id=lockers.user
INNER JOIN class ON user.class=class.id;

SELECT lockers.number, user.surname, class.name FROM `lockers` INNER JOIN user ON user.id=lockers.user
INNER JOIN class ON user.class=class.id

SELECT lockers.number, user.surname, class.name FROM `lockers` INNER JOIN user ON user.id=lockers.user
INNER JOIN class ON user.class=class.id ORDER BY lockers.number DESC

SELECT lockers.number, user.surname, class.name FROM `lockers` INNER JOIN user ON user.id=lockers.user
INNER JOIN class ON user.class=class.id WHERE class.name="7A8" ORDER BY lockers.number DESC

SELECT lockers.number, user.surname, class.name FROM `lockers` INNER JOIN user ON user.id=lockers.user
INNER JOIN class ON user.class=class.id WHERE class.name="7A8" AND user.gender="F" ORDER BY lockers.number DESC

SELECT class.name, COUNT(*) AS "pocet skrinek" FROM `lockers` INNER JOIN user ON user.id=lockers.user 
INNER JOIN class ON user.class=class.id GROUP BY class.id

SELECT class.name, COUNT(*) AS pocet_skrinek FROM `lockers` INNER JOIN user ON user.id=lockers.user 
INNER JOIN class ON user.class=class.id GROUP BY class.id ORDER BY pocet_skrinek DESC


-- ---------------------------------------
-- KURZY
-- ---------------------------------------

SELECT * FROM `kurzy_student` INNER JOIN user ON user.id=kurzy_student.user

SELECT * FROM `kurzy_student` INNER JOIN user ON user.id=kurzy_student.user INNER JOIN class ON class.id=user.class

SELECT * FROM `kurzy_student` INNER JOIN user ON user.id=kurzy_student.user INNER JOIN class ON class.id=user.class INNER JOIN kurzy ON kurzy_student.kurz=kurzy.id

SELECT user.firstname, user.surname FROM `kurzy_student` INNER JOIN user ON user.id=kurzy_student.user 
INNER JOIN class ON class.id=user.class INNER JOIN kurzy ON kurzy_student.kurz=kurzy.id WHERE class.name IN ("7A8", "7B8", "3A4")

SELECT user.firstname, user.surname FROM `kurzy_student` INNER JOIN user ON user.id=kurzy_student.user 
INNER JOIN class ON class.id=user.class INNER JOIN kurzy ON kurzy_student.kurz=kurzy.id WHERE class.name IN ("7A8", "7B8", "3A4") AND kurzy.title LIKE "Rakousko%"

SELECT user.firstname, user.surname FROM `kurzy_student` INNER JOIN user ON user.id=kurzy_student.user INNER JOIN class ON class.id=user.class 
INNER JOIN kurzy ON kurzy_student.kurz=kurzy.id WHERE class.name IN ("7A8", "7B8", "3A4") AND kurzy.title LIKE "Rakousko%" AND kurzy.type="1"

SELECT kurzy.title, count(*) as "pocet zaku" FROM `kurzy_student` INNER JOIN user ON user.id=kurzy_student.user INNER JOIN class ON class.id=user.class 
INNER JOIN kurzy ON kurzy_student.kurz=kurzy.id WHERE class.name IN ("7A8", "7B8", "3A4") AND kurzy.type="1" GROUP BY kurzy.title

SELECT kurzy.title, count(*) as "pocet zaku" FROM `kurzy_student` INNER JOIN user ON user.id=kurzy_student.user INNER JOIN class ON class.id=user.class 
INNER JOIN kurzy ON kurzy_student.kurz=kurzy.id WHERE class.name IN ("7A8", "7B8", "3A4") AND kurzy.type="1" GROUP BY kurzy.id

