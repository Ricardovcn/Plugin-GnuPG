$(document).ready(function(){
    $('.tabs').tabs();

    $('#btnEncrypt').click( function(event) {
        $.ajax({
            data : {
                email :   $("#emailEncrypt").val(),
                texto :   $("#textoEncrypt").val()
            },
            type : 'POST',
            url : 'http://127.0.0.1:5000/criptografar'
        })

        .done(function(data){
            $("#textoCriptografado").val(data.mensagem);
        });
        event.preventDefault();
    });
   });

   var req = new XMLHttpRequest();
   var btn = document.querySelector('#addChave');
   var abaEncryptar = document.querySelector('#encryptAba');

   var txtAreaic = document.querySelector('#chaveImportar');
   var btnic = document.querySelector('#btnImportarChave');
   btnic.onclick = function(){
    setTimeout(function(){
        alert("Chave importada");
        txtAreaic.value = "";
      }, 500);
      
   }
  

    btn.onclick = function () {
    var email = document.querySelector("#emailC").value;
    var palavra = document.querySelector("#palavra").value;
    req.open('GET', 'http://127.0.0.1:5000/public/'+email+'/'+palavra);
    req.send(null);
   }

    req.onloadend = function() {
        var resp = req.responseText;
        alert()
        var resp_obj = JSON.parse(resp);
        document.querySelector('#chavePublicaC').value = resp_obj.chave;
    }
