window.Utils = (function _() {

const post = (url, json) => {
    const req = new XMLHttpRequest();
    return new Promise((resolve, reject) => {
        req.onreadystatechange = function () {
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                resolve(JSON.parse(this.responseText)); 
            }
        };
        req.open('POST', url, true);
        req.setRequestHeader('Content-Type', 'application/json');
        req.send(JSON.stringify(json));
    });
}

const get = url => {
    const req = new XMLHttpRequest();
    return new Promise((resolve, reject) => {
        req.addEventListener('load', function () { resolve(JSON.parse(this.responseText)); });
        req.open('GET', url);
        req.send();
    });
};

const getCookie = name => {
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) return match[2];
}

const reload = force => {
    if (force === undefined) {
        force = true;
    }
    location.reload(force);
}

const getElementById = id => {
    const el = document.getElementById(id);
    if (!el) {
        throw new Event('no such id ' + id);
    }
    return el;
};
const getElementByTagNameAndId= (tagName, id) => {
    const el = getElementById(id);
    const currentTagName = el.tagName.toLowerCase();
    if (currentTagName !== (tagName + '').toLowerCase()) {
        throw new Event(`element with id ${id} has tagName ${currentTagName}, but ${tagName} is required`);
    }
    return el;
};

/**
 * Add multiple <option value="value">name</option> to the <select></select>
 **/
const setupSelect = (id, nameValues, callback) => {
    const select = getElementByTagNameAndId('select', id);
    const createOption = ({name, value}) => {
        const option = document.createElement('option');
        option.value = value;
        option.innerText = name;
        return option;
    };
    const options = (nameValues || []).map(createOption);
    options.forEach(option => {
        select.appendChild(option);
    });
    if (callback) {
        select.addEventListener('change', () => callback(select.value));
    }
};
const dateWithTimeZone = (timeZone, year, month, day, hour, minute, second) => {
    let date = new Date(Date.UTC(year, month, day, hour, minute, second));

    let utcDate = new Date(date.toLocaleString('en-US', { timeZone: "UTC" }));
    let tzDate = new Date(date.toLocaleString('en-US', { timeZone: timeZone }));
    let offset = utcDate.getTime() - tzDate.getTime();

    date.setTime(date.getTime() + offset);

    return date;
};
const dateFromAsiaSeconds = seconds => {
    const asiaTime = dateWithTimeZone('Asia/Shanghai', 1970, 0, 1, 0, 0, 0);
    asiaTime.setSeconds(seconds);
    return asiaTime;
};

/**
 * Example: getAttr(obj, 'a.b.c')
 **/
const getAttr = (obj, key) => {
    const keys = key.split('.');
    for (let k of keys) {
        if (obj === undefined || obj === null) {
            return null;
        }
        obj = obj[k];
    }
    return obj;
};

/**
 * An dict to [{key, value}]
 **/
const mapToPairs = map => {
    const pairs = [];
    for (let key in map) {
        pairs.push({key, value: map[key]});
    }
    return pairs;
};

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

const addCSS = cssStr => {
    cssStr = (cssStr || '').replace(/(\r\n|\n|\r)/gm, '')
    const styleSheet = document.createElement("style")
    styleSheet.type = "text/css"
    styleSheet.innerText = cssStr;
    document.head.appendChild(styleSheet)
};

const createElement = (tag, className, styles, options) => {
    const el = document.createElement(tag);
    el.className = className;
    for (let name in styles || {}) {
        el.style[name] = styles[name];
    }
    for (let name in options || {}) {
        el[name] = options[name];
    }
    return el;
};

const isEmptyValue = value => {
    return isNaN(value) || value === undefined || value === null;
};

const Utils = {
    post,
    get,
    getCookie,
    reload,
    getElementById,
    getElementByTagNameAndId,
    setupSelect,
    dateWithTimeZone,
    dateFromAsiaSeconds,
    getAttr,
    mapToPairs,
    isScriptLoaded,
    insert_script,
    addCSS,
    createElement,
    isEmptyValue
};

return Utils;

})();
