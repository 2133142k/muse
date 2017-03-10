



function insertProjectPreviews(projectPreviews, isLoggedIn, canEdit){

	var numberOfPreviews = projectPreviews.projectPreviews.length;
	var newPreviewsHTML = "";
	var projectPreviewsBlock = document.getElementById("projectPreviews");
	var previewDiv;
	var tempElement;
	var tempText;
	var i;

	for (i = 0; i < numberOfPreviews; i = i + 1){
		
		projectPreview = projectPreviews.projectPreviews[i];
		
		previewDiv = document.createElement("div");
		previewDiv.className ="projectPreview";
		
		
		
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
		
		addProjectPreviewAccessButtons(previewDiv, isLoggedIn, canEdit);
		projectPreviewsBlock.appendChild(previewDiv);
		
		
	}

}

function addProjectPreviewAccessButtons(previewDiv, isLoggedIn, canEdit){
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
		//add view event!!! Should either be link to view page or load in the project and display
		divBlock.appendChild(tempElement);
		
		if (canEdit){
			
			//Edit button
			tempElement = document.createElement("button");
			tempText = document.createTextNode("Edit");
			tempElement.appendChild(tempText);
			//add edit event!!! Should either be link to edit page or load in the project and display with edit controls
			divBlock.appendChild(tempElement);
			
			//Delete button
			tempElement = document.createElement("button");
			tempText = document.createTextNode("Delete");
			tempElement.appendChild(tempText);
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

//functionChangeLoggedIn

function getStartingProjectPreviews(){
	var projectPreviews = '{"projectPreviews":[{"ProjectName":"13 bar blues",' +
                                        '"ProjectAuthor":"UnluckyCoolCat24",' +
                                        '"ProjectGenre":"Blues",' +
                                        '"NumberOfComments":"2",' +
	'"ProjectDescription":"Like the 12 bar blues but with an added bar!"}]}';
	projectPreviews = JSON.parse(projectPreviews);

	return projectPreviews;
}

function onPageLoad(){

	insertProjectPreviews(getStartingProjectPreviews(), false, false);
	}
	
window.onload = onPageLoad(); 

