<script>
    import axios from 'axios';
    export default {
        data() {
            return {
                userId: this.$route.params.id,
                courses: [
                    {
                        title: "Математический Анализ",
                        image: ""
                    },
                    {
                        title: "Предмет 2",
                        image: ""
                    },
                    {
                        title: "Предмет 3",
                        image: ""
                    },
                    {
                        title: "Предмет 4",
                        image: ""
                    },
                    {
                        title: "Предмет 5",
                        image: ""
                    },
                    {
                        title: "Предмет 6",
                        image: ""
                    }
                ],
                courses2: []
            }
        },
        methods: {
            async loadData(id) {
                let response = await axios.get("/courses", {
                    params: {id: id},
                    headers: {
                        'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
                    },
                });
                this.courses2 = response.data;
                console.log(response.data);
            },
            goCourse(cid) {
                this.$router.push({name: "course", params: {id: this.userId, cid: cid}})
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
            <div class="courses">
                <div class="title__padding">
                    <h2 class="courses__title">Мои курсы</h2>
                </div>
            <div class="courses__row">
                <div v-for="item,index in courses2" class="courses__item course">
                        <div @click="goCourse(item.id)" class="course__body">
                            <div class="course__img">
                
                            <img src="../assets/imgs/image.png" alt="">
                        </div>
                        <div class="course__title">
                            <p>{{ item.name }}</p>
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
        background: rgb(111,131,143);
        background: linear-gradient(90deg, rgba(111,131,143,1) 0%, rgba(131,133,138,1) 50%, rgba(147,142,136,1) 100%);
    }
    .courses {
        border-left: 2px solid rgba(0,0,0,50%);
        border-right: 2px solid rgba(0,0,0,50%);
    }
    .courses {
        padding: 40px 0;
        color: #fff;
    }

    .title__padding {
        padding: 0 80px;
    }

    .courses__title {
        font-family: "Bona Nova", serif;
        font-size: 55px;
        font-weight: 700;
        text-transform: uppercase;
        position: relative;
        padding-left: 100px;
    }
    .courses__title:before {
        content: '';
        display: block;
        height: 90px;
        width: 80px;
        position: absolute;
        left: 0;
        top: 50%;
        transform: translateY(-50%);
        background: url(../assets/icons/bundle.png) 50% 50% no-repeat;
    }

    .courses__row {
        display: flex;
        flex-wrap: wrap;
    }

    .course {
        flex: 0 1 50%;
        padding: 40px 80px;
    }

    .course__body {
        padding: 30px;
        background: rgba(50,56,67,30%);
        border: 3px solid rgba(0,0,0, 30%);
        transition-duration: 200ms;
        cursor: pointer;
        text-align: center;
    }

    .course__body:hover {
        background: rgba(255,255,255,30%);
        color: #323843;
    }

    .course__img {
        width: 100%;
        position: relative;
        padding-bottom: 50%;
        border-radius: 50px;
        background: #fff;
        overflow: hidden;
        margin-bottom: 20px;
    }

    .course__img img {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .course__title {
        font-size: 27px;
        font-family: "Bona Nova", serif;
        max-width: 80%;
        text-align: center;
        margin: 0 auto;
        overflow: hidden;
        white-space: nowrap;
        position: relative;
        height: 32px;
    }

    .course__title p {
        position: absolute;
        left: 0;
        top: 0;
    }

    @media (max-width: 1200px) {
        .courses__item {
            padding: 40px;
        }
    }

    @media (max-width: 800px) {
        .courses__row {
            display: block;
        }

        .course {
            flex: 1 1 auto;
        }

        .course__img {
            padding-bottom: 40%;
        }

        .title__padding {
            padding: 0 40px;
        }
        .courses__title {
            font-size: 40px;
        }
    }
    @media (max-width: 600px) {
        .courses__item {
            padding: 20px 40px;
        }
        .courses__title {
            font-size: 30px;
        }
        .container {
            width: 100%;
            padding: 0 10px;
        }
        .courses {
            border: 0;
        }
    }

    @media (max-width: 450px) {
        .courses__item {
            padding: 20px 0;
        }
        .course__img {
            padding-bottom: 50%;
        }
    }
</style>