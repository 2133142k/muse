function removeAccount(accountId){
	var accepted = window.confirm("Are you sure you want to delete your account?");
	if (accepted == true) {
		var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			//alert(this.responseText);
			window.alert("Account deleted");
			var homeUrl = "/muse/";
			window.location.href = homeUrl;
		}
		
		//What to use to delete?
		//xhttp.open("GET","/muse/accounts/{{accountNo}}/delete/",true);
		//xhttp.send();
	}
}
}

function changePassword(accountId){
	window.alert("Add In Password Change Bit");
}

function newProject(){
	//window.alert("Link to new project form");
	window.location.assign("/muse/new_project/")
}