//creates the websocket and receives messages
const gameId = JSON.parse(document.getElementById('game-id').textContent);
const epd = JSON.parse(document.getElementById('epd').textContent);
var available_moves = JSON.parse(document.getElementById('available_moves').textContent);
displayedMoves = []

const squareMap = {
    "h" : "7",
    "g" : "6",
    "f" : "5",
    "e" : "4",
    "d" : "3",
    "c" : "2",
    "b" : "1",
    "a" : "0",
    "8" : "0",
    "7" : "1",
    "6" : "2",
    "5" : "3",
    "4" : "4",
    "3" : "5",
    "2" : "6",
    "1" : "7",
}
const letterMap = {
    "7" : "h",
    "6" : "g",
    "5" : "f",
    "4" : "e",
    "3" : "d",
    "2" : "c",
    "1" : "b",
    "0" : "a",
}
const numberMap = {
    "7" : "1",
    "6" : "2",
    "5" : "3",
    "4" : "4",
    "3" : "5",
    "2" : "6",
    "1" : "7",
    "0" : "8",
}

console.log(available_moves)
document.querySelector(".test").innerHTML = epd

//place pieces on board according to epd
let epdArray = epd.split(' ')
let epdBoard = epdArray[0]
console.log(epdBoard)

const ws = new WebSocket('ws://'
                        + window.location.host
                        + '/ws/chess/'
                        + gameId
                        + '/')

//creates the chess board
boardContainer = document.querySelector(".ChessBoardDiv")
//to do: Create check for player color to determine the default perspective
let perspective = 1;
createBoard();
swapLabels();

let whiteKing = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
<title>King</title>
<description>
Western white-side King
</description>

<g transform="matrix(1.4373857,0,0,1.4231916,-7.2974204,-7.4665584)" stroke="#121212" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5">
<path stroke-linejoin="miter" d="M22.5,11.63,22.5,6" stroke-linecap="round" fill="none"/>
<path stroke-linejoin="miter" d="m20,8,5,0" stroke-linecap="round" fill="none"/>
<path stroke-linejoin="miter" d="m22.5,25s4.5-7.5,3-10.5c0,0-1-2.5-3-2.5s-3,2.5-3,2.5c-1.5,3,3,10.5,3,10.5" fill-rule="evenodd" stroke-linecap="butt" fill="#ffffffe6"/>
<path stroke-linejoin="round" d="m11.5,37c5.5,3.5,15.5,3.5,21,0v-7s9-4.5,6-10.5c-4-6.5-13.5-3.5-16,4v3.5-3.5c-3.5-7.5-13-10.5-16-4-3,6,5,10,5,10v7.5z" fill-rule="evenodd" stroke-linecap="round" fill="#ffffffe6"/>
<path stroke-linejoin="round" d="M11.5,30c5.5-3,15.5-3,21,0" stroke-linecap="round" fill="none"/>
<path stroke-linejoin="round" d="m11.5,33.5c5.5-3,15.5-3,21,0" stroke-linecap="round" fill="none"/>
<path stroke-linejoin="round" d="M11.5,37c5.5-3,15.5-3,21,0" stroke-linecap="round" fill="none"/>
</g>
                    </svg>`

let whiteQueen = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>Queen</title>
                    <description>
                    Western white-side Queen
                    </description>

                    <g transform="matrix(1.2987013,0,0,1.2987013,-4.2207793,-4.0584416)" stroke-linejoin="round" stroke="#121212" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5">
                    <path d="m8,12a2,2,0,0,1,-4,0,2,2,0,1,1,4,0z" fill-rule="evenodd" stroke-linecap="round" fill="#ffffffe6"/>
                    <path d="m24.5,7.5a2,2,0,0,1,-4,0,2,2,0,1,1,4,0z" fill-rule="evenodd" stroke-linecap="round" fill="#ffffffe6"/>
                    <path d="m41,12a2,2,0,0,1,-4,0,2,2,0,1,1,4,0z" fill-rule="evenodd" stroke-linecap="round" fill="#ffffffe6"/>
                    <path d="m16,8.5a2,2,0,0,1,-4,0,2,2,0,1,1,4,0z" fill-rule="evenodd" stroke-linecap="round" fill="#ffffffe6"/>
                    <path d="m33,9a2,2,0,0,1,-4,0,2,2,0,1,1,4,0z" fill-rule="evenodd" stroke-linecap="round" fill="#ffffffe6"/>
                    <path d="m9,26c8.5-1.5,21-1.5,27,0l2-12-7,11v-14l-5.5,13.5-3-15-3,15-5.5-14v14.5l-7-11,2,12z" fill-rule="evenodd" stroke-linecap="butt" fill="#ffffffe6"/>
                    <path d="m9,26c0,2,1.5,2,2.5,4,1,1.5,1,1,0.5,3.5-1.5,1-1.5,2.5-1.5,2.5-1.5,1.5,0.5,2.5,0.5,2.5,6.5,1,16.5,1,23,0,0,0,1.5-1,0-2.5,0,0,0.5-1.5-1-2.5-0.5-2.5-0.5-2,0.5-3.5,1-2,2.5-2,2.5-4-8.5-1.5-18.5-1.5-27,0z" fill-rule="evenodd" stroke-linecap="butt" fill="#ffffffe6"/>
                    <path d="M11.5,30c3.5-1,18.5-1,22,0" stroke-linecap="round" fill="none"/>
                    <path d="m12,33.5c6-1,15-1,21,0" stroke-linecap="round" fill="none"/>
                    </g>
                    </svg>`
                    
