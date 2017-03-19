function insertComment(comment, commentsDiv){
	//alert(JSON.stringify(comment));
	//var commentsDiv = document.getElementById("comments");
	//var newCommentDiv = document.createElement("div");
	commentsDiv.innerHTML = commentsDiv.innerHTML + comment
	// commentsDiv.appendChild(newCommentDiv);
	
	// //<h3>{{CommentAuthor}}</h3>
	// var authorP = document.createElement("h3");
	// var authorText = document.createTextNode(comment.author);
	// authorP.appendChild(authorText);
	// newCommentDiv.appendChild(authorP);
	

	
	// /*{% if commentText %}
	// <p>{{CommentText}}</p>
	// {% endif %}*/
	// if (comment.commentText){
		// var commentP = document.createElement("p");
		// var commentText = document.createTextNode(comment.commentText);
		// commentP.appendChild(commentText);
		// newCommentDiv.appendChild(commentP);
	// }
	
	// /* {% if MUSICFILE %}
		// <div class="music_player">
			// <audio controls preload="metadata">
				// <source src=MUSICFILE type="audio/mpeg">
				// Music is not supported by your browser
			// </audio>
		// </div>
	// { endif %}*/
	// if (comment.musicfile){
		// var musicDiv = document.createElement("div");
		// var musicAudio = document.createElement("audio");
		// var musicSrc = document.createElement("source")
		// musicAudio.setAttribute("controls","controls");
		// musicAudio.setAttribute("preload", "metadata");
		// musicSrc.setAttribute("src", comment.musicfile);
		// musicSrc.setAttribute("type","audio/mpeg");
		// musicDiv.className = "music_player";
		// musicDiv.appendChild(musicAudio);
		// musicAudio.appendChild(musicSrc);
		// newCommentDiv.appendChild(musicDiv);
		
	// }
	
	// /*{% if commentAuthor == User or projectAuthor == User %}
		// <button type="button" onclick="removeComment({{commentId}})">
		// Remove 
		// </button>
	// {% endif %}*/
	// if (comment.canEdit){
		// var deleteButton = document.createElement("button");
		// var buttonText = document.createTextNode("Delete");
		// deleteButton.appendChild(buttonText);
		// var eventString = "javascript: deleteComment('";
		// eventString = eventString + comment.id + "')";
		// deleteButton.setAttribute("onclick", eventString);
		// newCommentDiv.appendChild(deleteButton);
		
	// }
	
}

function deleteComment(commentId){
	//confirm delete
	var confirmed = window.confirm("Are you sure you want to delete this comment?");
	if (!confirmed){return;}
	
	//request delete
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			var commentsDiv = document.getElementById("comments");

			getComments();
			
		}
	}
	xhttp.open("DELETE","comments/"+commentId+"/");
	xhttp.send();
}

function changeToHideComments(){
	//alert("change to hide");
	var showButton = document.getElementById("showComments");
	showButton.innerHTML = "Hide Comments";
	showButton.setAttribute("onclick", "javascript: hideComments();");
}

function changeToShowComments(){
	var showButton = document.getElementById("showComments");
	showButton.innerHTML = "Show Comments";
	showButton.setAttribute("onclick", "javascript: showComments();");
}

function hideComments(){
	//alert("hiding");
	document.getElementById("comments").style.display = "none";
	changeToShowComments();
}

function showComments(){
	getComments();
	changeToHideComments();
}

function displayMessage(parentElement, messageText){
	var messageDiv = document.createElement("div");
	parentElement.appendChild(messageDiv);
	//<h3>{{messageText}}</h3>
	var h3element = document.createElement("h3");
	var newText = document.createTextNode(messageText);
	h3element.appendChild(newText);
	messageDiv.appendChild(h3element);
}

function insertComments(commentsReply){
	//alert (JSON.parse(commentsReply));
	var comments = JSON.parse(commentsReply).comments;
	//alert (comments);
	//alert (comments instanceof Array);
	//alert (JSON.stringify(comments));
	var numberOfComments = comments.length;
	//alert (comments.length);
	//alert (numberOfComments);
	var commentsDiv = document.getElementById("comments");
	
	//remove all current comments
	while (commentsDiv.firstChild){
		commentsDiv.removeChild(commentsDiv.firstChild);
	}
	//check if there are new comments
	if (numberOfComments > 0){
		var i;
		for (i = 0; i < numberOfComments; i = i + 1){
			insertComment(comments[i], commentsDiv);
		}
	}
	/*else{//no comments
		displayMessage(commentsDiv, "There are no comments")
	}*/
	commentsDiv.style.display = "block";
	changeToHideComments();
	
}

function getComments(){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			//alert(this.responseText);
			insertComments(this.responseText);
		}
	}
	xhttp.open("GET","comments/",true);
	xhttp.send();
}
window.onload = getComments();