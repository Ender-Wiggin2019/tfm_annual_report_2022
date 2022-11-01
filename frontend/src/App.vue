<template>
	<router-view/>
</template>

<style>
.value {
  display: inline-block;
  padding: 5px;
  /*transform: scaleY(1.1) translateY(-5.2%);*/
  font-weight: bolder;
  color: #ffed7b;
}
    .front-page{
		background-image: linear-gradient(#ff7853, #ffd287);
	}

    .second{
		flex: 3;
    background-image: linear-gradient(#ff7853, #ffd287);
		border-top-left-radius: 17px;
		border-bottom-left-radius: 17px;
	}

	.form-section{
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0 4rem;
        height: 100%;
    }

    .form-title{
        flex: 1;
    }

    .form-title p{
        margin-bottom: 0;
    }

    .form-title--heading{
        font-size: 2rem;
        font-weight: 700;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

	.btn--primary{
        display: inline-block;
        color: #f7f7f7;
        background-color: #ff7853;
        border: 0;
        padding: .8rem 2rem;
        border-radius: 17px;
        box-sizing: border-box;
        transition: all .25s ease;
        outline: none;
        appearance: none;
        box-shadow: 0 10px 20px -10px rgb(246, 128, 92);
    }

    .btn--primary:hover,
    .btn--primary:focus{
        outline: none;
        box-shadow: 0px 20px 20px -10px rgb(239, 136, 102);
        transform: translateY(-5px);
    }

    .goto-signup,
    .goto-login{
        flex: 1;
        text-align: right;
        color: #aaa;
        outline: none;
        margin: 0;
    }

    .goto-signup a,
    .goto-login a{
        text-decoration: none;
    }

    @keyframes rotateLoader {
        0%{
            transform: rotate(0deg);
        }
        100%{
            transform: rotate(360deg);
        }
    }
@keyframes delay-display {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@keyframes slide-top {
  0% {
    opacity: 0;
    transform: translateY(10vh);
  }
  100% {
    opacity: 1;
    transform: translateY(0vh);
  }
}

    .alert-danger{
        box-shadow: 0px 20px 20px -10px rgba(245, 101, 101, .5);
    }

    .alert-success{
        box-shadow: 0px 20px 20px -10px rgba(72,187,120, .5);
    }
</style>
