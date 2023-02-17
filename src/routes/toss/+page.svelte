<svelte:head>
	<meta name="description" content="How to play Sverdle" />
</svelte:head>


<div class="text-column">
	<div class="form">
		<form action="http://localhost:5001/toss:api" method="post">
			<input type="text" name="amount" placeholder="입금액" />
			<input type="text" id="name" name="name" placeholder="입금자명">
			<input type="text" id="ingame" name="ingame" placeholder="인게임 이름">
			<button type="submit">충전하기</button>
		</form>			   
	</div>
</div>
<link href='//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSans-kr.css' rel='stylesheet' type='text/css'>
<style>
@import url(//spoqa.github.io/spoqa-han-sans/css/SpoqaHanSans-kr.css);
*{ font-family: 'Spoqa Han Sans', 'Spoqa Han Sans JP', 'Sans-serif'; }
* {
  box-sizing: border-box;
}
.form {
  background-color: #ffffff;
  width: 500px;
  margin: 50px auto 10px auto;
  padding: 30px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 10px -3px #333;
  text-align: center;
}

input {
  border-radius: 100px;
  padding: 10px 15px;
  width: 50%;
  border: 1px solid #D9D9D9;
  outline: none;
  display: block;
  margin: 20px auto 20px auto;
}

button {
  border-radius: 100px;
  border: none;
  background: #719BE6;
  width: 50%;
  padding: 10px;
  color: #FFFFFF;
  margin-top: 25px;
  box-shadow: 0 2px 10px -3px #719BE6;
  display: block;
  margin: 55px auto 10px auto;
}

</style>
