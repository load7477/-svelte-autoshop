<svelte:head>
	<meta name="description" content="How to play Sverdle" />
</svelte:head>

<div class="text-column">
	<div class="form">
		<form action="/login_check">
			<input type="email" name="email" placeholder="Email" />
			<input type="password" name="Password" placeholder="Password" />
			<button type="submit">로그인</button>
			<a href="/register">회원가입</a>
		</form>			   
	</div>
</div>

<style>
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

a {
  text-align: center;
  margin-top: 30px;
  color: #719BE6;
  text-decoration: none;
  padding: 5px;
  display: inline-block;
}

a:hover {
  text-decoration: underline;
}

</style>
