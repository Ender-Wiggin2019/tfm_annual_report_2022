<template>
  <div>
    <div class="d">
      {{ userTotal["createtime"] }}
    </div>
    <div class="a">
      你使用
      <span class="value">
        {{ userTotal["corporation"] }}
      </span>
      <span class="value" v-if="userTotal['corporation2'] !== null">
        和 {{ userTotal["corporation2"] }}
      </span>
      公司<br>
      在
      <span class="value">
        {{ userTotal["generations_4p_score"] }}
      </span>
      时代怒刷
      <span class="value">
        {{ userTotal["playerScore_4p_score"] }}
      </span>
      分

    </div>
    <div class="b">
      在同时代中位列第
      <span class="value">
        {{ userTotal["rn2"] }}
      </span>
      名
    </div>


    <div class="e" style="padding-top: 5vh; font-size: 5vw">还能记起来那天的精彩操作吗</div>
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
  created() {
    const userData = {
      'name': this.$store.state.name,
    }
    console.log(this.$store.state.name);
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
  // computed: {
  //   userType(){
  //     return this.$store.state.userType
  //   }
  // },
  // created() {
  //   const userData = {
  //     'name': this.$store.state.name,
  //   }
  //   getAPI.post('/api/account/usertype/', userData, {
  //     headers: {
  //       'Authorization': `Bearer ${this.$store.state.accessToken}`,
  //     }
  //   })
  //       .then(res => {
  //         this.$store.state.userType = res.data.type;
  //       })
  //       .catch(err => console.error(err))
  // }
};
</script>

<style scoped>
.a,
.b,
.c,
.d,
.e,
.f {
  /*text-align: center;*/
  color: white;
}
.a {
  font-size: 5vw;
  padding-top: 5vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 0.5s;
  animation-fill-mode: backwards;
}
.b {
  /*padding-top: 5vh;*/
  font-size: 5vw;
  white-space: normal;
  text-overflow: ellipsis;
  overflow: hidden;
  line-height: 2;
  color: ebf45f;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-fill-mode: backwards;
}
.c {
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1.5s;
  animation-fill-mode: backwards;
}
.d {
  font-size: 5vw;
  text-align: right;
  padding-top: 12vh;
  font-weight: bolder;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2s;
  animation-fill-mode: backwards;
}
.e{
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2.5s;
  animation-fill-mode: backwards;
}
</style>
