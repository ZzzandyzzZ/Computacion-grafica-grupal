var dataString = $('form').serialize();
function proceso($tipo) {
        dataString={"1" : $tipo};
        $.ajax({
                type: 'POST',
                url: 'procesar.php',
                data: dataString,
                success: function (html) {
                        $("#dividR").load(" #dividR");
                }
        });
}