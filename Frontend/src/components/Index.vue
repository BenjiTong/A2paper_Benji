<template>
  <div class="red20">
    {{ msg }}
  </div>
</template>

<script>
export default {
  data () {
    return {
      msg: 'This is a temp Index!'
    }
  }
}
</script>

<style scoped>
.red20 {
  color: red;
  font-size: 20px;
}
</style>
