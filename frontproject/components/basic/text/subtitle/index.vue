<template>
    <h3 
        class="title"
    >
        {{text}}
    </h3>
</template>
  
<script>
export default {
    props: {
        text: {
            type: String,
            required: true
        }
    }
}
</script>

<style lang="sass" scoped>
    .title
        height: fit-content
</style>