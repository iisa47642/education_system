<script>
    import dayjs from "dayjs";
    import "dayjs/locale/ru";
    dayjs.locale("ru");

    export default {
        data() {
            return {
                date: dayjs(),
                shedule: [
                    {
                        day: "Monday",
                        subjects: [
                            {
                                title: "название занятия №1",
                                startTime: "9:00",
                                endTime: "10:30",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №2",
                                startTime: "10:40",
                                endTime: "12:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №3",
                                startTime: "12:40",
                                endTime: "14:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №4",
                                startTime: "14:20",
                                endTime: "15:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №5",
                                startTime: "16:20",
                                endTime: "17:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №6",
                                startTime: "18:00",
                                endTime: "19:30",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №7",
                                startTime: "19:40",
                                endTime: "21:10",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №8",
                                startTime: "21:20",
                                endTime: "22:50",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                        ]
                    },
                    {
                        day: "Tuesday",
                        subjects: [
                            {
                                title: "название занятия №1",
                                startTime: "9:00",
                                endTime: "10:30",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №2",
                                startTime: "10:40",
                                endTime: "12:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №3",
                                startTime: "12:40",
                                endTime: "14:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №4",
                                startTime: "14:20",
                                endTime: "15:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №5",
                                startTime: "16:20",
                                endTime: "17:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №6",
                                startTime: "18:00",
                                endTime: "19:30",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №7",
                                startTime: "19:40",
                                endTime: "21:10",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №8",
                                startTime: "21:20",
                                endTime: "22:50",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                        ]
                    },
                    {
                        day: "Wednesday",
                        subjects: [
                            {
                                title: "название занятия №1",
                                startTime: "9:00",
                                endTime: "10:30",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №2",
                                startTime: "10:40",
                                endTime: "12:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №3",
                                startTime: "12:40",
                                endTime: "14:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №4",
                                startTime: "14:20",
                                endTime: "15:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №5",
                                startTime: "16:20",
                                endTime: "17:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №6",
                                startTime: "18:00",
                                endTime: "19:30",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №7",
                                startTime: "19:40",
                                endTime: "21:10",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №8",
                                startTime: "21:20",
                                endTime: "22:50",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                        ]
                    },
                    {
                        day: "Thurdsay",
                        subjects: [
                            {
                                title: "название занятия №1",
                                startTime: "9:00",
                                endTime: "10:30",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №2",
                                startTime: "10:40",
                                endTime: "12:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №3",
                                startTime: "12:40",
                                endTime: "14:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №4",
                                startTime: "14:20",
                                endTime: "15:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №5",
                                startTime: "16:20",
                                endTime: "17:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №6",
                                startTime: "18:00",
                                endTime: "19:30",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №7",
                                startTime: "19:40",
                                endTime: "21:10",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №8",
                                startTime: "21:20",
                                endTime: "22:50",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                        ]
                    },
                    {
                        day: "Friday",
                        subjects: [
                            {
                                title: "название занятия №1",
                                startTime: "9:00",
                                endTime: "10:30",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №2",
                                startTime: "10:40",
                                endTime: "12:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №3",
                                startTime: "12:40",
                                endTime: "14:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №4",
                                startTime: "14:20",
                                endTime: "15:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №5",
                                startTime: "16:20",
                                endTime: "17:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №6",
                                startTime: "18:00",
                                endTime: "19:30",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №7",
                                startTime: "19:40",
                                endTime: "21:10",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                            {
                                title: "название занятия №8",
                                startTime: "21:20",
                                endTime: "22:50",
                                class: "209a",
                                visited: false,
                                elective: true,
                            },
                        ]
                    },
                    {
                        day: "Saturday",
                        subjects: [
                            {
                                title: "название занятия №1",
                                startTime: "9:00",
                                endTime: "10:30",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №2",
                                startTime: "10:40",
                                endTime: "12:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №3",
                                startTime: "12:40",
                                endTime: "14:10",
                                class: "209a",
                                visited: true,
                                elective: false,
                            },
                            {
                                title: "название занятия №4",
                                startTime: "14:20",
                                endTime: "15:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                            {
                                title: "название занятия №5",
                                startTime: "16:20",
                                endTime: "17:50",
                                class: "209a",
                                visited: false,
                                elective: false,
                            },
                        ]
                    }
                ]
            }
        },
        methods: {
            getDate(date) {
                console.log(date);
            }
        },
        mounted() {
            this.getDate(this.date);
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
                    <h3>идёт 2 учебная неделя (чёт.) 11.09.2024</h3>
                </div>
                <div class="shedule__col">
                    <div v-for="day, index in shedule"  class="day">
                        <h3>{{ day.day }}</h3>
                        <div class="day__block">
                            <div class="day__row">
                                <div class="day__left">
                                    <div v-for="subject,index in day.subjects" class="left__item">
                                        <div class="subject non-elective" v-if="!subject.elective">
                                            <h4 class="subject__title">
                                                {{ subject.title }}
                                            </h4>
                                            <div class="subject__time">
                                                {{ subject.startTime }}-{{ subject.endTime }}
                                            </div>
                                            <div class="subject__class">
                                                {{ subject.class }}
                                            </div>
                                            <div :class="{subject__visited: true, visited: subject.visited}">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="day__right">
                                    <div v-for="subject,index in day.subjects" class="right__item">
                                        <div v-if="subject.elective" class="subject elective">
                                            <div class="subject__title">
                                                {{ subject.title }}
                                            </div>
                                            <div class="subject__time">
                                                {{ subject.startTime }}-{{ subject.endTime }}
                                            </div>
                                            <div class="subject__class">
                                                {{ subject.class }}
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