var Canvas = document.getElementById('canvas');
var ctx = Canvas.getContext('2d');

var resize = function() {
    Canvas.width = Canvas.clientWidth;
    Canvas.height = Canvas.clientHeight;
};
window.addEventListener('resize', resize);
resize();

var elements = [];
var presets = {};

// 画像の読み込み
var image = new Image();
image.src = 'https://a1.x0.com/NEN/image/logo321.png'; // 画像ファイルのパスを指定

presets.o = function (x, y, s, dx, dy, maxDistance) {
    var distanceTraveled = 0;
    var angle = 0;
    var rotationSpeed = Math.random() * 0.01 - 0.005; // ランダムな回転速度
	var alpha = Math.random() * 0.3 + 0.05; // 透過度（0.5〜1の範囲）
	
    return {
        x: x,
        y: y,
        s: s,
        dx: dx,
        dy: dy,
        draw: function(ctx) {
            // 位置の更新
            this.x += this.dx;
            this.y += this.dy;
            distanceTraveled += Math.sqrt(this.dx * this.dx + this.dy * this.dy);

            // 移動距離が最大値に達した場合、方向を反転
            if (distanceTraveled >= maxDistance) {
                this.dx = -this.dx;
                this.dy = -this.dy;
                distanceTraveled = 0;
            }

            // 角度の更新
            angle += rotationSpeed;

			// 透過度の設定
            ctx.globalAlpha = alpha;

            // 画像の回転描画
            ctx.save();
            ctx.translate(this.x + image.width * this.s / 2, this.y + image.height * this.s / 2);
            ctx.rotate(angle);
            ctx.drawImage(image, -image.width * this.s / 2, -image.height * this.s / 2, image.width * this.s, image.height * this.s);
            ctx.restore();
			
			// 透過度をリセット
            ctx.globalAlpha = 1.0; // 他の描画に影響が出ないように
        }
    }
};

for(var x = 0; x < Canvas.width; x++) {
    for(var y = 0; y < Canvas.height; y++) {
        if(Math.round(Math.random() * 28000) == 1) {
            var s = ((Math.random() * 6) + 3) / 50;
            var dx = (Math.random() - 0.5) / 6; // X方向の速度
            var dy = (Math.random() - 0.5) / 6; // Y方向の速度
            var maxDistance = Math.random() * 100 + 50; // 最大移動距離
            elements.push(presets.o(x, y, s, dx, dy, maxDistance));
        }
    }
}

setInterval(function() {
    ctx.clearRect(0, 0, Canvas.width, Canvas.height);

    var time = new Date().getTime();
    for (var e in elements)
    elements[e].draw(ctx, time);
}, 10);
/*
for(var x = 0; x < Canvas.width; x++) {
    for(var y = 0; y < Canvas.height; y++) {
        if(Math.round(Math.random() * 22000) == 1) {
            var s = ((Math.random() * 3) + 1) / 50;
            var dx = (Math.random() - 0.5) / 4; // X方向の速度
            var dy = (Math.random() - 0.5) / 4; // Y方向の速度
            elements.push(presets.o(x, y, s, dx, dy));
        }
    }
}

*/
