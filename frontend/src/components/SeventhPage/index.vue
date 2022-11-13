<template>
  <div>
    <div class="a">
      你最喜欢的前序是
      <!--      <span class="value"> {{ userTotal["create_no"] }} </span>-->
      <span class="value"> {{ userTotal["prelude"] }} </span>
    </div>
    <div class="b">
      足足打出了
      <!--      <span class="value"> {{ userTotal["create_no"] }} </span>-->
      <span class="value"> {{ userTotal["prelude_total"] | numFilter}} </span>
      次
    </div>

    <div class="c">
      随你出征次数最多的公司是
      <span class="value"> {{ userTotal["corporation_fav_corp"] }} </span><br>
      你们一起吃了<span class="value"> {{ userTotal["first"] }} </span>次鸡

    </div>

    <div class="d">
    <span v-if="userTotal['first'] / userTotal['total_fav_corp'] >= 0.7">
      所向披靡，战无不胜
      </span>
      <span v-else>
        千山万水，初心未改
      </span>
    </div>

    <!--    <div class="c">-->
    <!--      <div v-for="(count, word, index) in loveWord" :key="index">-->
    <!--        说{{ word }} <span class="value"> {{ count }} </span>次-->
    <!--      </div>-->
    <!--      <div>...</div>-->
    <!--    </div>-->
    <!--    <div class="d">比起网络<br />我们更喜欢在现实表达爱意</div>-->
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
  padding-top: 15vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: .5s;
  animation-fill-mode: backwards;
}
.b{
  font-size: 5vw;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-fill-mode: backwards;
}
.c{
  font-size: 5vw;

  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2s;
  animation-fill-mode: backwards;
}
.d {
  padding-top: 10vh;
  font-size: 5vw;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2.5s;
  animation-fill-mode: backwards;
}

</style>
