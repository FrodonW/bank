function chart1(url){

    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        var abc = JSON.stringify(data.labels);
        console.log(abc);
        const myArray = abc.split(",");

            for (let i = 0; i < myArray.length; i++) {
                if (i == 0) { myArray[i] = myArray[i].substring(myArray[i].lastIndexOf("-"), myArray[i].lastIndexOf(" ")).slice(2);}
                else {
                    myArray[i] = myArray[i].substring(myArray[i].lastIndexOf("-"), myArray[i].lastIndexOf(" ")).slice(1);
                    }
            }
        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: myArray,
                datasets: [{
                    label: 'labels',
                    data: data.data,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
}