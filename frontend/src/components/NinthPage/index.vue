<template>
  <div class="v">
    <div class="a">
      <div class="b">#2022</div>
      <div class="c">火星年度报告</div>
<!--      <div class="d">称号</div>-->
<!--      <div class="e">吃</div>-->
<!--      <div class="f"></div>-->
      <div class="d">称号</div>
      <div class="e" style="font-size: 5vw" ><pre>{{userTotal["ac"] }} </pre></div>
<!--      <div class="e">{{ b }}</div>-->
<!--      <div class="f"></div>-->
<!--      <div class="d">话痨月</div>-->
<!--      <div class="e" style="font-size: 5vw">{{ c }}月</div>-->
<!--      <div class="f"></div>-->
      <div class="h">
        <img class="p" src="@/assets/images/result.png" />
        <img class="y" src="@/assets/images/cloud2.png" />
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from '@/axios.api'
import data from "@/data.json";
export default {
  data() {
    return {
      ...data,
    };
  },
  computed: {
    userTotal(){
      // return JSON.parse(this.$store.state.userTotal)
      return this.$store.state.userTotal
    }
  },
  filters: {
    numFilter (value) {
      // 截取当前数据到小数点后两位
      let realVal = parseFloat(value).toFixed(0)
      return realVal
    }
  },
  created() {
    const userData = {
      'name': this.$store.state.name,
    }
    getAPI.post('/api/account/userdata/', userData, {
      headers: {
        'Authorization': `Bearer ${this.$store.state.accessToken}`,
      }
    })
        .then(res => {
          // this.$store.state.userTotal = res.data.userTotal;
          this.$store.state.userTotal = JSON.parse(res.data);
        })
        .catch(err => console.error(err))
  }
};
</script>
<style scoped>
.v {
  background-image: linear-gradient(#ff7853, #ffd287);
  height: 100%;
  color: #73e373;
}
.a {
  margin-top: 10vh;
  height: 60vh;
  border: 5px #73e373 solid;
  background: #fef9f9;
  padding: 5vw;
}
.b {
  font-size: 13vw;
  padding-bottom: unset;
}
.c {
  font-size: 5vw;
  font-weight: 700;
  padding-bottom: 5vh;
}
.d {
  color: black;
  font-weight: bold;
  font-size: 10vw;
}
.e {
  margin-top: 2vh;
  color: black;
  /* font-weight: bold; */
  font-size: 8vw;
}
.f {
  height: 1px;
  background: #73e373;
  width: 30vw;
  margin-top: 2vh;
  margin-bottom: 2vh;
}
.p {
  position: absolute;
  width: 27vw;
  left: 55vw;
  top: 15vh;
  z-index: 2;
}
.y {
  position: absolute;
  width: 60vw;
  left: 36vw;
  top: 25vh;
}
.i,
.j {
  position: absolute;
  color: #3c4739;
}
.j {
  font-size: 15vw;
  top: 25vh;
  left: 50vw;
}
.i {
  font-size: 15vw;
  top: 32vh;
  left: 53vw;
}
</style>
