window.onload = function (){
    ids = document.querySelectorAll("[id=prod]")
    ids_input = document.getElementById("ids")
    console.log(ids_input)
    for (prod of ids){
        ids_input.value += prod.value + " "
    }
}

function plus(sums){
    var counter = document.getElementById("counter")
    var sum = document.getElementById("sum")
    counter.innerText = String(parseInt(counter.innerText)+1)
    sum.innerText = String((parseFloat(sums) * parseInt(counter.innerText)).toFixed(2))
    document.getElementById("inputDays").value = String(parseInt(counter.innerText))
} 
     
function minus(sums){
    var counter = document.getElementById("counter")
    if (parseFloat(counter.innerText) > 1){
        var sum = document.getElementById("sum")
        counter.innerText = String(parseInt(counter.innerText)-1)
        sum.innerText = String((parseFloat(sums) * parseInt(counter.innerText)).toFixed(2))
        document.getElementById("inputDays").value = String(parseInt(counter.innerText))
    }
}
