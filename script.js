const ctx = document.getElementById('classChart');

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['First Class', 'Second Class', 'Third Class'],
        datasets: [{
            label: 'Passengers',
            data: [216,184,491],
            backgroundColor:[
                '#3498db',
                '#2ecc71',
                '#e74c3c'
            ],
            borderRadius:8
        }]
    },
    options:{
        responsive:true,
        plugins:{
            legend:{
                display:false
            },
            title:{
                display:true,
                text:'Passenger Class Distribution'
            }
        },
        scales:{
            y:{
                beginAtZero:true
            }
        }
    }
});