( function ( $ ) {
    
    const req = new XMLHttpRequest();//The onreadystatechange property
    //specifies a function to be
    //executed every time the status
    //of the XMLHttpRequest changes

     
    req.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
    //The responseText property
    //returns a text string
    var data = JSON.parse(this.responseText);
    //Team chart
     var ctx = document.getElementById( "team-chart" );
    
    
     ctx.height = 150;
     var myChart = new Chart( ctx, data );
     

    //Do some stuff
    }

    };
    req.open("GET", "/map/json", true);
    req.send()

    
    
 
   



   
    var dadmmta = {
        type: 'line',
        data: {
            labels: [ "2012", "2013", "2014", "2015", "2018", "2017", "2018" , "2019" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                data: [ 0, 7, 3, 5, 2, 8, 6 ],
                label: "Expense",
                backgroundColor: 'rgba(0,200,155,.35)',
                borderColor: 'rgba(0,200,155,0.60)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,200,155,0.60)',
                    },
                    {
                data: [ 0, 6, 3, 4, 13, 7, 10 ],
                label: "Profit",
                backgroundColor: 'rgba(0,194,146,.25)',
                borderColor: 'rgba(0,194,146,0.5)',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: 'rgba(0,194,146,0.5)',
                    }, ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },


            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                        } ]
            },
            title: {
                display: false,
            }
        }
    }    







} )( jQuery );
