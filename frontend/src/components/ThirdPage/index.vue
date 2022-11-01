<template>
  <div>
    <div class="a">
      今年你一共参与火星建设
<!--      <span class="value"> {{ userTotal["create_no"] }} </span>-->
      <span class="value"> {{ userTotal["days"] }} </span>
      天
    </div>
    <div class="b">
      累计进行了
      <!--      <span class="value"> {{ userTotal["create_no"] }} </span>-->
      <span class="value"> {{ userTotal["total"] }} </span>
      局游戏
    </div>

    <div class="c">
    <span v-if="userTotal['total'] >= 60">
      改造委员会当场留下了感动的泪水！
      </span>
    <span v-else-if="userTotal['total'] >= 10">
        平时生活也很忙碌吧！但火星一直都在哟
      </span>
    <span v-else>
        火星有点寂寞了，下次记得多陪陪人家~
      </span>
    </div>
    <div class="d">
      你最喜欢的模式是
      <span class="value"> {{ userTotal["fav"] }}P </span><br>

      <span v-if="userTotal['fav'] === '2P'">
      看来你更喜欢二人世界的甜蜜岁月
      </span>
      <span v-else>
        看来你更喜欢风云莫测的多人运动
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
