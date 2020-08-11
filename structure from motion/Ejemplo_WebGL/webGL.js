/******************************* variables *******************/
//Preparamos el render
var Render=new THREE.WebGLRenderer();
//El escenario
var Escenario=new THREE.Scene();
//La cámara
var Camara=new THREE.PerspectiveCamera();
// la Figura 
var Figura;
var controls;

/**************************llamado a las funciones ******************/
inicio();
animacion();
/******************************* inicio *******************/
function inicio(){
       //Tamaño del render(resultado)
       Render.setSize(800,600);
       //Se agrega el render al documento html
       document.getElementById('render').appendChild(Render.domElement);
       //Acercamos la cámara en z es profundidad para ver el punto
       Camara.position.z=100;
       //agregando la cámara al escenario
       Escenario.add(Camara);
         // cargar nuevos modelos
       cargar_modelo();
       // agregamos todo el escenario y la cámara al render
        controls=new THREE.OrbitControls(Camara,Render.domElement);
}
function cargar_modelo(){
    // Geometría
    Geometria=new THREE.Geometry();
    var vertices=[
                    [2,7,0],
                    [7,2,0],
                    [12,7,0],
                    [12,17,0],
                    [7,12,0],
                    [2,17,0],
                    [2,7,0],
                    [2,7,2],
                    [7,2,2],
                    [12,7,2],
                    [12,17,2],
                    [7,12,2],
                    [2,17,2],
                    [2,7,2]
    
                ];
    var long_vertices=vertices.length;
    for(i=0;i<long_vertices;i++){
        x=vertices[i][0];
        y=vertices[i][1];
        z=vertices[i][2];
        //Agregamos vértices al vector
        Vector=new THREE.Vector3(x,y,z);
        //Agregamos el vector a la geometría
        Geometria.vertices.push(Vector);   
    }
    // agregamos un material para que el punto tenga color
    Material=new THREE.ParticleBasicMaterial({color:0XFF0000});
    // creamos una partícula con la geometría y el material
    Figura=new THREE.Line(Geometria,Material);
    // agregamos la partícula al escenario
    Escenario.add(Figura);
}
function animacion(){
    requestAnimationFrame(animacion);
    render_modelo();
}
function render_modelo(){
    controls.update();
       Render.render(Escenario,Camara);
    }


