use db;

-- CREATE TABLE students(
--     StudentID int not null,
--     FirstName varchar(100) not null,
--     Surname varchar(100) not null,
--     PRIMARY KEY (StudentID)
-- );

-- INSERT INTO students(StudentID,FirstName,Surname)
-- VALUES (1,"John","Andersen"), (2,"Emma","Smith");


CREATE TABLE tasks(
    taskNum int not null,
    task varchar(100) not null,
    PRIMARY KEY (taskNum)
);