let whiteBishop = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>Bishop</title>
                    <description>
                    Western white-side Bishop
                    </description>
                    
                    <g transform="matrix(1.4492754,0,0,1.4358729,-7.6086965,-6.815488)" stroke="#121212" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5">
                    <g stroke-linejoin="round" fill-rule="evenodd" stroke-linecap="butt" fill="#ffffffe6">
                        <path d="m9,36c3.39-0.97,10.11,0.43,13.5-2,3.39,2.43,10.11,1.03,13.5,2,0,0,1.65,0.54,3,2-0.68,0.97-1.65,0.99-3,0.5-3.39-0.97-10.11,0.46-13.5-1-3.39,1.46-10.11,0.03-13.5,1-1.354,0.49-2.323,0.47-3-0.5,1.354-1.94,3-2,3-2z"/>
                        <path d="m15,32c2.5,2.5,12.5,2.5,15,0,0.5-1.5,0-2,0-2,0-2.5-2.5-4-2.5-4,5.5-1.5,6-11.5-5-15.5-11,4-10.5,14-5,15.5,0,0-2.5,1.5-2.5,4,0,0-0.5,0.5,0,2z"/>
                        <path d="m25,8a2.5,2.5,0,1,1,-5,0,2.5,2.5,0,1,1,5,0z"/>
                    </g>

                    <path stroke-linejoin="miter" d="m17.5,26,10,0m-12.5,4,15,0m-7.5-14.5,0,5m-2.5-2.5h5" stroke-linecap="round" fill="none"/>
                    </g>
                    </svg>`
                    
let whiteKnight = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>Knight</title>
                    <description>
                    Western white-side Knight
                    </description>

                    <g stroke-linejoin="round" fill-rule="evenodd" transform="matrix(1.4912192,0,0,1.4925373,-7.8284143,-9.3283579)" stroke="#121212" stroke-linecap="round" stroke-dasharray="none" stroke-miterlimit="4">
                    <path d="m22,10c10.5,1,16.5,8,16,29h-23c0-9,10-6.5,8-21" stroke-width="1.5" fill="#ffffffe6"/>
                    <path d="m24,18c0.38,2.91-5.55,7.37-8,9-3,2-2.82,4.34-5,4-1.042-0.94,1.41-3.04,0-3-1,0,0.19,1.23-1,2-1,0-4.003,1-4-4,0-2,6-12,6-12s1.89-1.9,2-3.5c-0.73-0.994-0.5-2-0.5-3,1-1,3,2.5,3,2.5h2s0.78-1.992,2.5-3c1,0,1,3,1,3" stroke-width="1.5" fill="#ffffffe6"/>
                    <path d="m9.5,25.5a0.5,0.5,0,0,1,-1,0,0.5,0.5,0,1,1,1,0z" stroke-width="1.5" fill="#ffffffe6"/>
                    <path d="m14.933,15.75a0.49999,1.5,30.001,0,1,-0.866,-0.5,0.49999,1.5,30.001,0,1,0.866,0.5z" stroke-width="1.49996698" fill="#ffffffe6"/>
                    </g>
                    </svg>`
                    
