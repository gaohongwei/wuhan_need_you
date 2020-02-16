
(function() {

const isScriptLoaded = url => {
    var scripts = document.getElementsByTagName('script');
    for (var i = scripts.length; i--;) {
        if (scripts[i].src == url) return true;
    }
    return false;
}
const insert_script = url => {
    if (isScriptLoaded(url)) return;
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.onload = function() {
        callFunctionFromScript();
    }
    script.src = url;
    head.appendChild(script);
}

const insert_scripts() {
    const urls = [
        'https://cdn.jsdelivr.net/npm/echarts/dist/echarts.min.js',
        'https://cdn.jsdelivr.net/npm/echarts-gl/dist/echarts-gl.min.js',
        'https://cdn.jsdelivr.net/npm/echarts-stat/dist/ecStat.min.js',
        'https://cdn.jsdelivr.net/npm/echarts/dist/extension/dataTool.min.js',
        'https://cdn.jsdelivr.net/npm/echarts/map/js/china.js',
        'https://cdn.jsdelivr.net/npm/echarts/map/js/world.js'
    ];
    urls.forEach(insert_script);
};

/**
 * data: {name, provinces}
 *   provices = [{name, value}]
 **/
const render_china_map = (containerId, data) => {
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
            seriesIndex: [1],
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

    insert_scripts();
    const dom = document.getElementById(containerId);
    const myChart = echarts.init(dom);
    const app = {};

    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
};

return {render_china_map};

})();

