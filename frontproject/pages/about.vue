<template>
    <article class="main">
      <section class="main-about">
          <hgroup class="main-about-title">
              <h1>About</h1>
          </hgroup>
      </section>
  </article>
</template>

<script lang="ts">
export default {
    layout: 'base'
}
</script>

<style lang="sass" scoped>
    .main
        min-height: calc(100vh - 74px)
        display: grid
        grid-template-columns: 1fr
        @media screen and (min-width: 1024px)
            grid-template-columns: repeat(2, 1fr)
            
        &-about
            padding: 5rem
            background: #00000099
            display: grid
            grid-template-rows: auto
            max-height: 900px
            color: #fff
            &-title
                h1
                    text-align: center
                    font-size: 3rem
                    font-weight: bold
                    text-decoration: underline 
                    @media screen and (min-width: 1024px)
                        padding-bottom: 2rem
</style>