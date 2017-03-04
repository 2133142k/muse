



function insertProjectPreviews(projectPreviews){

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
		
		projectPreviewsBlock.appendChild(previewDiv);
		
		
	}

}

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

	insertProjectPreviews(getStartingProjectPreviews());
	}
	
window.onload = onPageLoad(); 

