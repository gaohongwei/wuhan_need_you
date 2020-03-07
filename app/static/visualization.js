
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
 * Create pieces for echarts visualMap
 * values: an array of any format. 
 *         If the elements are numbers, mapper can be null,
 *         or the mapper should be provided to get an array of numbers
 * numPieces: how many pieces
 * mapper: map the element to a number [optional if the values are numbers]
 * */
const createPieces = (values, numPieces, mapper) => {
    mapper = mapper || (i => i);
    let cmp = (i, j) => {i = mapper(i); j = mapper(j); return (i > j) ? 1 : (i < j ? -1 : 0)};
    values = values.sort(cmp);
    const numPerPiece = Math.floor(values.length / numPieces);
    const createPiece = i => {
        const beg = values[i * numPerPiece];
        const end = values[i * numPerPiece + numPerPiece - 1];
        const min = mapper(beg);
        let max = mapper(end);
        if (i === numPieces - 1) {
            max = mapper(values[values.length - 1]);
        }
        return {min, max};
    };
    const pieces = new Array(numPieces).fill().map((_, i) => createPiece(i));
    const min = mapper(values[0]);
    const max = mapper(values[values.length - 2]); // ignore the max
    return {pieces, min, max};
};

const world_country_name_map = {
    'Palau': '帕劳',
    'Singapore':'新加坡',
    'Dominican Rep.':'多米尼加',
    'Palestine':'巴勒斯坦',
    'Bahamas':'巴哈马',
    'Timor-Leste':'东帝汶',
    'Afghanistan':'阿富汗',
    'Guinea-Bissau':'几内亚比绍',
    "Côte d'Ivoire":'科特迪瓦',
    'Siachen Glacier':'锡亚琴冰川',
    "Br. Indian Ocean Ter.":'英属印度洋领土',
    'Angola':'安哥拉',
    'Albania':'阿尔巴尼亚',
    'United Arab Emirates':'阿联酋',
    'Argentina':'阿根廷',
    'Armenia':'亚美尼亚',
    'French Southern and Antarctic Lands':'法属南半球和南极领地',
    'Australia':'澳大利亚',
    'Austria':'奥地利',
    'Azerbaijan':'阿塞拜疆',
    'Burundi':'布隆迪',
    'Belgium':'比利时',
    'Benin':'贝宁',
    'Burkina Faso':'布基纳法索',
    'Bangladesh':'孟加拉国',
    'Bulgaria':'保加利亚',
    'The Bahamas':'巴哈马',
    'Bosnia and Herz.':'波斯尼亚和黑塞哥维那',
    'Belarus':'白俄罗斯',
    'Belize':'伯利兹',
    'Bermuda':'百慕大',
    'Bolivia':'玻利维亚',
    'Brazil':'巴西',
    'Brunei':'文莱',
    'Bhutan':'不丹',
    'Botswana':'博茨瓦纳',
    'Central African Rep.':'中非',
    'Canada':'加拿大',
    'Switzerland':'瑞士',
    'Chile':'智利',
    'China':'中国',
    'Ivory Coast':'象牙海岸',
    'Cameroon':'喀麦隆',
    'Dem. Rep. Congo':'刚果民主共和国',
    'Congo':'刚果',
    'Colombia':'哥伦比亚',
    'Costa Rica':'哥斯达黎加',
    'Cuba':'古巴',
    'N. Cyprus':'北塞浦路斯',
    'Cyprus':'塞浦路斯',
    'Czech Rep.':'捷克',
    'Germany':'德国',
    'Djibouti':'吉布提',
    'Denmark':'丹麦',
    'Algeria':'阿尔及利亚',
    'Ecuador':'厄瓜多尔',
    'Egypt':'埃及',
    'Eritrea':'厄立特里亚',
    'Spain':'西班牙',
    'Estonia':'爱沙尼亚',
    'Ethiopia':'埃塞俄比亚',
    'Finland':'芬兰',
    'Fiji':'斐',
    'Falkland Islands':'福克兰群岛',
    'France':'法国',
    'Gabon':'加蓬',
    'United Kingdom':'英国',
    'Georgia':'格鲁吉亚',
    'Ghana':'加纳',
    'Guinea':'几内亚',
    'Gambia':'冈比亚',
    'Guinea Bissau':'几内亚比绍',
    'Eq. Guinea':'赤道几内亚',
    'Greece':'希腊',
    'Greenland':'格陵兰',
    'Guatemala':'危地马拉',
    'French Guiana':'法属圭亚那',
    'Guyana':'圭亚那',
    'Honduras':'洪都拉斯',
    'Croatia':'克罗地亚',
    'Haiti':'海地',
    'Hungary':'匈牙利',
    'Indonesia':'印度尼西亚',
    'India':'印度',
    'Ireland':'爱尔兰',
    'Iran':'伊朗',
    'Iraq':'伊拉克',
    'Iceland':'冰岛',
    'Israel':'以色列',
    'Italy':'意大利',
    'Jamaica':'牙买加',
    'Jordan':'约旦',
    'Japan':'日本',
    'Kazakhstan':'哈萨克斯坦',
    'Kenya':'肯尼亚',
    'Kyrgyzstan':'吉尔吉斯斯坦',
    'Cambodia':'柬埔寨',
    'Korea':'韩国',
    'Kosovo':'科索沃',
    'Kuwait':'科威特',
           'Lao PDR':'老挝',
           'Lebanon':'黎巴嫩',
           'Liberia':'利比里亚',
           'Libya':'利比亚',
           'Sri Lanka':'斯里兰卡',
           'Lesotho':'莱索托',
           'Lithuania':'立陶宛',
           'Luxembourg':'卢森堡',
           'Latvia':'拉脱维亚',
           'Morocco':'摩洛哥',
           'Moldova':'摩尔多瓦',
           'Madagascar':'马达加斯加',
           'Mexico':'墨西哥',
           'Macedonia':'马其顿',
           'Mali':'马里',
           'Myanmar':'缅甸',
           'Montenegro':'黑山',
           'Mongolia':'蒙古',
           'Mozambique':'莫桑比克',
           'Mauritania':'毛里塔尼亚',
           'Malawi':'马拉维',
           'Malaysia':'马来西亚',
           'Namibia':'纳米比亚',
           'New Caledonia':'新喀里多尼亚',
           'Niger':'尼日尔',
           'Nigeria':'尼日利亚',
           'Nicaragua':'尼加拉瓜',
           'Netherlands':'荷兰',
           'Norway':'挪威',
           'Nepal':'尼泊尔',
           'New Zealand':'新西兰',
           'Oman':'阿曼',
           'Pakistan':'巴基斯坦',
           'Panama':'巴拿马',
           'Peru':'秘鲁',
           'Philippines':'菲律宾',
           'Papua New Guinea':'巴布亚新几内亚',
           'Poland':'波兰',
           'Puerto Rico':'波多黎各',
           'Dem. Rep. Korea':'朝鲜',
           'Portugal':'葡萄牙',
           'Paraguay':'巴拉圭',
           'Qatar':'卡塔尔',
           'Romania':'罗马尼亚',
           'Russia':'俄罗斯',
           'Rwanda':'卢旺达',
           'W. Sahara':'西撒哈拉',
           'Saudi Arabia':'沙特阿拉伯',
           'Sudan':'苏丹',
           'S. Sudan':'南苏丹',
           'Senegal':'塞内加尔',
           'Solomon Is.':'所罗门群岛',
           'Sierra Leone':'塞拉利昂',
           'El Salvador':'萨尔瓦多',
           'Somaliland':'索马里兰',
           'Somalia':'索马里',
           'Serbia':'塞尔维亚',
           'Suriname':'苏里南',
           'Slovakia':'斯洛伐克',
           'Slovenia':'斯洛文尼亚',
           'Sweden':'瑞典',
           'Swaziland':'斯威士兰',
           'Syria':'叙利亚',
           'Chad':'乍得',
           'Togo':'多哥',
           'Thailand':'泰国',
           'Tajikistan':'塔吉克斯坦',
           'Turkmenistan':'土库曼斯坦',
           'East Timor':'东帝汶',
           'Trinidad and Tobago':'特里尼达和多巴哥',
           'Tunisia':'突尼斯',
           'Turkey':'土耳其',
           'Tanzania':'坦桑尼亚',
           'Uganda':'乌干达',
           'Ukraine':'乌克兰',
           'Uruguay':'乌拉圭',
           'United States':'美国',
           'Uzbekistan':'乌兹别克斯坦',
           'Venezuela':'委内瑞拉',
           'Vietnam':'越南',
           'Vanuatu':'瓦努阿图',
           'West Bank':'西岸',
           'Yemen':'也门',
           'South Africa':'南非',
           'Zambia':'赞比亚',
           'Zimbabwe':'津巴布韦'
        };

