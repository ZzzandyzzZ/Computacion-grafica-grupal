/******************************* variables *******************/
//Preparamos el render
var Render = new THREE.WebGLRenderer();
//El escenario
var Escenario = new THREE.Scene();
//La cámara
var Camara = new THREE.PerspectiveCamera();
// la Figura
var Figura;
//var sphere;
var controls;

/**************************llamado a las funciones ******************/
inicio();
animacion();
/******************************* inicio *******************/
function inicio() {
  //Tamaño del render(resultado)
  Render.setSize(800, 600);
  //Se agrega el render al documento html
  document.getElementById("render").appendChild(Render.domElement);
  //Acercamos la cámara en z es profundidad para ver el punto
  Camara.position.z = 100;
  //agregando la cámara al escenario
  Escenario.add(Camara);
  // cargar nuevos modelos
  cargar_modelo();
  // agregamos todo el escenario y la cámara al render
  controls = new THREE.OrbitControls(Camara, Render.domElement);
}
function cargar_modelo() {
  //////////////////////
  var geometry;
  var material;
  var sphere;
  /////////////////////
  var file = "coordenadas.txt";
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", file, false);
  rawFile.send(null);
  var txt = rawFile.responseText;
  var xD = txt.split("\n");
  var x;
  for (var i = 0; i < xD.length; i++) {
    x = xD[i].split(",");
    geometry = new THREE.SphereGeometry(1, 8, 6);
    material = new THREE.MeshBasicMaterial({
      color: 0xffff00,
      wireframe: true,
    });
    sphere = new THREE.Mesh(geometry, material);
    sphere.position.x = x[0];
    sphere.position.y = x[1];
    sphere.position.z = x[2];
    Escenario.add(sphere);
  }
}
function animacion() {
  requestAnimationFrame(animacion);
  render_modelo();
}
function render_modelo() {
  controls.update();
  Render.render(Escenario, Camara);
}
