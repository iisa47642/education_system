<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                userId: this.$route.params.id,
                isStudent: "",
                user: {}
            }
        },
        methods: {
            parseJwt(token) {
                var base64Url = token.split('.')[1];
                var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
                var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
                    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
                }).join(''));
                return JSON.parse(jsonPayload);
            },
            updateTokens() {

                axios.post('/token/refresh/', { refresh: localStorage.getItem('refreshToken')})
                .then(response => {
                    const newAccessToken = response.data.access;
                    const newRefreshToken = response.data.refresh;
                    localStorage.setItem('accessToken', newAccessToken)
                    localStorage.setItem('refreshToken', newRefreshToken)
                })
                .catch(error => {
                    this.$router.push({name: "login"});
                });
            },
            // типо подгрузка данных
            sleep(ms) {
                return new Promise(resolve => setTimeout(resolve, ms))
            },

            async loadData(id) {
                let response = await axios.get("/profile", {
                    params: {id: id},
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                }).catch( e => {
                    try {
                        this.updateTokens();
                    } catch {
                        this.$router.push({name: "login"});
                    }
                });
                if (!response) {
                    await this.sleep(200);
                    response = await axios.get("/profile", {
                    params: {id: id},
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                    });
                }
                console.log(response.data);
                this.user = response.data[0];
                if (response.data[0].groups[0] == "student") {
                    this.isStudent = true;
                } else {
                    this.isStudent = false;
                }
            },
            goCourses(id) {
                this.$router.push({name: "courses", params: {id: id}});
            },
            goShedule(id) {
                this.$router.push({name: "schedule", params: {id: id}});
            },
            goRating(id) {
                this.$router.push({name: "rating", params : {id: id}});
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
                    <h2 v-if="!isStudent">Здравствуйте, {{ this.user.username }}</h2>
                    <h2 v-if="isStudent">Привет, студент!</h2>
                    <h3>ww.study <br> cabinet</h3>
                    <ul class="left__menu">
                        <li id="one"><a @click="goCourses(this.id)"><span>мои курсы</span></a></li>
                        <li id="two"><a @click="goShedule(this.id)"><span>мое расписание</span></a></li>
                        <li id="three"><a @click="goRating(this.id)"><span>рейтинг</span></a></li>
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
                        <p>Курс: {{ this.user.course }}</p>
                        <p>Др. Информация: {{ this.user.additional_info }}</p>
                    </div>
                    <div v-if="isStudent"class="right__grade">
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
    @media (max-width: 1400px) {
        .left__menu a {
            margin-bottom: 10px;
        }
    }
    @media (max-width: 1200px) {
        .grade__col p {
            font-size: 40px;
        }
        .profile__left {
            padding: 40px;
        }
        .left__menu {
            padding: 0;
        }
    }
    @media (max-width: 1000px) {
        .left__menu a:before {
            height: 70px;
            display: none;
        }
        .left__menu li:not(:last-child) {
            padding-bottom: 0;
        }
        .left__menu a {
            padding-left: 0;
            font-size: 32px;
        }
    }
    @media (max-width: 900px) {
        .profile__row {
            flex-direction: column;
            border-right: 2px solid rgba(0,0,0,50%);
            border-left: 2px solid rgba(0,0,0,50%);
        }
        .profile__left {
            border: 0;
            background: 0;
            text-align: center;
            padding: 0;
            padding-top: 40px;
        }
        .profile__left h3 {
            margin-bottom: 40px;
        }

        .left__menu {
            background: rgba(0,0,0,27%);
            border-top: 2px solid rgba(0,0,0,50%);
            border-bottom: 2px solid rgba(0,0,0,50%);
        }

        .left__menu a {
            line-height: 2;
        }
        .profile__right {
            border: 0;
        }
        .grade__row {
            justify-content: space-around;
        }
        .right__grade {
            padding: 30px;
        }
    }
    @media (max-width: 600px) {
        .profile__left {
            padding-top: 20px;
        }
        .profile__left h2 {
            font-size: 36px;
        }
        .profile__left h3 {
            font-size: 30px;
            margin-bottom: 20px;
        }
        .profile__row {
            border-right: 0;
            border-left: 0;
        }
        .container {
            width: 100%;
            padding: 0;
        }
        .right__info {
            font-size: 24px;
        }
    }
    @media (max-width: 420px) {
        .right__grade h3 {
            font-size: 24px;
        }

        .grade__col p {
            font-size: 30px;
        }
    }
</style>