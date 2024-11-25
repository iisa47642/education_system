<script>
    import axios from "axios";
    import dayjs from "dayjs";
    export default {
        data() {
            return {
                user: {},
                userId: this.$route.params.id,
                cid: this.$route.params.cid,
                groups: [],
                group: "",
                students: [],
                dates: [],
            }
        },
        methods: {
            getDate(date) {
                return dayjs(date).format("DD-MM");
            },
            async changeAttendance(userId, attId, ids, date, typeId, attendance, created,user_id) {
                if (created) {
                    console.log("put запрос: ");
                    console.log(ids,user_id,date,typeId,attendance);
                    let response = await axios.put("/createattendance", {
                        subjectId: ids,
                        userId: user_id,
                        date: date,
                        type: typeId,
                        attendance: attendance,
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                        },
                    });
                    console.log(response);
                } else {
                    console.log("post запрос: ");
                    console.log(ids,user_id,date,typeId,attendance);
                    let response = await axios.post("/createattendance", {
                        subjectId: ids,
                        userId: user_id,
                        date: date,
                        type: typeId,
                        attendance: attendance,
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                        },
                    });
                    console.log(response);
                    this.students[userId].attendances[attId].created = true;
                }
            },
            async changeGroup(group) {
                let response = await axios.get("/students", {
                    params: {
                        name: group
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                console.log(response.data);
                this.makeStudents(response.data);
            },
            async makeStudents(s) {
                this.students = [];
                for (let i=0;i<s.length;i++) {
                    this.students.push({
                        name: s[i].username,
                        surname: s[i].surname,
                        id: s[i].id,
                        ids: this.cid,
                        attendances: []
                    });
                }
                console.log(this.students);
                for (let i=0;i<s.length;i++) {
                    let response = await axios.get("/attendancesub", {
                        params: {
                            id: s[i].id,
                            ids: this.cid
                        },
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                        },
                    });
                    let att = response.data;
                    for (let j=0; j < this.dates.length; j++) {
                        let flag = true;
                        for (let k = 0; k < att.length; k++) {
                            if (att[k].lessonId.id == this.dates[j].id) {
                                if (att[k].attendance) {
                                    this.students[i].attendances.push({
                                        date: att[k].lessonId.date,
                                        attendance: true,
                                        lessonType: this.dates[j].type.id,
                                        lesson: this.dates[j].type.name,
                                        created: true,
                                    });
                                } else {
                                    this.students[i].attendances.push({
                                        date: att[k].lessonId.date,
                                        attendance: false,
                                        lessonType: this.dates[j].type.id,
                                        lesson: this.dates[j].type.name,
                                        created: true,
                                    });
                                }
                            flag = false;
                            break;
                            }
                        }
                        if (flag) {
                            this.students[i].attendances.push({
                                date: this.dates[j].date,
                                attendance: false,
                                lessonType: this.dates[j].type.id,
                                lesson: this.dates[j].type.name,
                                created: false,
                            });
                        }
                    }
                }
            },
            async loadData() {
                let response = await axios.get("/profile", {
                    params: {
                        id: this.userId
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                this.user = response.data[0];
                this.groups = response.data[0].student_groups;
                this.group = this.groups[0];
                response = await axios.get("/datelessons", {
                    params: {
                        name: this.group,
                        ids: this.cid
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                this.dates = response.data;
                console.log(response.data);
                response = await axios.get("/students", {
                    params: {
                        name: this.group
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                console.log("s", response.data);
                this.makeStudents(response.data);
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
            <div class="attendance">
                <div class="attendance__title">
                    <div class="title__icon">
                        <img src="../assets/icons/clip.png" alt="">
                    </div>
                    <div class="title__text">посещаемость</div>
                </div>
                <div class="attendance__select">
                    <select @change="changeGroup(this.group)" v-model="this.group">
                        <option v-for="item,index in groups" :value="item">{{ item }}</option>
                    </select>
                </div>
                <div class="attendance__change">
                    <div class="attendance__row">
                        <div class="attendance__name"><p>ФИО\ДАТА</p></div>
                        <div v-for="item,index in dates" class="attendance__date">
                            <p>{{ getDate(item.date) }}</p>
                            <p>{{ item.type.name }}</p>
                        </div>
                    </div>
                    <div v-for="student,sindex in students" class="attendance__row">
                        <div class="attendance__name"><p>{{student.name}} {{ student.surname }}</p></div>
                        <div v-for="att,aindex in student.attendances" class="attendance__date attendance">
                            <select @change="changeAttendance(sindex,aindex,this.cid,att.date,att.lessonType,att.attendance,att.created,student.id)" v-model="att.attendance">
                                <option :value="true">+</option>
                                <option :value="false">н</option>
                            </select>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

</template>
<style scoped>
    .attendance {
        padding: 100px 0;
    }
    .attendance__change {
        background: rgba(0,0,0,20%);
        border: 2px solid rgba(0,0,0,50%);
        border-radius: 20px;
        overflow-x: scroll;
    }
    .attendance__change::-webkit-scrollbar {
        height: 16px;
        border-radius: 10px;
    }
    .attendance__change::-webkit-scrollbar-track {
        background: rgba(0,0,0,25%);
        border-radius: 10px;
    }
    .attendance__change::-webkit-scrollbar-thumb {
        background: rgba(0,0,0,50%);
        border-radius: 10px;
    }
    .attendance__row {
        display: flex;
        color: #fff;
        font-size: 20px;
        font-family: "Bona Nova", serif;
        padding: 0 20px;
        border-bottom: 2px solid rgba(0,0,0,50%);
    }
    .attendance__row:last-child {
        border-bottom: 0;
    }
    .attendance__date {
        padding: 10px;
        flex: 0 1 100px;
        overflow: hidden;
    }
    .attendance__date:not(:last-child) {
        border-right: 2px solid rgba(0,0,0,50%);
    }
    .attendance__name {
        padding: 10px;
        flex: 0 1 300px;
        text-align: center;
        border-right: 2px solid rgba(0,0,0,50%);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .attendance__date.attendance {
        padding: 0;
    }
    .attendance__date.attendance select {
        display: block;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,20%);
        text-align: center;
        color: #fff;
        font-size: 20px;
    }
    .attendance__date.attendance select:focus {
        outline: none;
    }
    .attendance__date.attendance option {
        background: transparent;
    }
    .attendance__select {
        text-align: right;
        margin-bottom: 10px;
    }
    .attendance__select select {
        background: rgba(0,0,0,20%);
        border: 2px solid rgba(0,0,0,50%);
        font-size: 20px;
        display: inline-block;
        padding: 10px 30px;
        border-radius: 10px;
        color: #fff;
    }
    .attendance__select select:focus {
        outline: none;
    }
    .attendance__title {
        display: flex;
        align-items: center;
    }
    .title__text {
        font-size: 55px;
        font-family: "Bona Nova", serif;
        font-weight: 700;
        color: #fff;
        text-transform: uppercase;
    }
</style>