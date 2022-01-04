/*
window.onload = function(){
    var submit = document.getElementById("submit")
    submit.onclick = function(){
        var email = document.getElementById("email").value
        var password = document.getElementById("password").value
        if (email != "" && password != ""){
            setTimeout(async function(){
                await axios
                .post("/api/add-product", prodDict)
                .then(function (response) {
                  console.log(response);
                })
                .catch(function (error) {
                  console.log(error);
                });
            }, 5000);
        }
    }
}
*/