let whiteRook = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>Rook</title>
                    <description>
                    Western white-side Rook
                    </description>
                    
                    <g transform="matrix(1.5873016,0,0,1.5873016,-10.714286,-13.095238)" stroke="#121212" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5">
                    <path stroke-linejoin="round" d="m9,39,27,0,0-3-27,0,0,3z" fill-rule="evenodd" stroke-linecap="butt" fill="#ffffffe6"/>
                    <path stroke-linejoin="round" d="m12,36,0-4,21,0,0,4-21,0z" fill-rule="evenodd" stroke-linecap="butt" fill="#ffffffe6"/>
                    <path stroke-linejoin="round" d="m11,14,0-5,4,0,0,2,5,0,0-2,5,0,0,2,5,0,0-2,4,0,0,5" fill-rule="evenodd" stroke-linecap="butt" fill="#ffffffe6"/>
                    <path stroke-linejoin="round" d="m34,14-3,3-17,0-3-3" fill-rule="evenodd" stroke-linecap="round" fill="#ffffffe6"/>
                    <path stroke-linejoin="miter" d="m31,17,0,12.5-17,0,0-12.5" fill-rule="evenodd" stroke-linecap="butt" fill="#ffffffe6"/>
                    <path stroke-linejoin="round" d="m31,29.5,1.5,2.5-20,0,1.5-2.5" fill-rule="evenodd" stroke-linecap="round" fill="#ffffffe6"/>
                    <path stroke-linejoin="miter" d="m11,14,23,0" stroke-linecap="round" fill="none"/>
                    </g>
                    </svg>`
                    
let whitePawn = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
<title>Pawn</title>
                    <description>
                    Western white-side Pawn
                    </description>

                    <g>
                    <path stroke-linejoin="miter" d="m25,1.1719c-3.4531,0-6.25,2.7969-6.25,6.25,0,1.3906,0.45312,2.6719,1.2188,3.7188-3.0469,1.75-5.125,5.0156-5.125,8.7812,0,3.1719,1.4688,6,3.7656,7.8594-4.688,1.657-11.579,8.672-11.579,21.047h35.938c0-12.375-6.8906-19.391-11.578-21.047,2.2969-1.8594,3.7656-4.6875,3.7656-7.8594,0-3.7656-2.0781-7.0312-5.125-8.7812,0.765-1.047,1.218-2.3285,1.218-3.7191,0-3.4531-2.7969-6.25-6.25-6.25z" fill-rule="nonzero" stroke="#121212" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="2.34375" fill="#ffffffe6"/>
                    </g>
                    </svg>`

