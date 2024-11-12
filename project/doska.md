Таблицы:

1. Users
{

PK - id;
login: varchar;
role - FK;
password: varchar;

body:
...
}


2. Courses
{
    PK - id
    name - varchar;
    role - FK;
}

3. Roles
{
    id - FK
    role - varchar;
}

<!-- 3. Attendance
{
    PK - id;
     - enum

} -->