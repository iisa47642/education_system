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
                attendance: [],
                s: [],
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
            selectDay(dayId, linkId) {
                let days = document.querySelectorAll(".day");
                let day = document.getElementById(dayId);
                let link = document.getElementById(linkId);
                let links = document.querySelectorAll(".schedule__row a");
                console.log(days);
                console.log(day);
                console.log(links);
                console.log(link);
                for (let i = 0; i < 6; i++) {
                    days[i].classList.remove("visible");
                    links[i].classList.remove("active");
                }
                link.classList.add("active");
                day.classList.add("visible");
            },
            goEditSchedule() {
                this.$router.push({name: "scheduleEdit", params: {
                    id: this.userId
                }});
            },
            getDate(date) {
                console.log(date);
            },
            createShedule(s,a) {
                console.log("s",s);
                console.log("a",a);
                for (let i = 0; i < this.schedule.length; i++) {
                    if (this.schedule[i].day == this.weekday) {
                        this.schedule[i].today = true;
                        break;
                    }
                }
                for (let i = 0; i < s.length; i++) {
                    if (s[i].week_number == this.weekNumber) {
                        let flag = true;
                        for (let j = 0; j < a.length; j++) {
                            if (s[i].id == a[j].id) {
                                this.schedule[s[i].week_day_number-1].subjects.push(
                                    {
                                        name: s[i].subjectId.name,
                                        startTime: dayjs(s[i].startTime).format("HH:mm"),
                                        endTime: dayjs(s[i].endTime).format("HH:mm"),
                                        location: s[i].location.name,
                                        order: s[i].lesson_number,
                                        attendance: a[j].attendance,
                                        isElective: s[i].subjectId.is_elective,
                                        isAttendance: true
                                    }
                                );
                                flag = false;
                                break;
                            }
                        }
                        if (flag) {
                            this.schedule[s[i].week_day_number-1].subjects.push(
                                    {
                                        name: s[i].subjectId.name,
                                        startTime: dayjs(s[i].startTime).format("HH:mm"),
                                        endTime: dayjs(s[i].endTime).format("HH:mm"),
                                        location: s[i].location.name,
                                        order: s[i].lesson_number,
                                        attendance: false,
                                        isElective: s[i].subjectId.is_elective,
                                        isAttendance: false
                                    }
                                );
                        }
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
                let attendance = response.data;
                response = await axios.get("/schedule", {
                    params: {
                        id: id,
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                let s = response.data;
                this.createShedule(s,attendance);
                response = await axios.get("/profile", {
                    params: {
                        id: id,
                    },
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                console.log(response.data);
                if (response.data[0].groups[0] == "student") {
                    this.isStudent = true;
                } else {
                    this.isStudent = false;
                }
                
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
                <ul class="schedule__row">
                    <li><a id="MondayA" @click="selectDay('Monday', 'MondayA')" class="active">mon</a></li>
                    <li><a id="TuesdayA" @click="selectDay('Tuesday', 'TuesdayA')">tue</a></li>
                    <li><a id="WednesdayA" @click="selectDay('Wednesday', 'WednesdayA')">wed</a></li>
                    <li><a id="ThursdayA" @click="selectDay('Thurday', 'ThursdayA')">thu</a></li>
                    <li><a id="FridayA" @click="selectDay('Friday', 'FridayA')">fri</a></li>
                    <li><a id="SaturdayA" @click="selectDay('Saturday', 'SaturdayA')">sat</a></li>
                </ul>
                <div class="shedule__col">
                    <div v-for="item, index in schedule">
                        <div :id="item.name" :class="{day: true, visible: item.today }">
                            <h3 :class="{today: item.today}">{{item.name}}</h3>
                            <div class="day__block">
                                <div class="day__row">
                                    <div class="day__left">
                                        <div v-for="subject, ind in item.subjects" class="left__item">
                                            <div v-if="!subject.isElective" class="subject non-elective">
                                                <h4 class="subject__title">
                                                    {{ subject.name }}
                                                </h4>
                                                <div class="subject__time">
                                                    {{ subject.startTime }}-{{ subject.endTime }}
                                                </div>
                                                <div class="subject__class">
                                                    {{subject.location}}
                                                </div>
                                                <div v-if="isStudent" :class="{subject__visited: true, visited: subject.attendance}">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="day__right">
                                        <div v-for="subject, ind in item.subjects" class="right__item">
                                            <div v-if="subject.isElective" class="subject elective">
                                                <h4 class="subject__title">
                                                    {{ subject.name }}
                                                </h4>
                                                <div class="subject__time">
                                                    {{ subject.startTime }}-{{ subject.endTime }}
                                                </div>
                                                <div class="subject__class">
                                                    {{subject.location}}
                                                </div>
                                                <div v-if="isStudent" :class="{subject__visited: true, visited: subject.attendance}">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                </div>
                <div @click="goEditSchedule" v-if="isStudent" class="schedule__edit">
                    <a>изменить расписание</a>
                </div>
            </div>
        </div>
    </main>
</template>
<style scoped>
    .schedule__row {
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
        display: flex;
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

    @media(max-width: 1400px) {
        .day__row {
            display: block;
        }
        .day__left {
            border: 0;
        }
    }

    @media(max-width: 900px) {
        .shedule__title h2 {
            font-size: 40px;
        }
        .schedule__row {
            display: flex;
            margin-bottom: 40px;
            justify-content: space-around;
        }
        .schedule__row a {
            display: block;
            color: #fff;
            font-size: 20px;
            line-height: 56px;
            text-align: center;
            width: 60px;
            height: 60px;
            border: 2px solid rgba(0,0,0,50%);
            border-radius: 30px;
        }
        .schedule__row a.active {
            background: #fff;
            color: #323843;
        }
        .day {
            display: none;
        }
        .day.visible {
            display: block;
        }
        .shedule {
            border: 0;
        }
        .day__row {
            display: block;
            background: transparent;
            border: 0;
            padding: 0;
            border-radius: 0;
        }
        .subject {
            display: block;
            background: rgba(0,0,0,20%);
            border: 2px solid rgba(0,0,0,50%);
            border-radius: 20px;
            padding: 20px;
            font-size:  24px;
        }
        .subject__time {
            text-align: right;
            color: #323843;
        }
        .subject__visited {
            display: none;
        }
        .container {
            width: 100%;
        }

        .shedule {
            padding: 40px 0;
        }
    }

    @media (max-width: 500px) {
        .schedule__row {
            justify-content: space-between;
        }

        .shedule__title {
            margin-bottom: 20px;
        }
        .shedule__title h2 {
            font-size: 30px;
        }
        .schedule__row a {
            width: 50px;
            height: 50px;
            font-size: 18px;
            line-height: 46px;
            border-radius: 25px;
        }
    }
</style>