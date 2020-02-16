
/**
 * A canvas based carousel, the images will be auto-scaled
 * Usage:
    <head>
        <script src='./CanvasImage.js'></script>
	    <script type="text/javascript" src="jQuery.js"></script>
	    <script type="text/javascript" src="bootstrap-4.4.1-dist/js/bootstrap.min.js"></script>
	    <script type="text/javascript" src="bootstrap-4.4.1-dist/js/bootstrap.bundle.js"></script>
	    <link rel="stylesheet" href="bootstrap-4.4.1-dist/css/bootstrap-grid.css">
	    <link rel="stylesheet" href="bootstrap-4.4.1-dist/css/bootstrap.min.css">
    </head>
    <body>
        <div id="carousel"/>
        <canvas class="canvas-image" width="800" height="600" data-src="./test.jpg"></canvas>
    <script>
        const urls = ['./test2.jpg', './test.jpg'];
        const canvasClass = 'd-block w-100 h-80';
        document.body.onload = () => {
            CanvasImage.carousel_bootstrap4('carousel', urls, '600px');
            CanvasImage.register();
        };
    </script>
    </body>
 **/

const SlideShow = (function _() {
    const fillBackground = (canvas, color) => {
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;
        ctx.beginPath();
        ctx.rect(0, 0, width, height);
        ctx.fillStyle = color;
        ctx.fill();

    };
    const fillCanvasInParent = canvas => {
        const parent = canvas.parentNode;
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.width = parent.offsetWidth || parentWidth;
        canvas.height = parent.offsetHeight || parentHeight;
    };
    let parentWidth = 0;
    let parentHeight = 0;
    const drawImageInCenter = (canvas, image) => {
        const srcWidth = image.width;
        const srcHeight = image.height;
        const srcRatio = srcWidth / srcHeight;
        const width = canvas.width;
        const height = canvas.height;
        const ratio = width / height;
        let x = 0, y = 0, dw = width , dh = height;
        if (srcRatio > ratio) {
            x = 0;
            dw = width;
            dh = width / srcRatio;
            y = (height - dh) * 0.5;
        } else {
            y = 0;
            dh = height;
            dw = height * srcRatio;
            x = (width - dw) * 0.5;
        }
        const ctx = canvas.getContext('2d');
        if (isNaN(x) || isNaN(y) || isNaN(dw) || isNaN(dh)) {
            console.log(srcWidth, srcHeight);
            console.log(width, height);
            console.log(x,y,dw,dh);
            return;
        }
        console.log(srcWidth, srcHeight);
        console.log(width, height);
        console.log(x,y,dw,dh);
        console.log(image);
        ctx.drawImage(image, x, y, dw, dh);
    };
    const doWhenParentVisible = (elem, maxTry, callback) => {
        if (parentWidth !== 0) {
            callback();
            return;
        }
        if (maxTry === 0) return;
        if (!callback) return;
        const parent = elem.parentNode;
        if (!parent) {
            console.error('null parent');
            return;
        }
        if (!parent.offsetWidth) {
            setTimeout(() => doWhenParentVisible(elem, maxTry-1, callback), 5);
        } else {
            parentWidth = parent.offsetWidth;
            parentHeight = parent.offsetHeight;
            callback();
        }
    };
    const renderCanvas = (canvas, img) => {
        if (img) {
            fillCanvasInParent(canvas);
            fillBackground(canvas, '#a9acaf');
            drawImageInCenter(canvas, img);
        } else {
            const src = canvas.dataset.src;
            appendInvisibleImage(canvas, src);
        }
    };
    const appendInvisibleImage = (canvas, src) => {
        const div = document.createElement('div');
        const img = document.createElement('img');
        div.style.display = 'none';
        div.appendChild(img);
        img.src = src;
        img.addEventListener('load', e => {
            console.log(src);
            doWhenParentVisible(canvas, 5, () => {
                renderCanvas(canvas, img);
                div.removeChild(img);
            });
        });
        canvas.parentNode.insertBefore(div, canvas.nextSibling);
        return img;
    };
    const register = () => {
        const canvases = document.querySelectorAll('canvas.canvas-image');
        for(let canvas of canvases) {
            const src = canvas.dataset.src;
            if (src) {
                appendInvisibleImage(canvas, src);
            }
        }
    };

    const carousel_bootstrap4 = (divId, img_urls, height) => {
        height = height || '600px';
        const id = 'carouselExampleIndicators';
        const div3 = document.getElementById(divId);
        div3.className = 'carousel slide';
        div3.dataset.ride = 'carousel';
        const ol = document.createElement('ol');
        ol.className = 'carousel-indicators';
        const createLi = (id, i) => {
            const li = document.createElement('li');
            const className = i === 0 ? 'active' : '';
            li.className = className;
            li.dataset['slideTo'] = i;
            li.dataset.target = '#' + id;
            return li;
        };
        for (let i=0; i<img_urls.length; ++i) {
            const li = createLi(divId, i);
            ol.appendChild(li);
        };
        const div4 = document.createElement('div');
        div4.className = 'carousel-inner';
        const createItem = (url, i) => {
            const div = document.createElement('div');
            const className = i === 0 ? 'carousel-item active' : 'carousel-item';
            div.className = className;
            div.style.height = height;
            const canvas = document.createElement('canvas');
            canvas.className = 'canvas-image d-block w-100';
            canvas.dataset.src = url;
            div.appendChild(canvas);
            window.addEventListener('resize', () => renderCanvas(canvas));
            return div;
        };
        for (let i=0; i<img_urls.length; ++i) {
            const url = img_urls[i];
            const div = createItem(url, i);
            div4.appendChild(div);
        }
        const createButton = (slide, text, id) => {
            const a = document.createElement('a');
            a.className = 'carousel-control-' + slide;
            a.role = 'button';
            a.dataset.slide = slide;
            a.href = '#' + id;
            const span1 = document.createElement('span');
            span1.className = 'carousel-control-' + slide + '-icon';
            span1.setAttribute('aria-hidden', 'true');
            a.appendChild(span1);
            const span2 = document.createElement('span');
            span2.className = 'sr-only';
            span2.innerText = text;
            a.appendChild(span2);
            return a;
        };
        const a1 = createButton('prev', 'Previous', divId);
        const a2 = createButton('next', 'Next', divId);
        div3.appendChild(ol);
        div3.appendChild(div4);
        div3.appendChild(a1);
        div3.appendChild(a2);
        register();
        // a hack to solve not-auto-playing
        setTimeout(() => a2.click(), 2000);
    };

    const slideCSS = `
* {box-sizing: border-box;}
body {font-family: Verdana, sans-serif;}
.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: white;
  font-size: 20px;
  padding: 8px 12px;
  position: absolute;
  margin-left: 10px;
  bottom: 18px;
  width: 100%;
  text-align: left;
}

/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active_1 {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}
    `;
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
    const playSlide = (id, index) => {
        index = index || 0;
        const elem = document.getElementById(id);
        if (!elem) {
            return;
        }
        const slides = elem.querySelectorAll(".mySlides");
        if (!slides || slides.length == 0) {
            return;
        }
        if (index >= slides.length) {
            index = index % slides.length;
        }
        const dots = elem.querySelectorAll('.dot');
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = i === index ? 'block' : 'none';  
        }
        for (let i = 0; i < dots.length; i++) {
            if (i !== index) {
                dots[i].className = dots[i].className.replace(" active_1", "");
            } else {
                dots[i].className += " active_1";
            }
        }
    };
    const setDataSet = (id, key, value) => {
        const elem = document.getElementById(id);
        if (!elem) {
            return
        }
        elem.dataset[key] = value;
    };
    const getDataSet = (id, key) => {
        const elem = document.getElementById(id);
        if (!elem) {
            return null;
        }
        return elem.dataset[key];
    };
    const playSlides = (id, index, period) => {
        index = index || 0;
        console.log('playSlides: ', id, index, period);
        period = period || 2000; // default 2 seconds
        let currentIndex = index;
        const play = () => {
            playSlide(id, currentIndex);
            currentIndex = currentIndex + 1;
        };
        let handle = parseInt(getDataSet(id, 'slide'));
        if (handle) {
            clearInterval(handle);
        }
        handle = setInterval(play, period);
        setDataSet(id, 'slide', handle);
    };
    const stopSlides = slideHandle => {
        clearInterval(slideHandle);
    };
    const showSlides = (id, imgUrls) => {
        const createImageDiv = (imgUrl, text) => {
            const div = createElement('div', 'mySlides fade');
            const img = createElement('img', '', {width: '100%', height: '5%'}, {src: imgUrl});
            const div2 = createElement('div', 'text', {});
            div2.innerText = text || '';
            div.appendChild(img);
            div.appendChild(div2);
            return div;
        };
        const _createImageDiv = item => {
            if (!item) {
                return null;
            }
            if (item instanceof String || typeof(item) === 'string') {
                return createImageDiv(item);
            } else {
                const imgUrl = item.imgUrl;
                const title = item.title;
                return !!imgUrl ? createImageDiv(imgUrl, title) : null;
            }
        };
        const div1 = createElement('div', 'row');
        const div2 = createElement('div', 'col-md-12 col-lg-12 col-xl-12 jumbotron', {padding: 0});
        const div3 = createElement('div', '', {'margin-left': '0em', 'margin-right': '0em'});
        const div4 = createElement('div', 'slideshow-container', {'max-width': '100%'});
        const div5 = createElement('div', '', {'text-align': 'center', 'background-color': 'white'});
        imgUrls = imgUrls || [];
        const imgDivs = imgUrls.map(_createImageDiv).filter(i => !!i);
        imgDivs.forEach(div => {
            div4.appendChild(div);
        });
        imgDivs.forEach((div, i) => {
            const dot = createElement('span', 'dot');
            dot.addEventListener('click', () => {
                playSlides(id, i);
            })
            div5.appendChild(dot);
        });
        div4.appendChild(div5);
        div3.appendChild(div4);
        div2.appendChild(div3);
        div1.appendChild(div2);
        addCSS(slideCSS);
        const container = document.getElementById(id);
        container.appendChild(div1);
        playSlides(id);
    };

    return {register, carousel_bootstrap4, showSlides};
})();

window.SlideShow = SlideShow;
