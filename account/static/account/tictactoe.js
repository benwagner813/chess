//creates the websocket and receives messages

const moves = JSON.parse(document.getElementById('moves').textContent);
const OG_available_move_list = JSON.parse(document.getElementById('available_move_list').textContent);
const gameId = JSON.parse(document.getElementById('game-id').textContent);

const ws = new WebSocket('ws://'
                        + window.location.host
                        + '/ws/tictactoe/'
                        + gameId
                        + '/')

console.log('Hello ' + gameId)

document.querySelector('.TTTtitle').append(' - ' + gameId);

ws.onopen = function(e) {
    console.log(OG_available_move_list)
    //TODO - CONTINUE WORKING ON "ONOPEN" FUNCTION
}

ws.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if(data.player == 1){
        document.querySelector(".player1").innerHTML = ("Player 1 - " + data.username);
    }
    else if(data.player == 2){
        document.querySelector(".player2").innerHTML = ("Player 2 - " + data.username);
    }

    const available_move_list = data.available_move_list

    console.log(data)

    console.log(available_move_list)
    console.log("Type of available_move_list = " + typeof available_move_list)

    for(let i=0; i < 3; i++) {
        for(let j=0; j < 3; j++) {
            if (available_move_list.includes(i.toString() + j.toString())) {
                var clickable = document.getElementById(i.toString() + j.toString()).onclick = "addX(" + i.toString() + "," + i.toString() + ")"
            }
        }
    }
}


//creates the board and adds onclick function to each square
boardContainer = document.querySelector('.TTTboardDiv')
let htmlUpdate = "";

for(let i=0; i < 3; i++) {
    htmlUpdate += '<div class="TTTcolumn">'
    for(let j=0; j < 3; j++) {
        htmlUpdate += '<div class="TTTbox" id="' + i + j + '"></div>'
    }
    htmlUpdate += '</div>'
}
boardContainer.innerHTML = htmlUpdate;

//This will display x or o on click
function addX(x, y) {
    let id = x.toString() + y.toString()
    console.log(id);
    document.getElementById(id).innerHTML = 
    `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 460.775 460.775" style="enable-background:new 0 0 460.775 460.775;" xml:space="preserve">
        <path
        style ="fill:rgb(255, 255, 255, .40)" 
        d="M285.08,230.397L456.218,59.27c6.076-6.077,6.076-15.911,0-21.986L423.511,4.565c-2.913-2.911-6.866-4.55-10.992-4.55  c-4.127,0-8.08,1.639-10.993,4.55l-171.138,171.14L59.25,4.565c-2.913-2.911-6.866-4.55-10.993-4.55  c-4.126,0-8.08,1.639-10.992,4.55L4.558,37.284c-6.077,6.075-6.077,15.909,0,21.986l171.138,171.128L4.575,401.505  c-6.074,6.077-6.074,15.911,0,21.986l32.709,32.719c2.911,2.911,6.865,4.55,10.992,4.55c4.127,0,8.08-1.639,10.994-4.55  l171.117-171.12l171.118,171.12c2.913,2.911,6.866,4.55,10.993,4.55c4.128,0,8.081-1.639,10.992-4.55l32.709-32.719  c6.074-6.075,6.074-15.909,0-21.986L285.08,230.397z"/>
     </svg>`;
    
    ws.send(JSON.stringify({
        'move': id 
    }))

    /* O SVG 
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Capa_1" x="0px" y="0px" viewBox="0 0 380.734 380.734" style="enable-background:new 0 0 380.734 380.734;" xml:space="preserve">
        <path style="fill:#010002;" d="M190.367,0C85.23,0,0,85.23,0,190.367s85.23,190.367,190.367,190.367s190.367-85.23,190.367-190.367   S295.504,0,190.367,0z M299.002,298.36c-28.996,28.996-67.57,44.959-108.634,44.959S110.723,327.35,81.733,298.36   c-28.865-28.876-44.769-67.227-44.769-107.993c0-40.771,15.904-79.128,44.769-107.993c28.99-28.996,67.57-44.959,108.634-44.959   c41.054,0,79.639,15.969,108.629,44.959c28.871,28.865,44.763,67.221,44.763,107.993   C343.765,231.133,327.867,269.489,299.002,298.36z"/>
    </svg>
    */
}