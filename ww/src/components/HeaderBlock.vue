<script>
    export default {
        methods: {
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
            goInfo() {
                this.$router.push({
                    name: "info"
                });
            },
            goAbout() {
                document.querySelector("#about").scrollIntoView();
            }
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
                    <li><a @click="goInfo">информация</a></li>
                    <li><a @click="goHome(true)">о нас</a></li>
                    <li><a>мяу</a></li>
                    <li><a>прочее</a></li>
                </ul>
            </div>
        </div>
    </header>
</template>
<style scoped>
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
</style>