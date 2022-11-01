<template>
    <div class="front-page flex h-screen">
<!--  <div class="mainApp">-->
<!--        <Hero />-->
		<section class="second">
            <div class="p-6 form-section">
                <section class="form-title">
<!--                    <p class="form-title&#45;&#45;pre text-gray-600">Welcome</p>-->
<!--                    <p class="form-title&#45;&#45;heading"><span>Login to</span><span>Assignment Portal</span></p>-->
                </section>

                <section class="form-login mt-6c">
                    <form v-on:submit.prevent="login" class="login-form">
                        <p v-if="incorrectAuth" class="bg-red-500 text-red-900 rounded-xl py-2 px-4 mb-6 alert-danger" style="width: 400px"><i class="fas fa-exclamation-triangle mr-2"></i>Invalid name or password</p>
                        <div class="form-component">
                            <input type="text" name="name" v-model="name" class="input-field" autocomplete="off" required>
                            <span class="label-placeholder">User Name</span>
                        </div>

                        <div class="form-component">
                            <input type="password" name="password" v-model="password" class="input-field" autocomplete="off" required>
                            <span class="label-placeholder">Password</span>
                        </div>

                        <div class="form-bottom flex items-center justify-between">
                            <button type="submit" class="btn--primary" id="loginBtn">Login</button>
<!--                            <div class="goto-signup">账号不符?-->
<!--                                <router-link to="/register" exact class="text-blue-600">注册</router-link>-->
<!--                            </div>-->
                        </div>
                    </form>
                </section>
            </div>
		</section>
	</div>
</template>

<script>
    import Hero from '@/components/Hero.vue';

    export default {
        name: "Login",
        components: {
            Hero
        },
        data() {
            return{
                name: '',
                password: '',
                incorrectAuth: false
            }
        },
        methods: {
            login(){
                const loginBtn = document.querySelector('#loginBtn');
                loginBtn.innerHTML = '<i class="fas fa-circle-notch load-icon"></i> <span class="ml-2">Logging In<span>';

                this.$store.dispatch('userLogin', {
                    name: this.name,
                    password: this.password
                })
                .then(() => {
                    this.$router.push({ name: 'Home' });
                    loginBtn.innerHTML = 'Logged In';
                })
                .catch(err => {
                    console.log(err);
                    this.incorrectAuth = true;
                    loginBtn.innerHTML = 'Login';
                })
            }
        }
    }
</script>

<style scoped>

.mainApp {
  background-image: linear-gradient(#ff7853, #ffd287);
  height: 100vh;
  overflow: hidden;
  font-family: "Microsoft YaHei", 微软雅黑, "Microsoft JhengHei", 华文细黑,
  STHeiti, MingLiu;
  font-size: 4vw;
}
    .form-login{
        flex: 2;
        padding: 1rem 2rem;
    }

    .form-component{
        width: 200px;
        height: 50px;
        position: relative;
        margin-bottom: 1.5rem;
    }

    .label-placeholder{
        pointer-events: none;
        position: absolute;
        top: 12px;
        left: 20px;
        transition: 0.2s ease all;
    }

    .input-field{
        width: 200px;
        height: 50px;
        background: #Ffffff;
        border: 0;
        border-radius: 17px;
        padding: 0em 1rem;
        outline: none;
    }

    input:focus ~ .label-placeholder,
    input:not(:focus):valid ~ .label-placeholder{
        top: -18px;
        font-size: 12px;
    }

    .form-bottom{
        width: 400px;
    }

    .load-icon{
        margin-right: .5rem;
        animation: rotateLoader 1s infinite;
    }
</style>
