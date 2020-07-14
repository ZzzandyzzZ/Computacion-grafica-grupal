var width;
var height;
let img;
var point;
var points;
var arrayData= new Array();
var archivoTxt=new XMLHttpRequest();
var fileRuta ='puntos.txt';
var values;
function setup(){
	width = 500;
	height = 500;
	var canvas=createCanvas(width,height);
	canvas.parent("canvas");
	LoadImage("1.jpg");
	loadTxt();
	points=[];
	for(var i=0;i<values.length;i+=2){
		points.push(new Point(values[i],values[i+1],30));
	}
}
function loadTxt(){
	archivoTxt.open("GET",fileRuta,false);
	archivoTxt.send(null);
	values=archivoTxt.responseText;
	values=values.split(',');
	for (var i = 0; i < values.length; i++) {
	   values[i]=parseInt(values[i]);
	}
}
function enderezar() 
{
   p("ENDEREZANDO");
   out='';
   for(var i=0;i<points.length;i++){
		out+=(parseInt(points[i].x)+','+parseInt(points[i].y));
		if(i<points.length-1)out+=',';
	}
	p(out);
	jQuery.ajax({
		url:'update.php',
		type:'post',
		data:{values:out},
		
	}).done(function(resp){
		LoadImage("out.jpg");
		
	});
   
}

function draw(){
	image(img,0,0,width,height);
	drawLines();
	if (mouseIsPressed){
		for(var i=0;i<points.length;i++){
			if(points[i].clicked())
				point=points[i];
		}
		if(point!=null){
			point.y=mouseY;
			point.x=mouseX;
		}
	}
	else{
		point=null;
		for(var i=0;i<points.length;i++){
			points[i].desactive();
		}
	}	
}
function drawLines(){
	stroke(0,0,120);
	strokeWeight(4);
	for(var i=0;i<points.length-1;i++){
		line(points[i].x,points[i].y,points[i+1].x,points[i+1].y);
	}
	line(points[points.length-1].x,points[points.length-1].y,points[0].x,points[0].y);
}
function LoadImage(name){
	img=loadImage(
		name, 
		img => {image(img,0,0,width,height);}, 
	    (event) => { 
	      fill("red") 
	      text("Error: The image could not be loaded.", 20, 40); 
	      console.log(event); 
	    } 
	);
}