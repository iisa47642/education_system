<script>
    
</script>
<template>
    <main>
        <div class="container">
           <h1 class="main__title">WW.STUDY</h1>
            <a href="">войти в портал</a>
            <p>WW study - учебный портал, обеспечивающий комфортную и эффективную связь учебных заведений со студентами.</p>
            <div class="line"></div> 
        </div>
        <div id="about" class="about">
            <div class="container">
                <div class="about__title">немного о нас: кто такие эти ваши ww?</div>
                <div class="about__img">
                    <div class="img__about">
                        <img src="" alt="">
                    </div>
                </div>
                <p>Мы — группа студентов первого курса Российского технологического университета (РТУ МИРЭА), увлеченных разработкой программного обеспечения. Несмотря на то, что наш опыт в этой области пока небольшой, мы полны энтузиазма и стремления к обучению.</p>
                <p>Наша команда стремится создавать инновационные решения, которые могут принести пользу обществу.</p>
                <p class="last">Проект WW.STUDY - еще один шанс опробовать наши силы и сделать жизнь людей лучше.</p>
                <p class="last">С любовью, WinWin! ❧</p>
                <div class="line"></div>
            </div>
        </div>
    </main>
</template>
<style scoped>
    main .container {
        padding: 270px 0 160px;
        text-align: center;
    }
    h1 {
        font-family: "Elsie Swash Caps", serif;
        font-size: 120px;
        color: #323843;
        text-transform: uppercase;
        margin-bottom: 65px;
    }

    main a {
        font-family: "Bona Nova", serif;
        color: #323843;
        text-transform: uppercase;
        font-size: 27px;
        line-height: 1;
        border: 3px solid #323843;
        letter-spacing: 1px;
        display: inline-block;
        padding: 7px 14px;
        transition-duration: 200ms;
        margin-bottom: 30px;
    }
    main a:hover {
        background: #323843;
        color: #a3a3a3;
    }
    main p {
        font-family: "Bona Nova", serif;
        color: #323843;
        font-size: 27px;
        max-width: 80%;
        margin: 0 auto 100px;
    }
    .line {
        height: 4px;
        max-width: 10%;
        margin: 0 auto;
        background: #323843; 
    }
    .about {
        border-top: 12px solid #323843;
        background: rgb(138,162,175);
        background: linear-gradient(90deg, rgba(138,162,175,1) 0%, rgba(205,208,213,1) 70%, rgba(233,228,222,1) 100%);
    }

    .about .container {
        padding: 120px 0;
    }
    .about__title {
        font-family: "Bona Nova", serif;
        font-weight: 700;
        color: #323843;
        font-size: 35px;
        text-transform: uppercase;
        margin-bottom: 70px;
    }

    .img__about {
        border: 2px solid #000;
        border-radius: 60px;
        position: relative;
        padding-bottom: 20%;
        overflow: hidden;
        margin-bottom: 40px;
    }
    .img__about img {
        position: absolute;
        left: 0;
        right: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .about p {
        margin-bottom: 0;
    }
    .about p.last {
        margin-bottom: 40px;
    }
</style>