function removeAccount(userId){
	var accepted = window.confirm("Are you sure you want to delete your account?");
	alert(accepted);
	if (accepted == true) {
		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function(){
		alert(this.responseText);
		if (this.readyState == 4 && this.status == 200){
			alert(this.responseText);
			window.alert("Account deleted");
			var homeUrl = "/muse/";
			window.location.href = homeUrl;
		}
		else{
			alert("Delete failed");
		}
	}
		xhttp.open("POST","/muse/users/"+userId+"/delete/",true);
		alert("sending request");
		xhttp.send();

}
}

function changePassword(accountId){
	window.alert("Add In Password Change Bit");
}

function newProject(){
	//window.alert("Link to new project form");
	window.location.assign("/muse/new_project/")
}