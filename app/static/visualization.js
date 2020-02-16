
const visualization = (function() {

const isScriptLoaded = url => {
    var scripts = document.getElementsByTagName('script');
    for (var i = scripts.length; i--;) {
        if (scripts[i].src == url) return true;
    }
    return false;
}
const insert_script = async function (url) {
    if (isScriptLoaded(url)) return Promise.resolve();
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;
    const promise = new Promise((resolve, reject) => {
        script.onload = function() {
            resolve();
        }
    });
    head.appendChild(script);
    return promise;
}

const insert_scripts = async function () {
    const urls = [
        'https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js',
        'https://cdn.jsdelivr.net/npm/echarts-gl/dist/echarts-gl.min.js',
        'https://cdn.jsdelivr.net/npm/echarts-stat/dist/ecStat.min.js',
        'https://cdn.jsdelivr.net/npm/echarts/dist/extension/dataTool.min.js',
        'https://cdn.jsdelivr.net/npm/echarts/map/js/china.js',
        'https://cdn.jsdelivr.net/npm/echarts/map/js/world.js'
    ];
    for (let url of urls) {
        await insert_script(url);
    }
};

/**
 * data: {name, provinces}
 *   provices = [{name, value}]
 **/
const render_china_map = async function (containerId, data) {
    if (!data) {
        return;
    }
    const name = data.name;
    const provinces = data.provinces;

    if (!name || !provinces) {
        return;
    }

    const option = {
        tooltip: {},
        visualMap: {
            min: 0,
            max: 1500,
            left: 'left',
            top: 'bottom',
            text: ['High','Low'],
            seriesIndex: [0],
            inRange: {
                color: ['#e0ffff', '#006edd']
            },
            calculable : true
        },
        geo: {
            map: 'china',
            roam: true,
            label: {
                show: true,
                color: 'rgba(0,0,0,0.4)'
            },
            itemStyle: {
                borderColor: 'rgba(0, 0, 0, 0.2)'
            },
            emphasis:{
                itemStyle: {
                    areaColor: null,
                    shadowOffsetX: 0,
                    shadowOffsetY: 0,
                    shadowBlur: 20,
                    borderWidth: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        },
        series : [
            {
                name: name,
                type: 'map',
                geoIndex: 0,
                data: provinces
            }
        ]
    };

    await insert_scripts();
    const dom = document.getElementById(containerId);
    const myChart = echarts.init(dom);
    myChart.setOption(option, true);
    const resize = () => {
        dom.style.width = '80%';
        dom.style.height = '80%';
        myChart.resize();
    };
    window.addEventListener('resize', resize);
    setTimeout(resize, 1000);
};

return {render_china_map};

})();

window.visualization = visualization;
