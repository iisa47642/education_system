<script>
    import dayjs from "dayjs";
    import axios from "axios";
    import "dayjs/locale/ru";
    dayjs.locale("ru");

    export default {
        data() {
            return {
                date: dayjs().format("DD.MM.YYYY"),
                userId: this.$route.params.id,
                weekNumber: 1,
                schedule: [
                    {
                        day: "Monday",
                        subjects: [],
                        today: false,
                    },
                    {
                        day: "Tuesday",
                        subjects: [],
                        today: false,
                    },
                    {
                        day: "Wednesday",
                        subjects: [],
                        today: false,
                    },
                    {
                        day: "Thurday",
                        subjects: [],
                        today: false,
                    },
                    {
                        day: "Friday",
                        subjects: [],
                        today: false,
                    },
                    {
                        day: "Saturday",
                        subjects: [],
                        today: false,
                    },
                ],
            }
        },
        methods: {
            getDate(date) {
                console.log(date);
            },
            createShedule(s) {
                for (let i = 0; i < s.length; i++) {
                    if (s[i].week_number == this.weekNumber) {
                        this.schedule[s[i].week_day_number-1].subjects.push(
                            {
                                name: s[i].subjectId.name,
                                startTime: dayjs(s[i].startTime).format("HH:mm"),
                                endTime: dayjs(s[i].endTime).format("HH:mm"),
                                location: s[i].location.name,
                                order: s[i].lesson_number
                            }
                        )
                    } else {
                        console.log(this.weekNumber);
                        console.log(s.week_number);
                    }
                }
                for (let i = 0; i < 6; i++) {
                    this.schedule[i].subjects.sort(function(a, b) {
                    return parseFloat(a.order) - parseFloat(b.order);
                    });
                }
            },
            async loadData(id) {
                let response = await axios.get("/schedule", {
                    params: {id: id}
                });
                this.createShedule(response.data);
                console.log(response.data);
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
                    <div v-for="item, index in schedule" class="day">
                        <h3>{{item.day}}</h3>
                        <div class="day__block">
                            <div class="day__row">
                                <div class="day__left">
                                    <div class="left__item">
                                        <div v-for="subject, ind in item.subjects"  class="subject non-elective">
                                            <h4 class="subject__title">
                                                {{ subject.name }}
                                            </h4>
                                            <div class="subject__time">
                                                {{ subject.startTime }}-{{ subject.endTime }}
                                            </div>
                                            <div class="subject__class">
                                                {{subject.location}}
                                            </div>
                                            <div class="subject__visited">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="day__right">
                                    <div class="right__item">
                                        <div class="subject elective">
                                            <div class="subject__title">
                                                
                                            </div>
                                            <div class="subject__time">
                                                
                                            </div>
                                            <div class="subject__class">
                                                
                                            </div>
                                        </div>
                                    </div>
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

    .day:not(:last-child) {
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
</style>