let blackKing = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>King</title>
                    <description>
                    Western black-side King
                    </description>
                    
                    <g stroke-miterlimit="4" stroke-width="1.5" stroke-dasharray="none" transform="matrix(1.4373857,0,0,1.4234875,-7.2974204,-7.4733086)">
                    <path stroke-linejoin="miter" d="M22.5,11.63,22.5,6" stroke="#121212" stroke-linecap="round" fill="none"/>
                    <path stroke-linejoin="miter" d="m22.5,25s4.5-7.5,3-10.5c0,0-1-2.5-3-2.5s-3,2.5-3,2.5c-1.5,3,3,10.5,3,10.5" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" fill="#121212"/>
                    <path stroke-linejoin="round" d="m11.5,37c5.5,3.5,15.5,3.5,21,0v-7s9-4.5,6-10.5c-4-6.5-13.5-3.5-16,4v3.5-3.5c-3.5-7.5-13-10.5-16-4-3,6,5,10,5,10v7.5z" fill-rule="evenodd" stroke="#121212" stroke-linecap="round" fill="#121212"/>
                    <path stroke-linejoin="miter" d="m20,8,5,0" stroke="#121212" stroke-linecap="round" fill="none"/>
                    <path stroke-linejoin="round" d="m32,29.5s8.5-4,6.03-9.65c-3.88-5.85-13.03-1.85-15.53,4.65l0.01,2.1-0.01-2.1c-2.5-6.5-12.594-10.5-15.503-4.65-2.497,5.65,4.853,9,4.853,9" stroke="#ffffffe6" stroke-linecap="round" fill="none"/>
                    <path stroke-linejoin="round" d="m11.5,30c5.5-3,15.5-3,21,0m-21,3.5c5.5-3,15.5-3,21,0m-21,3.5c5.5-3,15.5-3,21,0" stroke="#ffffffe6" stroke-linecap="round" fill="none"/>
                    </g>
                    </svg>`
                    
let blackQueen = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>Queen</title>
                    <description>
                    Western black-side Queen
                    </description>
                    
                    <g transform="matrix(1.2987013,0,0,1.2987013,-4.2207793,-5.157942)">
                    <g fill="#121212" fill-rule="evenodd">
                    <circle d="M 8.75,12 C 8.75,13.518783 7.5187831,14.75 6,14.75 4.4812169,14.75 3.25,13.518783 3.25,12 3.25,10.481217 4.4812169,9.25 6,9.25 c 1.5187831,0 2.75,1.231217 2.75,2.75 z" cy="12" cx="6" r="2.75"/>
                    <circle d="m 16.75,9 c 0,1.518783 -1.231217,2.75 -2.75,2.75 -1.518783,0 -2.75,-1.231217 -2.75,-2.75 0,-1.5187831 1.231217,-2.75 2.75,-2.75 1.518783,0 2.75,1.2312169 2.75,2.75 z" cy="9" cx="14" r="2.75"/>
                    <circle d="m 25.25,8 c 0,1.5187831 -1.231217,2.75 -2.75,2.75 -1.518783,0 -2.75,-1.2312169 -2.75,-2.75 0,-1.5187831 1.231217,-2.75 2.75,-2.75 1.518783,0 2.75,1.2312169 2.75,2.75 z" cy="8" cx="22.5" r="2.75"/>
                    <circle d="m 33.75,9 c 0,1.518783 -1.231217,2.75 -2.75,2.75 -1.518783,0 -2.75,-1.231217 -2.75,-2.75 0,-1.5187831 1.231217,-2.75 2.75,-2.75 1.518783,0 2.75,1.2312169 2.75,2.75 z" cy="9" cx="31" r="2.75"/>
                        <circle d="m 41.75,12 c 0,1.518783 -1.231217,2.75 -2.75,2.75 -1.518783,0 -2.75,-1.231217 -2.75,-2.75 0,-1.518783 1.231217,-2.75 2.75,-2.75 1.518783,0 2.75,1.231217 2.75,2.75 z" cy="12" cx="39" r="2.75"/>
                    </g>

                    <path stroke-linejoin="round" d="m9,26c8.5-1.5,21-1.5,27,0l2.5-12.5-7.5,11.5-0.3-14.1-5.2,13.6-3-14.5-3,14.5-5.2-13.6-0.3,14.1-7.5-11.5,2.5,12.5z" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="round" d="m9,26c0,2,1.5,2,2.5,4,1,1.5,1,1,0.5,3.5-1.5,1-1.5,2.5-1.5,2.5-1.5,1.5,0.5,2.5,0.5,2.5,6.5,1,16.5,1,23,0,0,0,1.5-1,0-2.5,0,0,0.5-1.5-1-2.5-0.5-2.5-0.5-2,0.5-3.5,1-2,2.5-2,2.5-4-8.5-1.5-18.5-1.5-27,0z" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="round" d="m11,38.5a35,35,0,0,0,23,0" stroke="#121212" stroke-linecap="butt" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="none"/>
                    <path stroke-linejoin="round" d="m11,29a35,35,0,0,1,23,0" stroke="#ffffffe6" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="none"/>
                    <path stroke-linejoin="round" d="m12.5,31.5,20,0" stroke="#ffffffe6" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="none"/>
                    <path stroke-linejoin="round" d="m11.5,34.5a35,35,0,0,0,22,0" stroke="#ffffffe6" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="none"/>
                    <path stroke-linejoin="round" d="m10.5,37.5a35,35,0,0,0,24,0" stroke="#ffffffe6" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="none"/>
                    </g>
                    </svg>`
                    
