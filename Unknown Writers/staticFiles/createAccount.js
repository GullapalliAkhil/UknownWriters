function mouseover(){
  
  ele=document.getElementById("Create");
  
  ele.style.background="#3b9bf5";
  
  ele.style.color="white";
  
}

function mouseout(){
  
  ele=document.getElementById("Create");
  
  ele.style.background="transparent";
  
  ele.style.color="#3b9bf5";
  
}
function passwordfieldvalidation() {

  var name=document.getElementById("name1").value;
  var x = document.getElementById("pwd_1").value;
  var y =document.getElementById("pwd_2").value;

  if(name.length>16){

    document.getElementById("errors").innerHTML="*Username characters must be between 5 and 16.";
  
    return false;
    
    }
  if(name.length<5){
  
    document.getElementById("errors").innerHTML="*Username characters must be between 5 and 16.";
  
    return false;
    
    }
  
  
  if (x == "") {
    document.getElementById("errors").innerHTML="   *Password field cannot be NULL.";

		return false;
   }
  if(y == ""){
    document.getElementById("errors").innerHTML="*Confirm Password field cannot be NULL.";

		return false;
  
   }
if(x !=y){

  document.getElementById("errors").innerHTML="*Password and Confirm Password fields must match.";

  return false;
  
   }
if(x>14){

  document.getElementById("errors").innerHTML="*Password characters must be between 5 and 14.";

  return false;
  
  }
if(x<5){

  document.getElementById("errors").innerHTML="*Password characters must be between 5 and 14.";

  return false;
  
  }

}

