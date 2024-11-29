<script>
    import HeaderBlock from "./components/HeaderBlock.vue";
    import FooterBlock from "./components/FooterBlock.vue";
    import {RouterView} from "vue-router";

    export default {
      components: {
        HeaderBlock,
        RouterView,
        FooterBlock,
      }
    }
</script>

<template>
  <div class="wrapper">
    <header-block></header-block>
    <RouterView />
    <footer-block></footer-block>
  </div>
</template>

<style>
</style>
