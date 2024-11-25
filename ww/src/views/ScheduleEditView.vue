<script>
    import dayjs from "dayjs";
    import axios from "axios";
    import "dayjs/locale/ru";
    dayjs.locale("ru");

    export default {
        data() {
            return {
                weekday: dayjs().day(),
                date: dayjs().format("DD.MM.YYYY"),
                userId: this.$route.params.id,
                weekNumber: 1,
                isStudent: false,
                s: [],
                electives: [],
                schedule: [
                    {
                        name: "Monday",
                        day: 1,
                        subjects: [],
                        today: false,
                    },
                    {
                        name: "Tuesday",
                        day: 2,
                        subjects: [],
                        today: false,
                    },
                    {
                        name: "Wednesday",
                        day: 3,
                        subjects: [],
                        today: false,
                    },
                    {
                        name: "Thurday",
                        day: 4,
                        subjects: [],
                        today: false,
                    },
                    {
                        name: "Friday",
                        day: 5,
                        subjects: [],
                        today: false,
                    },
                    {
                        name: "Saturday",
                        day: 6,
                        subjects: [],
                        today: false,
                    },
                ],
            }
        },
        methods: {
            goSchedule() {
                this.$router.push({name: "schedule", params: {id: this.userId}});
            },
            async changeElective(value,id,name) {
                console.log(value, id, name);
                if (value) {
                    let response = await axios.post("/createelective", {
                        name: name,
                        userId: id,
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                        },
                    });
                    console.log(response);
                } else {
                    let response = await axios.delete('/createelective', {
                        data: {
                            userId: id,
                            name: name  
                        },
                        headers: {
                            'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                        },
                    });
                    console.log(response);
                }
            },
            getDate(date) {
                console.log(date);
            },
            createElectives(allelective,selective) {
                for (let i = 0; i < allelective.length; i++) {
                    let id = allelective[i].id;
                    let flag = true;
                    for (let j = 0; j < selective.length; j++) {
                        if (selective[j].id == id) {
                            this.electives.push({
                                name: allelective[i].name,
                                selected: true,
                                group: allelective[i].groups[0]
                            });
                            flag = false;
                            break;
                        }
                    }
                    if (flag) {
                        this.electives.push({
                            name: allelective[i].name,
                            selected: false,
                            group: allelective[i].groups[0]
                        });
                    }
                }
            },
            createShedule(s) {
                for (let i = 0; i < this.schedule.length; i++) {
                    if (this.schedule[i].day == this.weekday) {
                        this.schedule[i].today = true;
                        break;
                    }
                }
                for (let i = 0; i < s.length; i++) {
                    if (s[i].lessonId.week_number == this.weekNumber) {
                        this.schedule[s[i].lessonId.week_day_number-1].subjects.push(
                            {
                                name: s[i].lessonId.subjectId.name,
                                startTime: dayjs(s[i].lessonId.startTime).format("HH:mm"),
                                endTime: dayjs(s[i].lessonId.endTime).format("HH:mm"),
                                location: s[i].lessonId.location.name,
                                order: s[i].lessonId.lesson_number,
                                attendance: s[i].attendance,
                                isElective: s[i].lessonId.subjectId.is_elective,
                            }
                        )
                    } else {
                        console.log(this.weekNumber);
                        console.log(s[i].lessonId.week_number);
                    }
                }
                for (let i = 0; i < 6; i++) {
                    this.schedule[i].subjects.sort(function(a, b) {
                    return parseFloat(a.order) - parseFloat(b.order);
                    });
                }
            },
            async loadData(id) {
                let response = await axios.get("/attendance", {
                    params: {
                        id: id,
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                this.createShedule(response.data);
                console.log("r", response.data);
                if (response.data[0].userId.groups[0] == "student") {
                    this.isStudent = true;
                } else {
                    this.isStudent = false;
                }
                response = await axios.get(`/studentelective/${id}`, {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                console.log(response.data);
                this.createElectives(response.data.all_group,response.data.student_group);
            }
        },
        mounted() {
            this.getDate(this.date);
            this.loadData(this.userId);
            
        }
    }
</script>
<template>
    <main>
        <div class="container">
            <div class="shedule">
                <div class="shedule__title">
                    <h2>мое расписание</h2>
                </div>
                <div class="shedule__subtitle">
                    <h3>идёт {{this.weekNumber}} учебная неделя (нечёт.) {{this.date}}</h3>
                </div>
                <div class="shedule__col">
                    <div class="schedule__electives">
                        <div v-for="item,index in electives" class="schedule__elective">
                            <div class="elective__name">{{ item.name }}</div>
                            <div class="elective__input">
                                <input :id="item.name" @change="changeElective(item.selected, this.userId, item.group)" type="checkbox" v-model="item.selected">
                                <label :for="item.name"></label>  
                            </div>
                        </div>
                    </div>
                    <div class="go_back">
                        <a @click="goSchedule">Вернуться в расписание</a>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>
<style scoped>
    .go_back {
        text-align: center;
    }
    .go_back a {
        font-size: 24px;
        color: rgba(255,255,255,70%);
        line-height: 2;
        cursor: pointer;
        text-transform: uppercase;
        font-family: "Bona Nova", serif;
        font-weight: 700;
    }
    .go_back a:hover {
        text-decoration: underline;
    }
    .schedule__elective {
        display: flex;
        max-width: 80%;
        background: rgba(0,0,0,20%);
        border: 2px solid rgba(0,0,0,50%);
        color: #fff;
        padding: 20px;
        border-radius: 20px;
        margin: 0 auto 20px;
        font-size: 30px;
        justify-content: space-between;
    }
    .elective__input label {
        width: 40px;
        height: 40px;
        border-radius: 20px;
        border: 2px solid rgba(0,0,0,50%);
        display: block;
    }
    .elective__input input:checked + label {
        background: #fff;
    }
    .schedule__elective input {
        display: none;
    }
    main {
        background: rgb(115,130,138);
        background: linear-gradient(45deg, rgba(115,130,138,1) 0%, rgba(132,135,139,1) 50%, rgba(155,153,156,1) 100%);
    }
    .shedule {
        padding: 40px;
        border-left: 2px solid rgba(0,0,0,30%);
        border-right: 2px solid rgba(0,0,0,30%);
    }

    .shedule__title {
        margin-bottom: 40px;
    }

    .shedule__title h2 {
        color: #fff;
        font-size: 55px;
        font-family: "Bona Nova", serif;
        font-weight: 700;
        text-transform: uppercase;
        padding-left: 100px;
        position: relative;
    }
    .shedule__title h2:before {
        content: '';
        position: absolute;
        width: 92px;
        height: 98px;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        background: url(../assets/icons/hat.png) 50% 50% no-repeat;
    }

    .shedule__subtitle {
        font-family: "Bona Nova SC", serif;
        font-size: 30px;
        font-weight: 700;
        color: #fff;
        margin-bottom: 40px;
    }

    .day {
        margin-bottom: 30px;
    }

    .day h3 {
        font-family: "Elsie Swash Caps", serif;
        font-weight: 900;
        color: #fff;
        font-size: 30px;
        text-transform: uppercase;
        text-align: center;
        margin-bottom: 20px;
    }

    .day h3.today {
        color: #323843;
    }

    .day__row {
        display: block;
        padding: 20px;
        background: rgba(50,56,67,20%);
        border: 2px solid rgba(50,56,67,50%);
        border-radius: 50px;
        color: #fff;
        font-family: "Bona Nova SC", serif;
        font-size: 20px;
        font-weight: 700;
        align-items: flex-start;
    }

    .subject {
        display: flex;
        padding: 0 20px;
        align-items: center;
        justify-content: space-between;
    }

    .subject {
        margin-bottom: 10px;
    }

    .subject__title {
        font-weight: 700;
        line-height: 1;
        flex: 0 1 40%;
        overflow: hidden;
    }

    .subject__visited {
        width: 16px;
        height: 16px;
        border: 1px solid #fff;
        border-radius: 8px;
    }

    .subject__visited.visited {
        background: #fff;
    }

    .day__left {
        flex: 1 1 50%;
        border-right: 2px solid rgba(0,0,0,20%);
        padding-top: 10px;
    }
    .day__right {
        flex: 0 1 50%;
        padding-top: 10px;
    }

    .schedule__edit{
        text-align: center;
        cursor: pointer;
        color: rgba(255,255,255,70%);
        font-family: "Bona Nova SC", serif;
        font-weight: 700;
        font-size: 30px;
    }

    .schedule__edit a:hover {
        text-decoration: underline;
    }
</style>