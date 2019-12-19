document.addEventListener('DOMContentLoaded' , () => {
	var socket = io.connect('http://'+document.domain+':'+location.port) ;
	let room = "Lounge" ;
	joinRoom("Lounge") ;   
	// Display Incoming Messages
	socket.on('message' , data => {
		const p = document.createElement('p') ;
		const span_username = document.createElement('span') ;  
		const span_timestamp = document.createElement('span') ; 
		const br = document.createElement('br') ; 
		if(data.username)
		{
			span_username.innerHTML = data.username ; 
			span_timestamp.innerHTML = data.time_stamp ; 
			p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML ; 
			document.querySelector('#display-message-section').append(p) ; 			
		}else{
			printSysMessage(data.msg) ; 
		}
	});
	// sending message to server 
	document.querySelector('#send_message').onclick = () => {
		socket.send({'msg':document.querySelector('#user_message').value , 
			'username':username , 'room':room }) ; 
		// clear typing area 
		document.querySelector('#user_message').value = '' ; 
		// auto focus on the input box 
		document.querySelector('#user_message').focus() ;

	}
	// room selection 
	document.querySelectorAll('.select-room').forEach(p => {
		p.onclick = () => {
			let newRoom = p.innerHTML ; 
			if( newRoom == room ){
				msg = `You are already in the ${room} Room !`
				printSysMessage(msg) ; 
			}else{
				leaveRoom(room) ; 
				joinRoom(newRoom) ; 
				room = newRoom ; 
			}
		}
	}) ; 
	// leave room 
	function leaveRoom(room){
		socket.emit('leave' , {'username': username , 'room':room }) ; 
	}
	// join room 
	function joinRoom(room){
		socket.emit('join' , {'username': username , 'room':room }) ; 
		// clear message are 
		document.querySelector('#display-message-section').innerHTML = '' ; 
		// auto focus on the input box 
		document.querySelector('#user_message').focus() ; 
	}
	// printing system messages 
	function printSysMessage(msg){
		const p = document.createElement('p') ; 
		p.innerHTML = msg ; 
		document.querySelector('#display-message-section').append(p) ; 
	}
})





