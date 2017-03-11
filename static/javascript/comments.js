function insertComment(comment){
	var commentsDiv = document.getElementById("comments");
	var newCommentDiv = document.createElement("div");
	commentsDiv.appendChild(newCommentDiv);
	
	//<h3>{{CommentAuthor}}</h3>
	var authorP = document.createElement("h3");
	var authorText = document.createTextNode(comment.author);
	authorP.appendChild(authorText);
	newCommentDiv.appendChild(authorP);
	
	/* {% if MUSICFILE %}
		<div class="music_player">
			<audio controls preload="metadata">
				<source src=MUSICFILE type="audio/mpeg">
				Music is not supported by your browser
			</audio>
		</div>
	{ endif %}*/
	if (comment.musicfile){
		var musicDiv = document.createElement("div");
		var musicAudio = document.createElement("audio");
		var musicSrc = document.createElement("source")
		musicAudio.setAttribute("controls");
		musicAudio.setAttribute("preload", "metadata");
		musicSrc.setAttribute("src", musicfile.textContent);
		musicSrc.setAttribute("type","audio/mpeg");
		musicDiv.className = "music_player";
		musicDiv.appendChild(musicAudio);
		musicAudio.appendChild(musicSrc);
		newCommentDiv.appendChild(musicDiv);
		
	}
	
	/*{% if commentText %}
	<p>{{CommentText}}</p>
	{% endif %}*/
	if (comment.commentText){
		var commentP = document.createElement("p");
		var commentText = document.createTextNode(comment.commentText);
		commentP.appendChild(commentText);
		newCommentDiv.appendChild(commentP);
	}
	
	/*{% if commentAuthor == User or projectAuthor == User %}
		<button type="button" onclick="removeComment({{commentId}})">
		Remove 
		</button>
	{% endif %}*/
	
}

function insertComments(commentsReply){
	var comments = JSON.parse(commentsReply).comments
	var numberOfComments = comments.length;
	var i;
	for (i = 0; i < numberOfComments; i = i + 1){
		insertComment(comments[i]);
	}
	
}

function getComments(){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function(){
		if (this.readyState == 4 && this.status == 200){
			alert(this.responseText);
			insertComments(this.responseText);
		}
	}
	xhttp.open("GET","/muse/testProjectViewPage/comments/",true);
	xhttp.send();
}