// function bar() {
//     var data = JSON.parse("{{data|escapejs}}");
//     var dataNode = document.getElementById('alldata');
//     dataNode.innerHTML = "abc"
        // dataNode.innerHTML += "{{data|escapejs}}";
        // dataNode = document.getElementById('neatdata');
        // for (var x in data) {
        //     dataNode.innerHTML += x + ' : ' + data[x][0] + ',,' + data[x][1] + '<br><br>';
        // }

    // var ctx = $("#bar-chartcanvas");

    // var data = {
    //     labels: ["match1", "match2", "match3", "match4", "match5"],
    //     datasets: [{
    //             label: "TeamA score",
    //             data: [10, 50, 25, 100, 40],
    //             backgroundColor: [
    //                 "rgba(10, 20, 30, 0.3)",
    //                 "rgba(10, 20, 30, 0.3)",
    //                 "rgba(10, 20, 30, 0.3)",
    //                 "rgba(10, 20, 30, 0.3)",
    //                 "rgba(10, 20, 30, 0.3)"
    //             ],
    //             borderColor: [
    //                 "rgba(10, 20, 30, 1)",
    //                 "rgba(10, 20, 30, 1)",
    //                 "rgba(10, 20, 30, 1)",
    //                 "rgba(10, 20, 30, 1)",
    //                 "rgba(10, 20, 30, 1)"
    //             ],
    //             borderWidth: 1
    //         }

    //     ]
    // };

    // var options = {
    //     title: {
    //         display: true,
    //         position: "top",
    //         text: "Bar Graph",
    //         fontSize: 18,
    //         fontColor: "#111"
    //     },
    //     legend: {
    //         display: true,
    //         position: "bottom"
    //     },
    //     scales: {
    //         yAxes: [{
    //             ticks: {
    //                 min: 0

    //             }
    //         }]
    //     }
    // };

    // var chart = new Chart(ctx, {
    //     type: "bar",
    //     data: data,
    //     options: options
    // });

// }