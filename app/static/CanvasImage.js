
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

const CanvasImage = (function _() {
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
            fillBackground(canvas, 'black');
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
    };

    return {register, carousel_bootstrap4};
})();

window.CanvasImage = CanvasImage;
