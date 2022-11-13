<template>
  <div>
    <div class="a">这一年在大家的齐心协力下</div>
    <div class="b">火星上一共建造了<span class="value">2905</span>座小型风车</div>
    <div class="c">寻找了<span class="value">5068</span>次地外生命</div>
    <div class="d">养育了<span class="value">28258</span>只缓步微生物</div>
    <div class="e">不积跬步，无以至千里~</div>
    <div class="f">出发去看看我们的2022吧~</div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.a,
.b,
.c,
.d,
.e,
.f {
  text-align: center;
  color: white;
}
.a {
  font-size: 5vw;
  padding-top: 10vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: .5s;
  animation-fill-mode: backwards;
}
.b {
  font-size: 4vw;
  padding-top: 3vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-fill-mode: backwards;
}
.c {
  font-size: 4vw;
  padding-top: 3vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1.5s;
  animation-fill-mode: backwards;
}
.d {
  font-size: 4vw;
  padding-top: 3vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2.0s;
  animation-fill-mode: backwards;
}
.e {
  font-size: 6vw;
  padding-top: 10vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2.5s;
  animation-fill-mode: backwards;
}
.f {
  font-size: 6vw;
  padding-top: 3vh;
  font-weight: lighter;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 3.0s;
  animation-fill-mode: backwards;
}
</style>
