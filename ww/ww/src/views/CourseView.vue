<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                cid: this.$route.params.cid,
                user_id: this.$route.params.id,
                user: {},
                isStudent: true,
                subject: {},
                attendance: [
                    
                ],
                tasks: [],
                marks: [],
                lectures: [
                    {
                        name: "лекция_1.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "лекция_2.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "лекция_3.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "лекция_4.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "лекция_5.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "лекция_6.doc",
                        path: "лекция_1.doc"
                    }
                ],
                practices: [
                    {
                        name: "практика_1.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "практика_2.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "практика_3.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "практика_4.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "практика_5.doc",
                        path: "лекция_1.doc"
                    },
                    {
                        name: "практика_6.doc",
                        path: "лекция_1.doc"
                    }
                ],
                grades: [],
                students: [
                    
                ],
                gradesGroup: "",
            }
        },
        methods: {
            goAttendance() {
                this.$router.push({name: "attendance", params: {id: this.user_id,cid: this.cid}})
            },
            makeId(student, work,) {
                return String(student) + " " + String(work);
            },
            async makeAttendance() {
                let response = await axios.get("/attendancesub", {
                    params: {
                        id: this.user_id,
                        ids: this.cid
                    }
                });
                for (let i = 0; i < response.data.length; i++) {
                    let attendance = "н";
                    if (response.data[i].attendance) {
                        attendance = "+";
                    }
                    this.attendance.push({
                        date: response.data[i].lessonId.date,
                        attendance: attendance,
                    })
                }
                console.log("a", this.attendance);
            },
            async changeMark(studentId, workId, value) {
                let input = document.getElementById(String(studentId) + " " + String(workId));
                let mark = Number(input.value);
                value = Number(value);
                console.log(studentId,workId,mark);
                if (value == 0) {
                    let response = await axios.post("/createmark",{
                        controlWorkId: workId,
                        userId: studentId,
                        mark: mark,
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                        },
                    });
                    console.log(response);
                } else {
                    let response = await axios.put("/createmark", {
                        
                        controlWorkId: workId,
                        userId: studentId,
                        mark: mark,    
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                        },
                    });
                    console.log(response);
                }
            },
            async getStudents(group) {
                let response = await axios.get("/students", {
                    params: {
                        name: group
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                this.makeStudents(response.data);
            },
            async makeStudents(s) {
                this.students = [];
                for (let i = 0; i < s.length; i++) {
                    let response = await axios.get("/marks", {
                        params: {
                            id: s[i].id,
                            ids: this.cid
                        },
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                        },
                    });
                    let resMarks = response.data;
                    let marks = [];
                    if (resMarks.length > 0) {
                        console.log(s[i].username);
                        for (let j = 0; j < this.tasks.length; j++) {
                            let taskId = this.tasks[j].id;
                            console.log(taskId);
                            let flag = true;
                            for (let k = 0; k < resMarks.length; k++) {
                                if (resMarks[k].controlWorkId.id == taskId) {
                                    console.log("t1", taskId);
                                    flag = false;
                                    marks.push({
                                        id: taskId,
                                        mark: resMarks[k].mark
                                    });
                                    break
                                } else {
                                    flag = true;
                                }
                            }
                            if (flag) {
                                marks.push({
                                    id: taskId,
                                    mark: 0
                                });
                            }
                        }
                    } else {
                        for (let j = 0; j < this.tasks.length; j++) {
                            marks.push({
                                id: this.tasks[j].id,
                                mark: 0
                            });
                        }
                    }
                    console.log("m", marks);
                    this.students.push({
                        name: s[i].username,
                        surname: s[i].surname,
                        id: s[i].id,
                        marks: marks
                    });
                }
            },
            async loadData() {
                let response = await axios.get("/course", {
                    params: {
                        id: this.user_id,
                        ids: this.cid
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                this.subject = response.data[0];
                this.gradesGroup = response.data[0].groups[0];
                this.groups = response.data[0].groups;
                console.log(this.subject);
                response = await axios.get("/marks", {
                    params: {
                        id: this.user_id,
                        ids: this.cid,
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                console.log(response.data);
                this.marks = response.data;
                response = await axios.get("/profile", {
                    params: {
                        id: this.user_id
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                this.user = response.data;
                console.log("u",response.data);
                if (this.user[0].groups[0] == "student") {
                    this.isStudent = true;
                } else {
                    this.isStudent = false;
                }
                console.log(this.user);
                response = await axios.get("/controlevent", {
                    params: {
                        ids: this.cid
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                this.tasks = response.data;
                console.log("tasks: ", this.tasks);
                response = await axios.get("/students", {
                    params: {
                        name: this.gradesGroup
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                console.log("students: ",response.data);
                if (!this.isStudent) {
                    this.makeStudents(response.data);
                } else {
                    this.makeAttendance();
                }
            }
        },
        mounted() {
            this.loadData();
        }
    }
</script>
<template>
    <main>
        <div class="container">
            <div class="course">
                <div class="course__title title">
                    <h2>{{this.subject.name}}</h2>
                </div>
                <div class="course__row">
                    <div class="course__info">
                        <h3>кафедра:</h3>
                        <p>индустриальное программирование</p>
                        <h3>лектор:</h3>
                        <p>herss@gmail.com</p>
                        <p>8-999-999-99-99</p>
                        <h3>практик:</h3>
                        <p>spathochuu@gmail.com</p>
                        <p>8-961-999-99-99</p>
                    </div>
                    <div class="course__img">
                        <img src="../assets/imgs/image.png" alt="">
                    </div>
                </div>
                <div class="course__nav">
                    <div class="nav__item">
                        <ul>
                            <li v-if="isStudent"><a href="">посещаемость</a></li>
                            <li v-if="!isStudent"><a @click="goAttendance">посещаемость</a></li>
                            <li><a href="">оценки</a></li>
                            <li><a href="">посещение</a></li>
                        </ul>
                    </div>
                    <div class="nav__item">
                        <ul>
                            <li><a href="">тестирования</a></li>
                            <li><a href="">контрольные</a></li>
                            <li><a href="">материалы</a></li>
                        </ul>
                    </div>
                </div>
                <div v-if="isStudent" class="course__attendance">
                    <div class="attendance__title title">
                        <h2>посещаемость</h2>
                    </div>
                    <div class="attendance__row">
                        <div v-for ="item,index in attendance" class="attendance__item">
                            <div class="attendance__date">{{item.date}}</div>
                            <div class="attendance__att">{{ item.attendance }}</div>
                        </div>
                    </div>
                </div>
                <div v-if="!isStudent" class="course__teacherGrades">
                    <div class="attendance__title title">
                        <h2>Оценки</h2>
                    </div>
                    <div class="teacher__select">
                        <select @change="getStudents(this.gradesGroup)" v-model="gradesGroup">
                            <option v-for="item, index in groups" :value="item">{{ item }}</option>
                        </select>
                    </div>
                    
                    <div class="teacher__grades">
                        <div class="teacher__row">
                            <div class="teacher__item up">ФИО</div>
                            <div  v-for="item, index in tasks" class="teacher__item up grade">
                                <p :workId="item.id">{{ item.name }}</p>
                            </div>
                        </div>
                        <div v-for="student, ind in students" class="teacher__row">
                            <div class="teacher__item">{{student.name}} {{ student.surname }}</div>
                            <div v-for="mark, index in student.marks" class="teacher__item grade">
                                <input :id="makeId(student.id,mark.id)" type="number" :value="mark.mark" @change="changeMark(student.id, mark.id, mark.mark)">
                            </div>
                        </div>
                    </div>
                </div>
                <div v-if="isStudent" class="course__grades">
                    <div class="attendance__title title">
                        <h2>Оценки</h2>
                    </div>
                    <div class="grades">
                        <div v-for="item,index in marks" class="grade__row">
                            <div class="grade__title">{{ item.controlWorkId.name }}</div>
                            <div class="grade__divider"></div>
                            <div class="grade__grade">{{  item.mark}}/100</div>
                        </div>
                    </div>
                </div>
                <div v-if="isStudent" class="course__tasks">
                    <div class="attendance__title title">
                        <h2>Тестирования и Контрольные</h2>
                    </div>
                    <div class="tasks">
                        <div v-for="item, index in marks" class="task__row">
                        <div class="task__title">{{item.controlWorkId.name}}</div>
                        <div class="task__divider"></div>
                        <div class="task__button">
                            <a class="">очно</a>
                        </div>
                        </div>
                    </div>
                </div>
                <div class="course__materials">
                    <div class="attendance__title title">
                        <h2>материалы</h2>
                    </div>
                    <div class="materials">
                        <div class="materials__title">Лекции:</div>
                        <div class="materials__row">
                            <div v-for="item, index in lectures" class="materials__item">
                                <div class="mitem__img">
                                    <img src="../assets/icons/file.png" alt="">
                                </div>
                                <div class="mitem__title">
                                    <a href="">{{ item.name }}</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="materials">
                        <div class="materials__title">Практические работы:</div>
                        <div class="materials__row">
                            <div v-for="item, index in lectures" class="materials__item">
                                <div class="mitem__img">
                                    <img src="../assets/icons/file.png" alt="">
                                </div>
                                <div class="mitem__title">
                                    <a href="">{{ item.name }}</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>
<style scoped>
    .teacher__select {
        text-align: right;
        margin-bottom: 10px;
    }
    .teacher__select select {
        display: inline-block;
        background: rgba(0,0,0,25%);
        color: #fff;
        font-size: 24px;
        border: 2px solid rgba(0,0,0,50%);
        border-radius: 5px;
        padding: 10px 30px;
    }

    .teacher__select select:focus {
        outline: none;
    }
    .teacher__grades {
        background: rgba(0,0,0,25%);
        border: 2px solid rgba(0,0,0,50%);
        border-bottom: 0;
        border-radius: 10px;
        overflow-x: scroll;
        max-width: 100%;
        display: inline-block;
    }

    .teacher__grades::-webkit-scrollbar {
        height: 16px;
        border-radius: 10px;
    }

    .teacher__grades::-webkit-scrollbar-track {
        background: rgba(0,0,0,25%);
        border-radius: 10px;
    }

    .teacher__grades::-webkit-scrollbar-thumb {
        background: rgba(0,0,0,50%);
        border-radius: 10px;
    }
    .teacher__item.up {
        line-height: 46px;
    }

    .teacher__item {
        font-size: 20px;
        color: #fff;
        text-align: center;
        overflow: hidden;
        flex: 0 0 300px;
        border-bottom: 2px solid rgba(0,0,0,50%);
    }

    .teacher__item.grade input {
        display: block;
        background: transparent;
        text-align: center;
        width: 100%;
        height: 100%;
        color: #fff;
        font-size: 20px;
    }
    .teacher__item.grade input:focus {
        outline: 0;
    }
    .teacher__item:not(:last-child) {
        border-right: 2px solid rgba(0,0,0,50%);
    }
    .teacher__item.grade {
        flex: 0 0 200px;
        overflow: hidden;
    }
    .teacher__item.grade p {
        white-space: nowrap;
    }
    .teacher__row {
        display: flex;
    }
    main {
        background: rgb(115,130,138);
        background: linear-gradient(45deg, rgba(115,130,138,1) 0%, rgba(132,135,139,1) 50%, rgba(155,153,156,1) 100%);
    }
    .course {
        padding: 80px;
        border-left: 2px solid rgba(0,0,0,30%);
        border-right: 2px solid rgba(0,0,0,30%);
    }
    .title {
        font-family: "Bona Nova", serif;
        font-size: 55px;
        font-weight: 700;
        text-transform: uppercase;
        padding-left: 100px;
        color: #fff;
        position: relative;
        margin-bottom: 80px;
    }
    .course__title:before {
        content: '';
        width: 89px;
        height: 77px;
        background: url(../assets/icons/star.png) 50% 50% no-repeat;
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
    }
    .course__row {
        display: flex;
        margin-bottom: 60px;
    }
    .course__info {
        flex: 1 1 50%;
        padding-right: 20px;
        padding-top: 10px;
    }

    .course__info h3 {
        font-family: "Bona Nova SC", serif;
        font-size: 35px;
        text-transform: lowercase;
        font-weight: 700;
        color: #fff;
        padding-bottom: 10px;
    }

    .course__info p {
        font-family: "Bona Nova SC", serif;
        font-size: 35px;
        text-transform: lowercase;
        font-weight: 700;
        color: #cccecd;
        padding-bottom: 10px;
    }
    .course__img {
        flex: 0 1 50%;
        border-radius: 40px;
        overflow: hidden;
    }
    .course__img img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .course__nav {
        display: flex;
        background: rgba(0,0,0,30%);
        border: 2px solid rgba(0,0,0,50%);
        padding: 40px 30px;
        border-radius: 40px;
        margin-bottom: 80px;
    }

    .course__nav a {
        color: #fff;
        font-family: "Bona Novs SC", serif;
        font-size: 40px;
        font-weight: 700;
        padding-left: 20px;
        position: relative;
        transition-duration: 100ms;
        cursor: pointer;
    }

    .course__nav a:hover {
        color: rgba(0,0,0,50%);
    }

    .course__nav a:hover:before {
        background: rgba(0,0,0,50%);
    }
    .course__nav a:before {
        position: absolute;
        content: '';
        width: 8px;
        height: 8px;
        border-radius: 4px;
        background: #fff;
        left: 0;
        top: 50%;
        transition-duration: 100ms;
    }

    .nav__item {
        flex: 0 1 50%;
        text-align: center;
        padding: 0 10px;
    }

    .nav__item:first-child {
        border-right: 2px solid rgba(50,56,67,50%);
    }

    .nav__item ul {
        display: inline-block;
        text-align: left;
    }

    .attendance__title:before {
        content: '';
        width: 105px;
        height: 112px;
        background: url(../assets/icons/clip.png) 50% 50% no-repeat;
        position: absolute;
        left: 0;
        top: 0;
        transform: translateY(-20px);
    }

    .attendance__row {
        background: rgba(0,0,0,30%);
        border: 2px solid rgba(0,0,0,50%);
        border-radius: 40px;
        padding: 60px 0;
        display: flex;
        flex-wrap: wrap;
        margin-bottom: 80px;
    }
    .attendance__item {
        flex: 0 1 25%;
        color: #fff;
        display: flex;
        padding: 0 30px;
        justify-content: space-between;
        position: relative;
        font-family: "Bona Nova", serif;
        font-weight: 700;
        font-size: 23px;
    }
    .attendance__item:after {
        content: '';
        width: 2px;
        height: 100%;
        background: rgba(50,56,67,50%);
        position: absolute;
        top: 0;
        right: -2px;
    }
    .grades {
        padding: 40px 60px 0;
        background: rgba(0,0,0,30%);
        border: 2px solid rgba(0,0,0,50%);
        border-radius: 40px;
        color: #fff;
        margin-bottom: 80px;
    }

    .grade__row {
        display: flex;
        align-items: center;
        margin-bottom: 40px;
    }

    .grade__title {
        flex: 0 1 25%;
        padding-right: 10px;
        text-align: left;
        font-family: "Bona Nova",  serif;
        font-size: 27px;
        font-weight: 700;
        line-height: 1;
    }
    .grade__divider {
        height: 2px;
        background: #fff;
        flex: 1 1 auto;
    }

    .grade__grade {
        flex: 0 1 70px;
        padding-left: 20px;
        text-align: right;
        font-family: "Bona Nova", serif;
        font-size: 30px;
        font-weight: 700;
        line-height: 1;
    }

    .tasks {
        padding: 40px 60px 0;
        background: rgba(0,0,0,30%);
        border: 2px solid rgba(0,0,0,50%);
        border-radius: 40px;
        color: #fff;
        margin-bottom: 80px;
    }

    .task__row {
        display: flex;
        align-items: center;
        margin-bottom: 40px;
    }

    .task__title {
        flex: 0 1 25%;
        font-size: 27px;
        font-family: "Bona Nova SC", serif;
        font-weight: 700;
        padding-right: 20px;
    }

    .task__button {
        flex: 0 1 20%;
        padding-left: 20px;
        text-align: center;
    }
    .task__button a {
        display: inline-block;
        font-size: 23px;
        font-family: "Bona Nova SC", serif;
        font-weight: 700;
        line-height: 28px;
        border: 2px solid #fff;
        width: 100%;
        border-radius: 15px;
    }

    .task__button a.active {
        cursor: pointer;
        transition-duration: 100ms;
    }
    .task__button a.active:hover {
        background: #fff;
        color: #64676a;
    }
    .task__divider {
        height: 2px;
        background: #fff;
        flex: 1 1 auto;
    }
    .materials__title {
        font-size: 40px;
        font-family: "Bona Nova";
        font-weight: 700;
        color: #fff;
        padding-left: 20px;
        position: relative;
        margin-left: 60px;
        margin-bottom: 30px;
    }
    .materials__title:before {
        content: '';
        width: 8px;
        height: 8px;
        border-radius: 4px;
        background: #fff;
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-4px);
    }
    .materials {
        color: #fff;
        margin-bottom: 40px;
    }
    .materials__row {
        padding: 20px 60px 0;
        border: 2px solid rgba(0,0,0,50%);
        background: rgba(0,0,0,30%);
        border-radius: 40px;
        display: flex;
        flex-wrap: wrap;
    }
    .materials__item {
        flex: 0 1 33.333%;
        display: flex;
        align-items: center;
        padding: 0 20px;
        margin-bottom: 20px;
    }
    .mitem__title a{
        font-size: 20px;
        font-family: "Bona Nova SC", serif;
        font-weight: 700;
        padding-left: 10px;
        color: #fff;
    }
    .mitem__title:hover {
        text-decoration: underline;
    }

    .course__teacherGrades {
        margin-bottom: 80px;
    }
</style>