/**
 * data: {name, items, time, title}
 *   provices = [{name, value}]
 * map: china or world
 **/
const render_map = async function (containerId, data, map='china') {
    if (!data) {
        return;
    }
    const name = data.name;
    const items = data.items;
    const time = data.time;
    let title = data.title || '';
    if (time) {
        title += `${time}`;
    }

    if (!name || !items) {
        return;
    }

    // const min = Math.min(...items.map(i => i.value));
    // const max = Math.max(...items.map(i => i.value));

    const option = {
        title: {
            text: title,
            borderColor: '#c00',
            left: 'center',
            x: 'center',
            show: true,
            textStyle: {
                fontSize: 16,
                fontWeight: 'bolder',
                color: '#000'
            }
        },
        tooltip: {
            trigger: 'item',
            formatter: params => {
                const {name, seriesName, value} = params;
                return (Utils.isEmptyValue(value)) ? '' : `${name}<br/>${seriesName}: ${value}`;
            }
        },
        visualMap: {
            ...createPieces(items, 4, i => parseFloat(i.value)),
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
            map: map,
            roam: true,
            label: {
                normal: {
                    show: map !== 'world', // by default the world map not show country name
                    color: 'rgba(0,0,0,0.4)'
                }
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
                data: items
            }
        ]
    };

    if (map === 'world') {
        option.geo.nameMap = world_country_name_map;
    }

    await insert_scripts();
    const dom = document.getElementById(containerId);
    const myChart = echarts.init(dom);
    myChart.setOption(option);

    const camera = {zoom: undefined, center: undefined};
    const zoomThresholdForLabel = 3;
    myChart.on('georoam', () => {
        let {zoom, center} = myChart.getOption().geo[0];
        camera.zoom = zoom;
        camera.center = center;
        refresh();
    });
    const refresh = () => {
        option.geo.label.normal.show = camera.zoom > zoomThresholdForLabel;
        myChart.setOption(option); // refresh
    };
    const resize = () => {
        dom.style.width = '80%';
        dom.style.height = '80%';
        myChart.resize();
    };
    window.addEventListener('resize', resize);
    setTimeout(resize, 1000);
};

return {render_map, world_country_name_map};

})();

window.visualization = visualization;
