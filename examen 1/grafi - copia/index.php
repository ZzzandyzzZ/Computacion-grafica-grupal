<!DOCTYPE html>
<html>
<head>
	<title>CG</title>
	<script type="text/javascript" src="js/jquery-3.5.1.min.js"></script>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
	<script type="text/javascript" src="js/bootstrap.min.js"></script>
	<script type="text/javascript" src="js/ajax.js"></script>
	<script type="text/javascript" src="js/funciones.js"></script>
  <link rel='stylesheet' href='css/imgareaselect-animated.css'>
  <link rel='stylesheet' href='css/imgareaselect-default.css'>
	<meta charset="utf-8">


<meta charset="utf-8">
  <title>Swiper demo</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1">
  <!-- Link Swiper's CSS -->
  <link rel="stylesheet" href="https://swiperjs.com/package/css/swiper.min.css">

  <!-- Demo styles -->
  <style>
    html, body {
      position: relative;
      height: 100%;
    }
    body {
      margin: 0;
      padding: 0;
    }
    .swiper-container {
      width: 100%;
      height: 70%;
    }
    .swiper-slide {
      overflow: hidden;
    }
  </style>
</head>
<body>
	<div class="container">
	<nav class="navbar navbar-dark bg-dark">
		<form class="form-inline" onsubmit="return false" name="formularioUsuario">
    		<button class="btn btn-outline-success" type="button" onclick="proceso(1)">Histogram</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(2)">Op. Exponencial</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(4)">Op. Logaritmico</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(5)">Op. raiz</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(7)">Contrast Stretching</button>
    		<button class="btn btn-outline-success" type="button" onclick="proceso(8)">Thresholding</button>
        <button class="btn btn-outline-success" type="button" onclick="casca()">Cascada</button>

		</form>
	</nav>

	<form enctype="multipart/form-data" action="#" method="POST">
	<div class="input-group mb-3">
		<div class="input-group-prepend">
			<button class="btn btn-outline-secondary upload" type="submit" onclick="proceso(3)">Subir</button>
		</div>
		<div class="custom-file">
			<input type="file" class="custom-file-input" id="image" name="image">
			<label class="custom-file-label" for="image">Escoga un archivo</label>
		</div>
	</div>
	</form>
	</div>


   <div class="container">
     <p>&nbsp;</p>
    <input type="button" id="boton_de_recorte" value="Recortar" >
    <p>&nbsp;</p>
   </div>

     <center>
  <figure>
    <div id="divid">
        <?php

            if(file_exists("uploads/original.jpg")){
              echo '<img src="uploads/original.jpg?'.rand().'" id="mi_imagen" alt="">';
            }
          ?>
     </div>
      </figure>
  </center>

  <div class="swiper-container">
    <div class="swiper-wrapper">

      <div class="swiper-slide">
        <div class="swiper-zoom-container">
				<?php
					if(file_exists("uploads/original.jpg")){
					echo '<img src="uploads/histograma.png?'.rand().'">';
					}
				?>
        </div>
      </div>

      <?php

            if(file_exists("uploads/original.jpg")){
              echo '<div class="swiper-slide">
              <div class="swiper-zoom-container">
              <img src="uploads/recorte.jpg?'.rand().'" id="mi_imagen" alt="">
                </div> </div>';
            }
          ?>

      <div class="swiper-slide">
        <div class="swiper-zoom-container">
         <div id="dividR" name="dividR">
          <?php
			if(file_exists("uploads/original.jpg")){
				echo '<img src="uploads/resultado.jpg?'.rand().'">';
			}
		?>
       </div>
        </div>
      </div>
    </div>
    <!-- Add Pagination -->
    <div class="swiper-pagination swiper-pagination-white"></div>
    <!-- Add Navigation -->
    <div class="swiper-button-prev"></div>
    <div class="swiper-button-next"></div>
  </div>

  <!-- Swiper JS -->
  <script src="https://swiperjs.com/package/js/swiper.min.js"></script>

  <!-- Initialize Swiper -->
  <script>
    var swiper = new Swiper('.swiper-container', {
      zoom: true,
      pagination: {
        el: '.swiper-pagination',
      },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });
  </script>

  <!-- Recorte -->
  <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  <script src="js/jquery.imgareaselect.js"></script>
  <script type="text/javascript" src="js/recorte.js"></script>

</body>
</html>