<script>
    import axios from "axios";
    export default {
        data() {
            return {
                access: localStorage.getItem("accessToken"),
                refresh: localStorage.getItem("refreshToken"),
            }
        },
        methods: {
            burger() {
                let menu = document.querySelector(".header__menu");
                menu.classList.toggle("active");
            },
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
                    localStorage.setItem('accessToken', newAccessToken);
                    localStorage.setItem('refreshToken', newRefreshToken);
                })
                .catch(error => {
                    this.$router.push({name: "login"});
                });
                },
                // типо подгрузка данных
                sleep(ms) {
                    return new Promise(resolve => setTimeout(resolve, ms))
                },
            async goHome(flag) {
                if (flag) {
                    await this.$router.push({
                    name: "home"
                    });
                    this.goAbout();
                } else {
                    this.$router.push({
                    name: "home"
                    });
                }
            },
            async getId() {
                this.access = localStorage.getItem("accessToken");
                var id = 0;
                try {
                    id = this.parseJwt(this.access).user_id;
                } catch {
                    this.updateTokens();
                }
                if (!id) {
                    await this.sleep(200);
                    this.access = localStorage.getItem("accessToken");
                    id = this.parseJwt(this.access).user_id;
                }
                console.log(id);
                return id;
            },
            goInfo() {
                this.$router.push({
                    name: "info"
                });
            },
            goAbout() {
                document.querySelector("#about").scrollIntoView();
            },
            async goCourses() {
                let id = await this.getId();
                this.$router.push({name: "courses", params: {
                    id: id
                }});
            },
            async goProfile() {
                let id = await this.getId();
                this.$router.push({name: "profile", params: {
                    id: id
                }});
            },
            async goSchedule() {
                let id = await this.getId();
                this.$router.push({name: "schedule", params: {
                    id: id
                }});
            },
            goRating() {
                this.$router.push({name: "rating"});
            }
        },
        mounted() {
            
        }
    }
</script>
<template>
    <header>
        <div class="container">
            <div class="header__block">
                <div class="header__logo">
                    <a @click="goHome(false)">ww.study</a>
                </div>
                <ul class="header__menu">
                    <li><a @click="goHome(true)">о нас</a></li>
                    <li><a @click="goCourses">мои курсы</a></li>
                    <li><a @click="goSchedule">расписание</a></li>
                    <li><a @click="goRating">рейтинг</a></li>
                    <li><a @click="goProfile">кабинет ст.</a></li>
                </ul>
                <div class="burger-menu">
                    <a @click="burger"></a>
                </div>
            </div>
        </div>
    </header>
</template>
<style scoped>
    .burger-menu {
        display: none;
    }
    .burger-menu a {
        width: 60px;
        height: 60px;
        background: #fff;
        display: block;
    }
    header {
        background: #323843;
        font-size: 20px;
        line-height: 1;
        font-weight: 700;
        text-transform: uppercase;
        font-family: "Bona Nova SC", serif;
        position: sticky;
        top: 0;
        z-index: 1984;
    }
    header a {
        color: #CCCECD;
        cursor: pointer;
    }

    .header__logo {
        font-family: "Elsie Swash Caps", serif;
        font-size: 30px;
        line-height: 1;
    }
    .header__block {
        display: flex;
        justify-content: space-between;
        padding: 30px 0;
        align-items: center;
    }

    .header__menu {
        display: flex;
    }
    .header__menu a {
        font-size: 16px;
        line-height: 1;
        padding: 10px 30px 8px;
        display: block;
        position: relative;
        transition-duration: 200ms;
        border-bottom: 2px solid transparent;
    }
    .header__menu a:hover {
        border-bottom: 2px solid #CCCECD;
    }
    .header__menu a::before {
        content: '';
        position: absolute;
        display: block;
        width: 14px;
        height: 14px;
        background: #CCCECD;
        left: 0;
        top: 10px;
        border-radius: 7px;
    }

    @media (max-width: 1150px) {
        .burger-menu {
            display: block;
        }
        .header__menu {
            position: fixed;
            left: 0;
            top: -500px;
            z-index: 10;
            background: #323843;
            display: block;
            width: 100%;
            text-align: center;
            transition-delay: 200ms;
        }
        .header__menu.active {
            top: 120px;
        }
        .header__menu a:before {
            display: none;
        }
    }
</style>