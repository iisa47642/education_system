<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                userId: this.$route.params.id,
                name: "Фамилия Имя Отчество",
                birthdate: "20.20.2020",
                degree: "мемология",
                course: 52,
                info: "информация",
                gpa: 87,
                perc: 94,
                image: "",
                user: {}
            }
        },
        methods: {
            // типо подгрузка данных
            async loadData(id) {
                let data = await axios.get("/profile", {
                    params: {id: id}
                });
                this.user = data.data[0];
                console.log(data);
            },
            goCourses(id) {
                this.$router.push({name: "courses", params: {id: id}});
            },
            goShedule(id) {
                this.$router.push({name: "shedule", params: {id: id}})
            }
        },
        mounted() {
            this.loadData(this.userId);
        }
    }
</script>
<template>
    <main>
        <div class="container">
            <div class="profile__row">
                <div class="profile__left">
                    <h2>Привет, студент!</h2>
                    <h3>ww.study <br> cabinet</h3>
                    <ul class="left__menu">
                        <li id="one"><a @click="goCourses(this.id)"><span>мои курсы</span></a></li>
                        <li id="two"><a @click="goShedule(this.id)"><span>мое расписание</span></a></li>
                        <li id="three"><a><span>рейтинг</span></a></li>
                        <li id="four"><a><span>настройки</span></a></li>
                    </ul>
                </div>
                <div class="profile__right">
                    <div class="profile__img">
                        <div class="img__profile">
                            <img src="" alt="">
                        </div>
                    </div>
                    <h3>{{ this.user.username }} {{ this.user.surname }}</h3>
                    <div class="right__info">
                        <p>Дата рождения: {{ this.user.birthdate }}</p>
                        <p>Профиль: {{ this.user.profile }}</p>
                        <p>Курс: {{ this.course }}</p>
                        <p>Др. Информация: {{ this.user.course }}</p>
                    </div>
                    <div class="right__grade">
                        <h3>Успеваемость</h3>
                        <div class="grade__row">
                            <div class="grade__col">
                                <p>gpa</p>
                                <span>{{ this.user.gpa }}%</span>
                            </div>
                            <div class="grade__col">
                                <p>perc</p>
                                <span>{{ this.user.perc }}%</span>
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
        display: grid;
        background: rgb(111,131,143);
        background: linear-gradient(90deg, rgba(111,131,143,1) 0%, rgba(131,133,138,1) 50%, rgba(147,142,136,1) 100%);
    }
    .container {
        margin: 0 auto;
    }
    .profile__row {
        display: flex;
        height: 100%;
    }

    .profile__left {
        flex: 0 1 50%;
        background: rgba(0,0,0,30%);
        padding: 40px 60px 0;
        border-left: 3px solid rgba(0,0,0,50%);
        border-right: 3px solid rgba(0,0,0,50%);
    }

    .profile__left h2 {
        font-size: 45px;
        font-family: "Bona Nova", serif;
        text-transform: uppercase;
        font-weight: 700;
        color: #fff;
        margin-bottom: 15px;
    }

    .profile__left  h3 {
        font-size: 45px;
        font-family: "Elsie Swash Caps", serif;
        font-weight: 900;
        color: #C6D0E0;
        text-transform: uppercase;
        margin-bottom: 100px;
    }

    .left__menu {
        padding: 10px 0 10px 30px;
    }

    .left__menu a {
        font-family: "Bona Nova SC", serif;
        color: #fff;
        font-size: 35px;
        font-weight: 700;
        cursor: pointer;
        display: block;
        line-height: 1;
        padding-left: 120px;
        position: relative;
        margin-bottom: 20px;
    }

    .left__menu a:before {
        content: '';
        width: 80px;
        height: 90px;
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        border-right: 2px solid #fff;
    }

    #one a:before {
        background: url(../assets/icons/bundle2.png) 0 50% no-repeat;
    }
    #two a:before {
        background: url(../assets/icons/hat2.png) 0 50% no-repeat;
    }
    #three a:before {
        background: url(../assets/icons/stars.png) 0 50% no-repeat;
    }
    #four a:before {
        background: url(../assets/icons/wheel.png) 0 50% no-repeat;
    }
    .left__menu li:not(:last-child) {
        padding-bottom: 20px;
    }
    .left__menu a span {
        border-bottom: 2px solid transparent;
        transition-duration: 200ms;
    }
    .left__menu a:hover span {
        border-bottom: 2px solid #fff;
    }
    .profile__right {
        flex: 0 1 50%;
        border-right: 3px solid rgba(0,0,0,50%);
        text-align: center;
        padding: 40px 40px 20px;
    }
    .profile__img {
        max-width: 220px;
        margin: 0 auto 40px;
    }
    .img__profile {
        border-radius: 50px;
        overflow: hidden;
        position: relative;
        width: 100%;
        padding-bottom: 100%;
        background: #fff;
    }

    .img__profile img {
        width: 100%;
        height: 100%;
        position: absolute;
        left: 0;
        top: 0;
        object-fit: cover;
        line-height: 1;
    }

    .profile__right h3 {
        color: #fff;
        font-family: "Bona Nova", serif;
        font-size: 35px;
        margin-bottom: 40px;
        font-weight: 700;
        line-height: 1;
    }

    .right__info {
        color: #fff;
        border-left: 2px solid #fff;
        text-align: left;
        padding: 10px 0 10px 20px;
        font-weight: 700;
        font-family: "Bona Nova SC", serif;
        font-size: 30px;
        margin-bottom: 40px;
    }
    .right__info p:not(:last-child) {
        padding-bottom: 20px;
    }

    .right__grade {
        background: rgba(0,0,0,30%);
        border: 2px solid #323843;
        padding: 20px 50px 50px;
    }

    .right__grade h3 {
        font-size: 30px;
        text-transform: uppercase;
    }

    .grade__row {
        display: flex;
        justify-content: space-between;
    }

    .grade__col {
        color: #fff;
    }
    .grade__col p {
        font-family: "Elsie Swash Caps", serif;
        font-size: 60px;
        font-weight: 700;
        text-transform: uppercase;
        line-height: 1;
        margin-bottom: 30px;
    }
    .grade__col span {
        font-family: "Bona Nova", serif;
        font-size: 30px;
        font-weight: 700;
        line-height: 1;

    }
</style>