let blackBishop = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
<title>Bishop</title>
<description>
Western black-side Bishop
</description>

                    <g transform="matrix(1.4492754,0,0,1.4358729,-7.6086965,-6.8154879)" stroke-dasharray="none" stroke-miterlimit="4" stroke-width="1.5">
                    <g stroke-linejoin="round" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" fill="#121212">
                        <path d="m9,36c3.39-0.97,10.11,0.43,13.5-2,3.39,2.43,10.11,1.03,13.5,2,0,0,1.65,0.54,3,2-0.68,0.97-1.65,0.99-3,0.5-3.39-0.97-10.11,0.46-13.5-1-3.39,1.46-10.11,0.03-13.5,1-1.354,0.49-2.323,0.47-3-0.5,1.354-1.94,3-2,3-2z"/>
                        <path d="m15,32c2.5,2.5,12.5,2.5,15,0,0.5-1.5,0-2,0-2,0-2.5-2.5-4-2.5-4,5.5-1.5,6-11.5-5-15.5-11,4-10.5,14-5,15.5,0,0-2.5,1.5-2.5,4,0,0-0.5,0.5,0,2z"/>
                        <path d="m25,8a2.5,2.5,0,1,1,-5,0,2.5,2.5,0,1,1,5,0z"/>
                    </g>
                    
                    <path stroke-linejoin="miter" d="m17.5,26,10,0m-12.5,4,15,0m-7.5-14.5,0,5m-2.5-2.5h5" stroke="#ffffffe6" stroke-linecap="round" fill="none"/>
                    </g>
                    </svg>`

let blackKnight = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>Knight</title>
                    <description>
                    Western black-side Knight
                    </description>

                    <g transform="matrix(1.4912192,0,0,1.4925373,-7.8284143,-16.791044)">
                    <path stroke-linejoin="round" d="m22,15c10.5,1,16.5,8,16,29h-23c0-9,10-6.5,8-21" stroke="#121212" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="round" d="m24,23c0.38,2.91-5.55,7.37-8,9-3,2-2.82,4.34-5,4-1.042-0.94,1.41-3.04,0-3-1,0,0.19,1.23-1,2-1,0-4.003,1-4-4,0-2,6-12,6-12s1.89-1.9,2-3.5c-0.73-0.994-0.5-2-0.5-3,1-1,3,2.5,3,2.5h2s0.78-1.992,2.5-3c1,0,1,3,1,3" stroke="#121212" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="round" d="m9.5,30.5a0.5,0.5,0,0,1,-1,0,0.5,0.5,0,1,1,1,0z" stroke="#ffffffe6" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.5" fill="#ffffffe6"/>
                    <path stroke-linejoin="round" d="m14.933,20.75a0.49999,1.5,30.001,0,1,-0.866,-0.5,0.49999,1.5,30.001,0,1,0.866,0.5z" stroke="#ffffffe6" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="1.49996698" fill="#ffffffe6"/>
                    <path fill="#ffffffe6" d="M24.55,15.4,24.1,16.85,24.6,17c3.15,1,5.65,2.49,7.9,6.75s3.25,10.31,2.75,20.25l-0.05,0.5h2.25l0.05-0.5c0.5-10.06-0.88-16.85-3.25-21.34s-5.79-6.64-9.19-7.16l-0.51-0.1z"/>
                    </g>
                    </svg>`
                    
