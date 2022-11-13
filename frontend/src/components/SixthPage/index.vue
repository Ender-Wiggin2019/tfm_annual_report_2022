<template>
  <div>
    <div class="a">
      今年陪伴你时间最长的玩家是
      <!--      <span class="value"> {{ userTotal["create_no"] }} </span>-->
      <span class="value"> {{ userTotal["opp"] }} </span>
    </div>
    <div class="b">
      一共陪伴了你
      <!--      <span class="value"> {{ userTotal["create_no"] }} </span>-->
      <span class="value"> {{ userTotal["total_opp"] }} </span>
      局游戏
    </div>

    <div class="c">
      你对阵TA的胜率是
      <span class="value"> {{ winRate }} % </span><br>

    </div>

    <div class="d">
    <span v-if="winRate >= 65">
      下次对TA温柔点，好吗
      </span>
      <span v-else-if="winRate < 35">
        下次让TA对你温柔点，好吗
      </span>
      <span v-else>
        你们旗鼓相当，势均力敌
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
    },
    winRate(){
      return (this.$store.state.userTotal["isWin"] * 100).toFixed(2)
    }

  },

  created() {
    const userData = {
      'name': (this.$store.state.name).toLowerCase(),
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
  padding-top: 10vh;
  font-size: 5vw;

  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2s;
  animation-fill-mode: backwards;
}
.d {
  font-size: 5vw;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 2.5s;
  animation-fill-mode: backwards;
}

</style>
