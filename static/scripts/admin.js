window.onload = function (){
    url = "/api/chartdata"
    axios.get(url)
    .then((response) => {
        var response = response.data;
        draw_chart(response['x_values'], response['y_values'])
    });
}


function draw_chart (x_values, y_values){
    var ctx = document.getElementById("chart").getContext("2d");
  
    new Chart(ctx, {
        type: "line",
        data: {
        labels: x_values,
        datasets: [
            {
            label: "$",
            data: y_values,
            pointRadius: 7,
            pointHoverRadius: 9,
            backgroundColor: ["#E83C5B"],
            borderColor: ["#E83C5B"],
            borderWidth: 1,
            },
        ],
        },
    });

}
