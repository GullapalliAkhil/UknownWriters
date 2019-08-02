function mouseover() {

	ele = document.getElementById("Signup1");

	ele.style.background = "#3b9bf5";

	ele.style.color = "white";

}

function mouseout() {

	ele = document.getElementById("Signup1");

	ele.style.background = "transparent";

	ele.style.color = "#3b9bf5";

}

function sessionstorage() {

	var name = "Akhil Gullapalli";

	sessionStorage.setItem("username", name);


}






