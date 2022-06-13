document.addEventListener('DOMContentLoaded', function () {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json')
        .then(response => response.json())
        .then(data => {
            const tMinHoje = data.data[0].tMin;
            const tMaxHoje = data.data[0].tMax;
            const dateHoje = data.data[0].forecastDate;
            const precipitacaoHoje = data.data[0].precipitaProb;
            const tMinAmanha = data.data[1].tMin;
            const tMaxAmanha = data.data[1].tMax;
            const dateAmanha = data.data[1].forecastDate;
            const precipitacaoAmanha = data.data[1].precipitaProb;
            document.getElementById('dateHoje-lisboa').innerHTML = dateHoje;
            document.getElementById('precipitacaoHoje-lisboa').innerHTML = precipitacaoHoje + '%';
            document.getElementById('tMinHoje-lisboa').innerHTML = tMinHoje + 'º';
            document.getElementById('tMaxHoje-lisboa').innerHTML = tMaxHoje + 'º';
            document.getElementById('dateAmanha-lisboa').innerHTML = dateAmanha;
            document.getElementById('precipitacaoAmanha-lisboa').innerHTML = precipitacaoAmanha + '%';
            document.getElementById('tMinAmanha-lisboa').innerHTML = tMinAmanha + 'º';
            document.getElementById('tMaxAmanha-lisboa').innerHTML = tMaxAmanha + 'º';
        });

    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1131200.json')
        .then(response => response.json())
        .then(data => {
            const tMinHoje = data.data[0].tMin;
            const tMaxHoje = data.data[0].tMax;
            const dateHoje = data.data[0].forecastDate;
            const precipitacaoHoje = data.data[0].precipitaProb;
            const tMinAmanha = data.data[1].tMin;
            const tMaxAmanha = data.data[1].tMax;
            const dateAmanha = data.data[1].forecastDate;
            const precipitacaoAmanha = data.data[1].precipitaProb;
            document.getElementById('dateHoje-porto').innerHTML = dateHoje;
            document.getElementById('precipitacaoHoje-porto').innerHTML = precipitacaoHoje + '%';
            document.getElementById('tMinHoje-porto').innerHTML = tMinHoje + 'º';
            document.getElementById('tMaxHoje-porto').innerHTML = tMaxHoje + 'º';
            document.getElementById('dateAmanha-porto').innerHTML = dateAmanha;
            document.getElementById('precipitacaoAmanha-porto').innerHTML = precipitacaoAmanha + '%';
            document.getElementById('tMinAmanha-porto').innerHTML = tMinAmanha + 'º';
            document.getElementById('tMaxAmanha-porto').innerHTML = tMaxAmanha + 'º';
        });

});