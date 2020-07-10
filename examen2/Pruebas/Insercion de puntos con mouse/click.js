//Declaro variables
var x = 0;
var y = 0;
var x2 = 0;
var y2 = 0;

window.onload = function(){
click();
};

function dibujar(x,y,x2,y2){
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

ctx.fillStyle ="red";
ctx.fillRect(x, y, x2, y2);
ctx.fill();
console.log(x,y);
}

function click(){
//Añadimos un addEventListener al canvas, para reconocer el click
canvas.addEventListener("click",
//Una vez se haya clickado se activará la siguiente función
function(e){
pintar(e.clientX, e.clientY);
}
,false);
}

function pintar(x, y){
dibujar(x, y, 10, 10);
}