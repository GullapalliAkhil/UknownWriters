function mouseover(){
  
  ele=document.getElementById("Signup1");
  
  ele.style.background="#3b9bf5";
  
  ele.style.color="white";
  
}

function mouseout(){
  
  ele=document.getElementById("Signup1");
  
  ele.style.background="transparent";
  
  ele.style.color="#3b9bf5";
  
}

function Validation(){

	if(document.Loginform.username.value == ""){

		document.getElementById("errors").innerHTML="*Username field cannot be NULL.";

		return false;
	}
	if(document.Loginform.Password.value == ""){

		document.getElementById("errors").innerHTML="*Password field cannot be NULL.";

		return false;
	}
	
	

}