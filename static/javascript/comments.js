function insertComment(comment){
	var commentsDiv = document.getElementById("comments");
	var newCommentDiv = document.createElement("div");
	
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
	if (coment.musicfile){
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