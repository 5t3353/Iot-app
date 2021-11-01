
var x1 = {{dash}};

var x2 = {{dash}};


var trace1 = {

x: x1,

type: "histogram",

};

var trace2 = {

x: x2,

type: "histogram",

};

var font = {

family: 'Courier New, monospace',

size: 18,

color: '#FFFFFF'
}

var data = [trace1, trace2];

var layout = {barmode: "stack",
            plot_bgcolor:"#fff",
            paper_bgcolor:"rgba(33, 72, 119, 0.7)",
            color:"#FFF",font};

Plotly.newPlot('tester', data, layout);



  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>


    <section class="graph__viz">
  <figure>
    <canvas id="pieChart"></canvas>
  </figure>
  <figure>
    <canvas id="barChart"></canvas>
  </figure>
  <figure>
    <canvas id="scatterChart"></canvas>
  </figure>
  </section>

<script>

  var data =  {  labels : ["Temperature","Humidity","Co2"],
               datasets : [{label : "Data",
                             data : [850,234,13,432,234),(13,452,34,42,342),(12,43,52,123,123)],
                             borderWidth : 2,
                             scaleStepWidth: 2,
                             borderColor :'black',
                             hoverBackgroundColor: "rgba(33, 72, 119, 0.8)",
                             hoverBorderColor: "white",
                             backgroundColor: ['rgb(255, 70, 0)',
                                               'rgb(5, 162, 30)',
                                               'rgb(255, 205, 86)']}] }

  const options =  {
    plugins: {
         legend: {
             labels: {
                 font: {
                     size: 18
                 }
             }
         }
     }
   }


  var ctx1 = document.getElementById('pieChart').getContext('2d');

  var ctx2 = document.getElementById('barChart').getContext('2d');

  var ctx3 = document.getElementById('scatterChart').getContext('2d');

  var pieChart = new Chart(ctx1,{

      scaleFontColor: "white",

      type : 'pie',

      data : data,

      options : options });

  var barChart = new Chart(ctx2,{

      type : 'bar',

      data : data,

      options : options});

  var sactterChart = new Chart(ctx3,{

      type : 'scatter',

      data : data,

      options : options});
</script>
