let opcion
let value
function xdd(){
	console.log('xddddd')
}

function girIzq(){
  value = value - 90
  document.getElementById('rotImg').style.transform = 'rotate(' + value + 'deg)';
}
function girDer(){
  value = value + 90
  document.getElementById('rotImg').style.transform = 'rotate(' + value + 'deg)';
}


function mostrar(){
  document.getElementById('mostrarOcultar').style.display = "block"
  document.getElementById('img2').style.display = "block"
}

function ocultar(){
  document.getElementById('mostrarOcultar').style.display = "none"
  document.getElementById('img2').style.display = "none"
}

function proceso($tipo) {
	console.log('exitoooooo')
	opcion = $tipo
	if($tipo == 1){
    mostrar()
    // <form id="formulario" action="recibir.php" method="post">
    //   <input type="hidden" value='Jose' name="nombre" required>
    //   <input type="number" placeholder="Ingresa tu edad" name="edad" required title="Ingresa tu edad porfavor">
    //   <br><br>
    //   <input type="submit" id="btnEnviar" name="btnEnviar" value="Enviar formulario">
    // </form>
	}
  if ($tipo == 2) {
    ocultar()
  }
  if ($tipo == 6) {
    ocultar()
    console.log("Opcion 56")
    document.getElementById('espImagen1').style.display = "none"
    document.getElementById('canvas').style.display = "none"
    jQuery.ajax({
      type: 'get',
      url: 'update3.php',
      beforeSend: function(){
          /*
          * Esta función se ejecuta durante el envió de la petición al
          * servidor.
          * */
          // btnEnviar.text("Enviando"); Para button
          document.getElementById('cargando').style.display = "block"
      },
      complete:function(data){
          /*
          * Se ejecuta al termino de la petición
          * */
          console.log('Puntos')
          document.getElementById('cargando').style.display = "none"
          document.getElementById('canvas').style.display = "block"
          datoss();
          draw();
          document.getElementById('espDatos').innerHTML=
          "<center>\
          <button type='button' class='btn btn-primary' onclick='enderezar()'>Procesar</button>\
          </center>";
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
}
function prueba(){
	console.log(opcion)
}
