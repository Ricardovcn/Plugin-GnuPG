$(document).ready(function(){
    $('.tabs').tabs();

      $("#encryptAba").click(
        function() {
            alert('oi')
        }
        );

        $("#encryptAba").click(
            function() {
                alert('oi')
            }
        );
   });

   var req = new XMLHttpRequest();
   var btn = document.querySelector('#addChave');

  

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
