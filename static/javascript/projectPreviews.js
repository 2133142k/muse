



function insertProjectPreviews(inputDict){

	var isLoggedIn = inputDict.SignedIn;
	var projectPreviews = inputDict.ProjectPreviews;
	var numberOfPreviews = projectPreviews.length;
	var projectPreviewsBlock = document.getElementById("projectPreviews");
	var i;

	for (i = 0; i < numberOfPreviews; i = i + 1){
		
		projectPreview = projectPreviews[i];
		addProjectPreview(projectPreview, projectPreviewsBlock, isLoggedIn);
	}

}

function addProjectPreview(projectPreview, parentDiv, isLoggedIn){
	
	var tempElement;
	var tempText;
	var previewDiv = document.createElement("div");
	previewDiv.className ="projectPreview";
	previewDiv.id ="projectReview"+projectPreview.nameSlug;
	
	tempElement = document.createElement("h3");
	tempText = document.createTextNode(projectPreview.ProjectName);
	tempElement.appendChild(tempText);
	previewDiv.appendChild(tempElement);
	
	tempElement = document.createElement("p");
	tempText = document.createTextNode(projectPreview.ProjectAuthor);
	tempElement.appendChild(tempText);
	previewDiv.appendChild(tempElement);
	
	tempElement = document.createElement("p");
	tempText = document.createTextNode(projectPreview.ProjectGenre);
	tempElement.appendChild(tempText);
	previewDiv.appendChild(tempElement);
	
	tempElement = document.createElement("p");
	tempText = document.createTextNode("Comments - " + projectPreview.NumberOfComments);
	tempElement.appendChild(tempText);
	previewDiv.appendChild(tempElement);
	
	tempElement = document.createElement("p");
	tempText = document.createTextNode(projectPreview.ProjectDescription);
	tempElement.appendChild(tempText);
	previewDiv.appendChild(tempElement);
	
	addProjectPreviewAccessButtons(previewDiv, isLoggedIn, projectPreview.canEdit, projectPreview.nameSlug);
	parentDiv.appendChild(previewDiv);
}

function addProjectPreviewAccessButtons(previewDiv, isLoggedIn, canEdit, slug){
	var tempElement;
	var tempText;
	var divBlock = document.createElement("div");
	divBlock.className = "projectPreviewAccessButtons";
	previewDiv.appendChild(divBlock);
	if(isLoggedIn){
		
		//View button
		tempElement = document.createElement("button");
		tempText = document.createTextNode("View");
		tempElement.appendChild(tempText);
		tempElement.setAttribute("onclick", "javascript: location.assign('/muse/projects/"+ slug + "'");//link to projectPage
		divBlock.appendChild(tempElement);
		
		if (canEdit){
			
			//Edit button
			//tempElement = document.createElement("button");
			//tempText = document.createTextNode("Edit");
			//tempElement.appendChild(tempText);
			//add edit event!!! Should either be link to edit page or load in the project and display with edit controls
			//divBlock.appendChild(tempElement);
			
			//Delete button
			tempElement = document.createElement("button");
			tempText = document.createTextNode("Delete");
			tempElement.appendChild(tempText);
			tempElement.setAttribute("onclick", "javascript: deleteProject(" + projectSlug + ")");
			
			//add delete event!!! Should ask if user wants to delete then request server to delete
			divBlock.appendChild(tempElement);
		}
		
	}
	else{
	//LoginToView button
	tempElement = document.createElement("button");
	tempText = document.createTextNode("Log In To View");
	tempElement.appendChild(tempText);
	//add login event!!! Should either link to login page or ask user to login
	divBlock.appendChild(tempElement);
	}
}

function deleteProject(projectSlug){
	//confirm delete
	var confirmed = window.confirm("Are you sure you want to delete this project?");
	if (!confirmed){return;}
	
	//request delete
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			var deleted = document.getElementById("projectPreview" + projectSlug);
			deleted.parentNode.removeChild(deleted);
		}
	}
	xhttp.open("DELETE","/muse/projects/"+projectSlug+"/");
	xhttp.send();
}

//functionChangeLoggedIn

function getStartingProjectPreviews(number){
	//change to request from server
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			//alert(this.responseText);
			insertProjectPreviews(JSON.parse(this.responseText));
		}
	}
	xhttp.open("GET","/muse/projects/?owned=true&number=" + number,true);
	xhttp.send();
}

function onPageLoad(isLoggedIn, username, projectAuthor){
	
	var number = 5;
	getStartingProjectPreviews(number);
	}
	
window.onload = onPageLoad(); 

