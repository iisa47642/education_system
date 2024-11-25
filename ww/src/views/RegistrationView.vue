<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                password: "",
                username: "",
                email: "",
                error: false
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
            // типо подгрузка данных
            async loadData(username, password, email) {
                if (!username || !password || !email) {
                    this.error = true;
                } else {
                    this.error = false;
                    let response = axios.post("/registration", {
                        username: username,
                        password: password,
                        email: email
                    });
                    response.then((result) => {
                        console.log(result.status);
                        if (String(result.status)[0] == "2") {
                            localStorage.setItem('accessToken', result.data.access);
                            localStorage.setItem('refreshToken', result.data.refresh);
                            let data = this.parseJwt(result.data.access);
                            console.log(data);
                            this.$router.push({name: "profile", params: {id: data.user_id}});
                        }
                        
                    });
                }
            }
        }
    }
</script>
<template>
    <main>
        <div class="circle">
            <div class="register-form-container">
                <h1 class="form-title">
                    регистрация
                </h1>
                <div class="form-fields">
                    <div class="form-field">
                        <h3 class="log">ЛОГИН: </h3><input v-model="username" name="username" class="vvod" type="text">
                    </div>
                    <div class="form-field">
                        <h3 class="password">ПАРОЛЬ: </h3><input v-model="password" class="vvod" type="password">
                    </div>
                    <div class="form-field">
                        <h3 class="password">ПОЧТА: </h3><input v-model="email" class="vvod1" type="text">
                    </div>
                </div>
                <div class="form-buttons">
                    <button @click="loadData(this.username,this.password, this.email)" class="button"><h3 class="enter">РЕГИСТРАЦИЯ</h3></button>
                    <div v-if="this.error" class="error">ошибка: данные неверные</div>
                    <div class="divider"><a href= "/recover" class="recover">восстановить доступ</a></div>
                </div>
            </div>
        </div>

    </main>
</template>
<style scoped>
main {
    font-family: "Bona Nova SC", serif;
    font-style: normal;
    display: flex;
    align-items: center;
    justify-content: center;
}
.circle {
    max-width: 800px;
    width: 70%;
    top: 100px;
    text-align: center;
    box-shadow: 0px 4px 4px 0px #00000040;
    border: 700px;
    border-radius: 20px;
    background: #fff;
    padding: 40px 80px;
}

.form-title {
    font-size: 50px;
    font-weight: 700;
    color: #323843;
    margin-bottom: 40px;
}

.form-field {
    display: flex;
    justify-content: space-between;
}

.form-fields {
    margin-bottom: 20px;
}

.form-field h3 {
    font-size: 30px;
    color: #323843;
    font-weight: 700;
    align-items: center;
    padding-right: 10px;
    flex: 0 1 180px;
 
}
.form-field input{
    border: 2px solid #323843;
    flex: 1 1 auto;
    line-height: 34px;
    font-size: 24px;
    background: #C6D0E0;
    padding-left: 10px;
}

.form-field:not(:last-child) {
    margin-bottom: 30px;
}

.button {
    font-size: 30px;
    font-weight: 700;
    background: #323843;
    color: #fff;
    line-height: 1.5;
    border: 2px solid #000;
    border-radius: 22px;
    padding: 0 2em;
    margin-bottom: 20px;
    transition-duration: 200ms;
}

.button:hover {
    color: #323843;
    background: #fff;
}

.recover {
    font-size: 20px;
    font-weight: 700;
    line-height: 1;
    color: #7e7f7f;
}

.error {
    font-size: 20px;
    font-weight: 700;
    color: #323843;
    line-height: 1;
    margin-bottom: 10px;
}
</style>