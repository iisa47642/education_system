<script>
</script>
<template>
    <footer>
        <div class="container">
            <div class="footer__row">
                <h2>связаться с нами: </h2>
                <ul class="footer__menu">
                    <li class="first"><a href="">tg: telegram.tg</a></li>
                    <li><a href="">vk: vkontakte.vk</a></li>
                </ul>
                <h2 class="copy">2024 win win</h2>
            </div>
        </div>
    </footer>
</template>
<style scoped>
footer {
    font-family: "Bona Nova SC", serif;
    background: #323843;
    color: #fff;
    font-size: 20px;
    font-weight: 700;
    line-height: 1;
    padding: 24px 0;
}
h2 {
    font-size: 20px;
    font-weight: 700;
    line-height: 1; 
}

.footer__row {
    display: flex;
    justify-content: center;
    align-items: center;
}

.footer__menu {
    padding: 0 80px;
}

footer a {
    color: #fff;
}

.copy {
    position: relative;
    padding-left: 18px;
}

.copy:before {
    content: '©';
    position: absolute;
    left: 0;
    top: 2px;
}

.footer__menu .first {
    margin-bottom: 8px;
}
</style>