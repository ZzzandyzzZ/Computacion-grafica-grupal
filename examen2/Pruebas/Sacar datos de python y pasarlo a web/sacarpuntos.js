var arrayData= new Array();
var archivoTxt=new XMLHttpRequest();
var fileRuta ='puntos.txt';
archivoTxt.open("GET",fileRuta,false);
archivoTxt.send(null);
var txt=archivoTxt.responseText;
txt=txt.split(',');
for (var i = 0; i < txt.length; i++) {
   txt[i]=parseInt(txt[i]);
}

console.log(txt.length);
console.log(txt[0]);
console.log(txt[1]);
console.log(txt[2]);
console.log(txt[3]);
console.log(txt[4]);
console.log(txt[5]);
console.log(txt[6]);
console.log(txt[7]);

//arrayData=parseInt(arrayData[2]);






