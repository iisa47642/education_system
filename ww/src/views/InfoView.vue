<script></script>
<template>
    <main>
        <div class="container">
            <h2>Информация о проекте</h2>
            <div class="info">
                <div class="info__elem info__elem1">
                    <div class="elem__body">
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugiat cum blanditiis quidem, quas, facere esse distinctio modi at repellat saepe illum dicta sapiente. Quis reiciendis inventore, sint nesciunt nostrum laborum.</p>
                    </div>
                </div>
                <div class="info__elem info__elem2">
                    <div class="elem__body">
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Debitis, minima.</p>
                    </div>
                </div>
                <div class="info__elem col info__elem3">
                    <div class="elem__body">
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis qui dignissimos quos similique maiores odio odit, ea aliquam sed necessitatibus sequi temporibus aperiam quidem perferendis! Quasi cum quam dignissimos facere!</p>
                        
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>
<style scoped>
    main {
        padding: 120px 0;
    }
    h2 {
        font-family: "Bona Nova", serif;
        color: #323843;
        font-size: 27px;
        text-align: center;
        margin-bottom: 80px;
    }
    .info {
        display: grid;
        gap: 30px;
        grid-template-areas:
        "A C"
        "B C";
    }
    .info__elem {
        background: #222;
        width: 100%;
        border-radius: 80px;
        padding: 20px;
        color: #fff;
    }

    .elem__body p {
        padding: 20px;
    }

    .elem__img {
        position: relative;
        padding-bottom: 40%;
    }

    .elem__img img {
        width: 100%;
        height: 100%;
        position: absolute;
        left: 0;
        top: 0;
        object-fit: cover;
    }
    .info__elem1 {
        grid-area: A;
    }
    .info__elem2 {
        grid-area: B;
    }
    .info__elem3 {
        grid-area: C;
        padding: 40px;
    }
</style>