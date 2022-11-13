<template>
  <div class="parent">
    <div class="a">
      你今年的雷达图如下:
      <!--      <span class="value"> {{ maxMonth[0] }} </span>点聊天 说的话 有<span-->
      <!--        class="value"-->
      <!--      >-->
      <!--        {{ maxMonth[1] }} </span-->
      <!--      >条-->
    </div>
    <div ref="chart" class="chart"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import { hourGroup } from "@/data.json";
import {getAPI} from "@/axios.api";
export default {
  data() {
    return {
      myChart: undefined,
      arr: hourGroup,
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
      'name': (this.$store.state.name).toLowerCase(),
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
  },
  mounted() {
    this.myChart = echarts.init(this.$refs.chart);
    this.myChart.setOption({
          color: '#dc7251',
          tooltip : {
            trigger: 'axis'
          },

          toolbox: {
            show : true,
            feature : {
              mark : {show: true},
              dataView : {show: true, readOnly: false},
              restore : {show: true},
              saveAsImage : {show: true}
            }
          },
          polar : [
            {
              indicator : [
                { text: '胜率', max: 1, color: 'white'},
                { text: '改造', max: 25, color: 'white'},
                { text: '打牌', max: 35, color: 'white'},
                { text: '拖拖', max: 1, color: 'white'},
                { text: '分数', max: 1, color: 'white'},
                { text: '勤奋', max: 100, color: 'white'},
              ],
              axisName: {
                color: '#f3d2a6',
                // backgroundColor: '#666',
                // borderRadius: 3,
                // padding: [3, 5],
                fontSize: 25,
              },
              splitLine : {
                show : true,
                lineStyle : {
                  width : 1,
                  color : ['#ffcfaa']
                  // 图表背景网格线的颜色
                }
              }
            }
          ],
          calculable : true,

          series : [
            {
              name: '',
              type: 'radar',
              data : [
                {
                  value : [Math.max(this.$store.state.userTotal["bayesPerc"], this.$store.state.userTotal["bayesPerc_2p"]), Math.min(25, this.$store.state.userTotal["increase_tr"]), Math.min(35, this.$store.state.userTotal["play_cards_total"]), Math.min(1, Math.max(this.$store.state.userTotal["gen_rank"], this.$store.state.userTotal["gen_rank_2p"]) / 100), Math.min(1, (1000 - Math.max(this.$store.state.userTotal["playerScore_rank"], this.$store.state.userTotal["playerScore_rank_2p"])) / 1000), Math.min(100, this.$store.state.userTotal["total"])],
                  name : ''
                }
              ],
              // itemStyle: {
              //   color: 'white',
              // }, // 修改indicator颜色
              areaStyle: {   // 阴影部分设置
                color: '#f67e57',
                opacity: 0.5
                // color: new echarts.graphic.RadialGradient(0.1, 0.6, 1, [
                //   {
                //     color: 'rgba(255, 145, 124, 0.1)',
                //     offset: 0
                //   },
                //   {
                //     color: 'rgba(255, 145, 124, 0.9)',
                //     offset: 1
                //   }
                // ])
              }
            }
          ]
        }
    );
  },
};
</script>

<style scoped>
.parent{position:relative;}
.chart {
  width: 100vw;
  height: 50vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: 1s;
  animation-fill-mode: backwards;
  /* position:relative;left:20%;-webkit-transform:translateX(-50%);transform:translateX(-50%); */
  /*position:absolute;left:50%;width:150px;margin-left:-75px;*/
}

.a {
  text-align: center;
  color: white;
  font-size: 5vw;
  padding-top: 10vh;
  animation-name: slide-top;
  animation-duration: 1s;
  animation-delay: .5s;
  animation-fill-mode: backwards;
}
/*.a {*/
/*  padding-top: 15vh;*/
/*  animation-name: slide-top;*/
/*  animation-duration: 1s;*/
/*  animation-delay: 0.5s;*/
/*  animation-fill-mode: backwards;*/
/*}*/
</style>
