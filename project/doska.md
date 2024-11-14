/332324343434

Таблицы1234334:

1. Users
{
PK - id;
login: varchar;
password: varchar;
body:
...
}

Промежуточная таблица, чтобы реализовать отношения many-to-many между таблицами.  
2. UsersRoles 
{
ID - integer - PK
userID - integer - FK
roleID - integer - FK
}

3. Courses
{
    PK - id
    name - varchar;
}

Промежуточная таблица, чтобы реализовать отношения many-to-many между таблицами.  
4.CoursesRoles 
{
courseID - integer - FK
roleID - integer - FK
}

5.Roles
{
    id - PK
    role - varchar;
}

<!-- 3. Attendance
{
    PK - id;
     - enum

} -->
12345678