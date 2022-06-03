//if the page was accesses via a back or forward, reload page
navigation = performance.getEntriesByType("navigation")
if(navigation[0].type == "back_forward"){
    location.reload();
}

//creates the websocket and receives messages
let moves = JSON.parse(document.getElementById('moves').textContent);
let moveArray = []
let available_move_list = JSON.parse(document.getElementById('available_move_list').textContent);
const gameId = JSON.parse(document.getElementById('game-id').textContent);
const username = JSON.parse(document.getElementById('username').textContent);
const winner = JSON.parse(document.getElementById('winnerUN').textContent);

oAudio= new Audio("https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-31172/zapsplat_office_chalk_stick_thick_draw_circle_on_small_chalk_board_001_34597.mp3");

xAudio1 = new Audio("https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-31172/zapsplat_office_chalk_stick_thick_draw_line_on_small_chalk_board_002_34604.mp3");

xAudio2 = new Audio("https://www.zapsplat.com/wp-content/uploads/2015/sound-effects-31172/zapsplat_office_chalk_stick_thick_draw_line_on_small_chalk_board_003_34605.mp3");


const ws = new WebSocket('ws://'
                        + window.location.host
                        + '/ws/tictactoe/'
                        + gameId
                        + '/')


document.querySelector('.TTTtitle').append(' - ' + gameId);

ws.onmessage = function(e) {

    const data = JSON.parse(e.data);
    
    if(data.move){
        moves = incrementMoves(moves, data.move)
        loadMoves(moves)
    }
    if(data.available_move_list){
        available_move_list = data.available_move_list
    }

    if(data.player == 1){
        document.querySelector(".player1").innerHTML = ("Player 1 (O) - " + data.username);
    }
    else if(data.player == 2){
        document.querySelector(".player2").innerHTML = ("Player 2 (X) - " + data.username);
    }

    for(let c=0; c < 3; c++) {
        for(let r=0; r < 3; r++) {
            if (available_move_list.includes(c.toString() + r.toString())) {
                const block = document.getElementById(c.toString() + r.toString())
                block.addEventListener("click", addX)
                block.r = c
                block.c = r
            }
        }
    }
    if(typeof data.turn === 'boolean' && data.turn === false){
        for(let c=0; c < 3; c++) {
            for(let r=0; r < 3; r++) {
                console.log("REMOVE IS BEING CALLED")
                document.getElementById(c.toString() + r.toString()).removeEventListener("click", addX)
            }
        }
    }
    if(typeof data.winner === 'string'){
        for(let c=0; c < 3; c++) {
            for(let r=0; r < 3; r++) {
                document.getElementById(c.toString() + r.toString()).removeEventListener("click", addX)
            }
        }

        //disply result data
        if(data.winner == username){
            document.querySelector(".result").innerHTML = ("Victory!")
            document.querySelector(".result").style.color = "rgb(50, 168, 82)"
            ws.close()
        }else{
            document.querySelector(".result").innerHTML = ("Defeat")
            document.querySelector(".result").style.color = "rgb(209, 85, 85)"
            ws.close()
        }
    }
    if(typeof data.winner === 'number'){
        console.log("The data is 0")
        document.querySelector(".draw").innerHTML = ("Draw")
        ws.close()
    }

    
}

//creates the board
boardContainer = document.querySelector('.TTTboardDiv')
let htmlUpdate = "";

for(let c=0; c < 3; c++) {
    htmlUpdate += '<div class="TTTcolumn">'
    for(let r=0; r < 3; r++) {
        htmlUpdate += '<div class="TTTbox" id="' + r + c + '"></div>'
    }
    htmlUpdate += '</div>'
}
boardContainer.innerHTML = htmlUpdate;
loadMoves(moves)

//This will display x or o on click
function addX(event) {
    let realR = event.currentTarget.r.toString()
    let realC = event.currentTarget.c.toString()
    let id = realR + realC
    
    moves = incrementMoves(moves, id)
    loadMoves(moves)

    ws.send(JSON.stringify({
        'move': id 
    }))

    for(let c=0; c < 3; c++) {
        for(let r=0; r < 3; r++) {
            console.log("REMOVE IS BEING CALLED")
            document.getElementById(c.toString() + r.toString()).removeEventListener("click", addX)
        }
    }
}

function loadMoves(moves){//Loops through array of moves to draw O or X
    if(moves){
        let moveArray = moves.split(',')
        oAudio.play()
        for(const [index, move] of moveArray.entries()){
            let c = move[1]
            let r = move[0]
            let id = r + "" + c

            if(index%2 == 0){
                document.getElementById(id).innerHTML = 
                `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 380.734 380.734" style="enable-background:new 0 0 380.734 380.734;" xml:space="preserve">
                <path style="fill:#010002;" d="M190.367,0C85.23,0,0,85.23,0,190.367s85.23,190.367,190.367,190.367s190.367-85.23,190.367-190.367   S295.504,0,190.367,0z M299.002,298.36c-28.996,28.996-67.57,44.959-108.634,44.959S110.723,327.35,81.733,298.36   c-28.865-28.876-44.769-67.227-44.769-107.993c0-40.771,15.904-79.128,44.769-107.993c28.99-28.996,67.57-44.959,108.634-44.959   c41.054,0,79.639,15.969,108.629,44.959c28.871,28.865,44.763,67.221,44.763,107.993   C343.765,231.133,327.867,269.489,299.002,298.36z"/>
                </svg>`; // O
            }else{
                document.getElementById(id).innerHTML = 
                `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 460.775 460.775" style="enable-background:new 0 0 460.775 460.775;" xml:space="preserve">
                <path
                style ="fill:rgb(255, 255, 255, .40)" 
                d="M285.08,230.397L456.218,59.27c6.076-6.077,6.076-15.911,0-21.986L423.511,4.565c-2.913-2.911-6.866-4.55-10.992-4.55  c-4.127,0-8.08,1.639-10.993,4.55l-171.138,171.14L59.25,4.565c-2.913-2.911-6.866-4.55-10.993-4.55  c-4.126,0-8.08,1.639-10.992,4.55L4.558,37.284c-6.077,6.075-6.077,15.909,0,21.986l171.138,171.128L4.575,401.505  c-6.074,6.077-6.074,15.911,0,21.986l32.709,32.719c2.911,2.911,6.865,4.55,10.992,4.55c4.127,0,8.08-1.639,10.994-4.55  l171.117-171.12l171.118,171.12c2.913,2.911,6.866,4.55,10.993,4.55c4.128,0,8.081-1.639,10.992-4.55l32.709-32.719  c6.074-6.075,6.074-15.909,0-21.986L285.08,230.397z"/>
                </svg>`;// X
                
            }
        }
    }
}

function incrementMoves(moves, move){//checks whether moves is null then returns the moves with the added move
    if(moves == null){
        moves = move
    }else{
        moves = moves + "," + move
    }
    return moves
}

ws.onclose = function (e){
    console.log("connection closed");
};