let blackRook = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>Rook</title>
                    <description>
                    Western black-side Rook
                    </description>
                    
                    <g stroke-miterlimit="4" stroke-dasharray="none" transform="matrix(1.5873016,0,0,1.5873016,-10.714286,-13.095238)">
                    <path stroke-linejoin="round" d="m9,39,27,0,0-3-27,0,0,3z" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="round" d="m12.5,32,1.5-2.5,17,0,1.5,2.5-20,0z" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="round" d="m12,36,0-4,21,0,0,4-21,0z" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="miter" d="m14,29.5,0-13,17,0,0,13-17,0z" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="round" d="m14,16.5-3-2.5,23,0-3,2.5-17,0z" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="round" d="m11,14,0-5,4,0,0,2,5,0,0-2,5,0,0,2,5,0,0-2,4,0,0,5-23,0z" fill-rule="evenodd" stroke="#121212" stroke-linecap="butt" stroke-width="1.5" fill="#121212"/>
                    <path stroke-linejoin="miter" d="m12,35.5,21,0,0,0" stroke="#ffffffe6" stroke-linecap="round" stroke-width="1" fill="none"/>
                    <path stroke-linejoin="miter" d="m13,31.5,19,0" stroke="#ffffffe6" stroke-linecap="round" stroke-width="1" fill="none"/>
                    <path stroke-linejoin="miter" d="m14,29.5,17,0" stroke="#ffffffe6" stroke-linecap="round" stroke-width="1" fill="none"/>
                    <path stroke-linejoin="miter" d="m14,16.5,17,0" stroke="#ffffffe6" stroke-linecap="round" stroke-width="1" fill="none"/>
                    <path stroke-linejoin="miter" d="m11,14,23,0" stroke="#ffffffe6" stroke-linecap="round" stroke-width="1" fill="none"/>
                    </g>
                    </svg>`
                    
let blackPawn = `<svg class="piece" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="-3 -3 56 56" height="100%" width="100%">
                    <title>Pawn</title>
                    <description>
                    Western black-side Pawn
                    </description>

                    <g>
                    <path stroke-linejoin="miter" d="m25,1.1719c-3.4531,0-6.25,2.7969-6.25,6.25,0,1.3906,0.45312,2.6719,1.2188,3.7188-3.0469,1.75-5.125,5.0156-5.125,8.7812,0,3.1719,1.4688,6,3.7656,7.8594-4.688,1.657-11.579,8.672-11.579,21.047h35.938c0-12.375-6.8906-19.391-11.578-21.047,2.2969-1.8594,3.7656-4.6875,3.7656-7.8594,0-3.7656-2.0781-7.0312-5.125-8.7812,0.765-1.047,1.218-2.3285,1.218-3.7191,0-3.4531-2.7969-6.25-6.25-6.25z" fill-rule="nonzero" stroke="#121212" stroke-linecap="round" stroke-miterlimit="4" stroke-dasharray="none" stroke-width="2.34375" fill="#121212"/>
                    </g>
                    </svg>`

let clickable = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 9 9" width="25%" height="100%">
                    <circle cx="4.5" cy="4.5" r="3.5" fill="rgb(255,255,255,.2)"/>
                    </svg>`

var clickable2 = document.createElementNS("http://www.w3.org/2000/svg", "svg");
clickable2.setAttribute('width', '25%');
clickable2.setAttribute('height', '100%');
clickable2.setAttribute('viewBox', '0 0 9 9')
clickable2.innerHTML = `<circle cx="4.5" cy="4.5" r="3.5" fill="rgb(255,255,255,.2)"/>`

const pieces = {
    'r' : blackRook,
    'n' : blackKnight,
    'b' : blackBishop,
    'q' : blackQueen,
    'k' : blackKing,
    'p' : blackPawn,
    'R' : whiteRook,
    'N' : whiteKnight,
    'B' : whiteBishop,
    'Q' : whiteQueen,
    'K' : whiteKing,
    'P' : whitePawn,
} 

loadPiecesEPD()

function flipBoard(){
    if(perspective == 1){
        perspective = 2
    }else if(perspective == 2){
        perspective = 1
    }
    createBoard();
    loadPiecesEPD();
    swapLabels();
} 
    
function createBoard(){
    let htmlUpdate = "";
    if(perspective == 1){
        for(let c=0; c < 8; c++) {//white perspective
            htmlUpdate += '<div class="ChessColumn">'
            for(let r=0; r < 8; r++) {
                if((r%2 == 1 && c%2 == 0) || (r%2 == 0 && c%2 == 1)) {
                    htmlUpdate += '<div class="ChessBoxGrey" id="' + r + c + '"></div>'
                }
                else {
                    htmlUpdate += '<div class="ChessBoxOrange" id="' + r + c + '"></div>'
                }
            }
            htmlUpdate += '</div>'
        }
        
    }
    else if(perspective == 2){
        for(let c=7; c >= 0; c--) {//white perspective
            htmlUpdate += '<div class="ChessColumn">'
            for(let r=7; r >=0; r--) {
                if((r%2 == 1 && c%2 == 0) || (r%2 == 0 && c%2 == 1)) {
                    htmlUpdate += '<div class="ChessBoxGrey" id="' + r + c + '"></div>'
                }
                else {
                    htmlUpdate += '<div class="ChessBoxOrange" id="' + r + c + '"></div>'
                }
            }
            htmlUpdate += '</div>'
        }
    }
    boardContainer.innerHTML = htmlUpdate;
}

