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
	width = 500
	height = 500;
	var canvas=createCanvas(width,height);
	canvas.parent("canvas");
	LoadImage("uploads/original.jpg");
	archivoTxt.open("GET",fileRuta,false);
	archivoTxt.send(null);
	p(archivoTxt);
	values=archivoTxt.responseText;
	values=values.split(',');
	for (var i = 0; i < values.length; i++) {
	   values[i]=parseInt(values[i]);
	}
	p(values);
	points=[];
	for(var i=0;i<values.length;i+=2){
		points.push(new Point(values[i],values[i+1],30));
	}
 	//console.log(points);
}
function enderezar()
{
	value=0
   p("ENDEREZANDO");
   out='';
   for(var i=0;i<points.length;i++){
		out+=(parseInt(points[i].x)+','+parseInt(points[i].y));
		if(i<points.length-1)out+=',';
	}
	p(out);
	jQuery.ajax({
		url:'upload4.php',
		type:'post',
		data:{values:out},

	beforeSend: function(){
          /*
          * Esta función se ejecuta durante el envió de la petición al
          * servidor.
          * */
          // btnEnviar.text("Enviando"); Para button
          document.getElementById('canvas').style.display = "none"
          document.getElementById('cargando').style.display = "block"
      },
      complete:function(data){
          /*
          * Se ejecuta al termino de la petición
          * */
          console.log('Puntos')
          document.getElementById('cargando').style.display = "none"
          document.getElementById('espImagen1').innerHTML=
          "<img id='rotImg' width=100% src='uploads/original.jpg?"+Math.random()+"' alt='Nature' class='responsive'>"
          document.getElementById('espImagen1').style.display = "block"
          document.getElementById('espDatos').innerHTML=
          "<button type='button' class='btn btn-primary' onclick='filt1()'>B/N</button>\
          <button type='button' class='btn btn-primary' onclick='filt2()'>Color</button>\
          <button type='button' class='btn btn-primary' onclick='filt3()'>Grises</button>\
          <button type='button' class='btn btn-primary' onclick='filt4()'>Original</button>\
          <br>\
          <br>\
          <button type='button' class='btn btn-primary' onclick='girIzq()'>Girar Izquierda</button>\
          <button type='button' class='btn btn-primary' onclick='girDer()'>Girar Derecha</button>\
          "
      },
      success: function(data){
          /*
          * Se ejecuta cuando termina la petición y esta ha sido
          * correcta
          * */
      },
      error: function(data){
          /*
          * Se ejecuta si la peticón ha sido erronea
          * */
          alert("Problemas al tratar de enviar el formulario");
      }
  });

}

function datoss(){
	LoadImage("uploads/original.jpg");
	archivoTxt.open("GET",fileRuta,false);
	archivoTxt.send(null);
	p(archivoTxt);
	values=archivoTxt.responseText;
	values=values.split(',');
	for (var i = 0; i < values.length; i++) {
	   values[i]=parseInt(values[i]);
	}
	p(values);
	points=[];
	for(var i=0;i<values.length;i+=2){
		points.push(new Point(values[i],values[i+1],30));
	}
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