<template>
  <div>
    <div class="a">
      你平均每局游戏提升
      <!--      <span class="value"> {{ userTotal["create_no"] }} </span>-->
      <span class="value"> {{ userTotal["increase_tr"]  | numFilter}} </span>
      改造度
    </div>
    <div class="b">
      打出
      <!--      <span class="value"> {{ userTotal["create_no"] }} </span>-->
      <span class="value"> {{ userTotal["play_cards_total"] | numFilter}} </span>
      张卡牌
    </div>

    <div class="c">
      和你最有羁绊的卡牌是
      <span class="value"> {{ userTotal["project"] }} </span><br>

    </div>

    <div class="d">
    <span v-if="userTotal['increase_tr'] >= 20 && userTotal['play_cards_total'] >= 25">
      能改造能打牌，不愧是你
      </span>
      <span v-else-if="userTotal['increase_tr'] >= 20">
        我愿称你为虔诚的改造党
      </span>
      <span v-else>
        我愿称你为熟练的拖拖党
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