function swapLabels(){
    if(perspective == 1){
        document.querySelector("#y1").innerHTML = "8"
        document.querySelector("#y2").innerHTML = "7"
        document.querySelector("#y3").innerHTML = "6"
        document.querySelector("#y4").innerHTML = "5"
        document.querySelector("#y5").innerHTML = "4"
        document.querySelector("#y6").innerHTML = "3"
        document.querySelector("#y7").innerHTML = "2"
        document.querySelector("#y8").innerHTML = "1"

        document.querySelector("#x1").innerHTML = "A"
        document.querySelector("#x2").innerHTML = "B"
        document.querySelector("#x3").innerHTML = "C"
        document.querySelector("#x4").innerHTML = "D"
        document.querySelector("#x5").innerHTML = "E"
        document.querySelector("#x6").innerHTML = "F"
        document.querySelector("#x7").innerHTML = "G"
        document.querySelector("#x8").innerHTML = "H"
    }
    else if(perspective == 2){
        document.querySelector("#y1").innerHTML = "1"
        document.querySelector("#y2").innerHTML = "2"
        document.querySelector("#y3").innerHTML = "3"
        document.querySelector("#y4").innerHTML = "4"
        document.querySelector("#y5").innerHTML = "5"
        document.querySelector("#y6").innerHTML = "6"
        document.querySelector("#y7").innerHTML = "7"
        document.querySelector("#y8").innerHTML = "8"

        document.querySelector("#x1").innerHTML = "H"
        document.querySelector("#x2").innerHTML = "G"
        document.querySelector("#x3").innerHTML = "F"
        document.querySelector("#x4").innerHTML = "E"
        document.querySelector("#x5").innerHTML = "D"
        document.querySelector("#x6").innerHTML = "C"
        document.querySelector("#x7").innerHTML = "B"
        document.querySelector("#x8").innerHTML = "A"
    }
}

function loadPiecesEPD() { //1A = 70 (i = 7, j = 0) i is number, j is letter

    let rowsEPD = epdBoard.split('/')
    let x = 0

    for (let i = rowsEPD.length-1; i >= 0; i--) { //for each row

        for (let j = 0; j < rowsEPD[i].length; j++) { //for each item in the row

            curRow = rowsEPD[i]
            tempChar = curRow[j]
            if (!isNaN(tempChar)) { //is a number
                x = x + (parseInt(tempChar) - 1)
            }
            else { //it's a letter (piece)
                
                document.getElementById(i + "" + x).innerHTML = pieces[tempChar]
            }

            x++
        }
        x = 0
    }
    addAvailMoves()
}

ws.onmessage = function(e){
    const data = JSON.parse(e.data);
    if(data.color == 1){
        document.querySelector(".player1").innerHTML = ("White - " + data.username);
    }
    else if(data.color == 2){
        document.querySelector(".player2").innerHTML = ("Black - " + data.username);
        flipBoard()//if the player is playing black flip the board to their perspective
    }
    if(data.available_moves){
        available_moves = data.available_moves
        addAvailMoves()
    }
    if (data.move) {//if there is a move in the message
        
        from2 = squareMap[data.move[0]]
        from1 = squareMap[data.move[1]]

        to2 = squareMap[data.move[2]]
        to1 = squareMap[data.move[3]]

        //place svg in "to" square
        document.getElementById(to1 + to2).innerHTML = document.getElementById(from1 + from2).innerHTML

        //remove svg from "from" square
        document.getElementById(from1 + from2).innerHTML = ""
    }
}

function addAvailMoves() {

    for (const key in available_moves) {
        selectedPieceID = squareMap[key[1]] + squareMap[key[0]]
        selectedPiece = document.getElementById(selectedPieceID).firstElementChild
        selectedPiece.addEventListener("click", clickPiece)
    }
}

function clickPiece(event) {
    
    startingSquare = this.parentElement.id
    moveArr = available_moves[letterMap[startingSquare[1]] + "" + numberMap[startingSquare[0]]]
    console.log(moveArr)
    let num = displayedMoves.length
    if(num > 0){
        for (var i = 0; i < num; i++){
            square = document.getElementById(displayedMoves.pop())
            square.removeChild(square.firstElementChild)
        }
    }
        
    for (const toSquare in moveArr){
        
        toSquareId = squareMap[moveArr[toSquare][1]] + squareMap[moveArr[toSquare][0]]
        displayedMoves.push(toSquareId)
        document.getElementById(toSquareId).appendChild(clickable2.cloneNode(true))
        
    }
}

