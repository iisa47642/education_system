<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                email: "",
                sended: false,
                code: "",
                email_error: false,
                code_error: false,
            }
        },
        methods: {
            async recover(email) {
                var pattern = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/; 
                if (email.match(pattern)) {
                    this.email_error = false;
                    this.sended = true;
                    // let response = await axios.get("/recover", {
                    //     params: {
                    //         email: email
                    //     }
                    // });
                    // if (response.status == 200 || response.status == 201) {
                    //     this.sended = true;
                    // } else {
                    //     this.sended = false;
                    //     this.email_error = true;
                    // }
                } else {
                    this.email_error = true;
                }
            },
            async codeRecover(code) {
                let response = await axios.get("/recover", {
                    params: {
                        email: this.email,
                        code: code
                    }
                }).catch(e => { this.code_error = true});
                if (response.status == 200 || response.status == 201) {
                    console.log(response.data);
                } else {
                    this.code_error = true;
                }
            }
        }
    }
</script>
<template>
    <main>
        <div class="container">
            <div class="recover">
                <div class="recover__email">
                    <label for="mail">Почта</label>
                    <input id="mail" v-model="email" type="text">
                 </div>
                 <div class="error" v-if="email_error">Неверная почта</div>
                    <button @click="recover(this.email)">Отправить код восстановления</button>
                <div v-if="sended" class="code">
                    <div class="code__form">
                        <p>Введите код восстановления</p>
                        <input type="text" v-model="code">
                    </div>
                    <div v-if="code_error" class="error">Неверный код</div>
                    <button @click="codeRecover(this.code)" class="no_mb">Восстановить</button>
                </div>
            </div>
        </div>
    </main>
</template>
<style scoped>
    .no_mb {
        margin-bottom: 0;
    }
    .container {
        padding-top: 150px;
    }
    .recover {
        background: #fff;
        padding: 60px 80px;
        max-width: 800px;
        margin: 0 auto;
        border-radius: 40px;
        box-shadow: 0 4px 4px 0 #00000040;
    }
    .recover__email {
        display: flex;
        margin-bottom: 20px;
    }
    label {
        font-family: "Bona Nova SC", serif;
        font-size: 30px;
        font-weight: 700;
        text-transform: uppercase;
        color: #323843;
        padding-right: 40px;
    }
    input {
        background: #C6D0E0;
        border: 2px solid #323843;
        flex: 1 1 auto;
        font-size: 20px;
    }
    input:focus {
        outline: none;
        padding: 0 10px;
    }
    button {
        padding: 0 20px;
        font-size: 20px;
        font-family: "Bona Nova", serif;
        font-weight: 700;
        line-height: 2;
        background: #323843;
        border-radius: 10px;
        color: #fff;
        transition-duration: 100ms;
        margin-bottom: 20px;
    }
    button:hover {
        background: #fff;
        color: #323843;
    }
    p {
        font-size: 20px;
        font-family: "Bona Nova SC", serif;
        font-weight: 700;
        color: #323843;
        margin-bottom: 10px;
    }
    .error {
        margin-bottom: 20px;
        color: #aaa;
        font-size: 20px;
        font-family: "Bona Nova SC", serif;
    }
    .code input {
        font-size: 20px;
        height: 36px;
        margin-bottom: 20px;
        width: 50%;
    }
</style>