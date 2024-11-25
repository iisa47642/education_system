<script>
    import axios from "axios";
    export default {
        data() {
            return {
                rating: []
            }
        },
        methods: {
            async loadData() {
                let response = axios.get("/rating", {
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                response.then( result => {
                    console.log(result);
                    this.rating = result.data;
                });
            }
        },
        mounted() {
            this.loadData();
        }
    }
</script>
<template>
    <main>
        <div class="container">
        <div class="box">
            <img src="../assets/icons/stars.png" class="imgane">
            <h1 class="title">
                РЕЙТИНГ СТУДЕНТОВ
            </h1>
        </div>
        <div class="rating">
            <div class="rating__row">
                <div class="rating__spot">Место</div>
                <div class="rating__name">Фамилия Имя Отчество</div>
                <div class="rating__group">Группа</div>
                <div class="rating__course">Курс</div>
                <div class="rating__gpa">GPA</div>
            </div>
            <div v-for="item,index in rating" class="rating__row rating__item">
                <div class="rating__spot">{{ index + 1 }}</div>
                <div class="rating__name">{{item.username}} {{ item.surname }}</div>
                <div class="rating__group">{{item.student_groups[0]}}</div>
                <div class="rating__course">{{item.course}}</div>
                <div class="rating__gpa">{{item.gpa}}</div>
            </div>
        </div>
        </div>
    </main>
</template>
<style scoped>
    .container {
        padding-top: 40px;
        border-left: rgba(0,0,0,30%) 2px solid;
        border-right: rgba(0,0,0,30%) 2px solid;

    }
    .title {
        font-family: "Bona Nova", serif;
        font-size: 55px;
        font-weight: 700;
        margin: 0;
    }

    .rating {
        padding: 0 80px;
    }

    .rating__row {
        display: flex;
        font-family: "Bona Nova SC", serif;
        font-size: 20px;
        color: #fff;
        font-weight: 700;
        text-align: center;
        margin-bottom: 30px;
    }

    .rating__spot {
        flex: 0 1 120px;
        padding: 0 20px;
    }

    .rating__gpa {
        flex: 0 1 17%;
    }

    .rating__course {
        flex: 0 1 100px;
        padding: 0 10px;
    }

    .rating__group {
        flex: 0 1 160px; 
        padding: 0 10px;
    }

    .rating__name {
        flex: 1 1 auto;
    }

    .rating__item {
        background: rgba(0,0,0,20%);
        border: 2px solid rgba(50,56,67, 50%);
        border-radius: 40px;
        padding: 20px 0;
    }
    .border{
    background: rgba(0, 0, 0, 0.21);
    font-family: Bona Nova SC;
    width: 849px;
    height: 39px;
    top: 534px;
    left: 196px;
    gap: 0px;
    border-radius: 50px 50px 50px 50px;
    border: 3px solid #32384380;
    opacity: 0px;
    word-spacing: 60px;
    text-align: center;
    margin-left: 290px;
    color: rgba(255, 255, 255, 1);
    font-weight: 600;
    line-height: 24px;
    font-size: 15px;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    padding-top: 13px;
}

.name{
    color: rgba(255, 255, 255, 1);
    font-family: Bona Nova SC;
    word-spacing: 55px;
    text-align: center;
    font-size: 17px;
    font-weight: 700;
    line-height: 30px;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    margin-left: 11px;
}

.title{
    font-family: Bona Nova SC;
    color: rgba(255, 255, 255, 1);
    margin-left: 14px;
}


.box{
    display: flex;
    align-items: center;
    margin-bottom: 80px;
}

.image{
    margin-right: 20px;
}

</style>