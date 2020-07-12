var width;
var height;
let img;
var point;
var points;
function setup(){
	width = 600;
	height = 700;
	var canvas=createCanvas(width,height);
	canvas.parent("canvas");
	img=loadImage(
		"1.png", 
		img => {image(img,0,0,width,height);}, 
	    (event) => { 
	      fill("red") 
	      text("Error: The image could not be loaded.", 20, 40); 
	      console.log(event); 
	    } 
	);
	values=[10,10,200,200,300,300,400,400];
	points=[];
	for(var i=0;i<values.length;i+=2){
		points.push(new Point(values[i],values[i+1],50));
	}
	console.log(points);
	//point= new Point(100,100,50);
    
}

function draw(){
	
	if (mouseIsPressed){
		image(img,0,0,width,height)
		
		for(var i=0;i<points.length;i++){
			points[i].clicked();
		}
	}
	for(var i=0;i<points.length;i++){
		points[i].draw();
	}
}