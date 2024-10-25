// デバッグコンソールの要素取得
const debugConsole = document.getElementById('debug-console');
const debugHeader = document.querySelector('.debug-header');
const debugContent = document.getElementById('debug-content');
const expandButton = document.getElementById('expand-debug');
const closeButton = document.getElementById('close-debug');

// フローティングウィンドウを表示する関数
function showDebugConsole() {
  debugConsole.style.display = 'block';
}

// フローティングウィンドウを閉じる
closeButton.addEventListener('click', () => {
  debugConsole.style.display = 'none';
});

// ウィンドウサイズの切り替え
expandButton.addEventListener('click', () => {
  debugConsole.style.right  = `10px`;
  debugConsole.style.bottom = `10px`;
  debugConsole.style.inset = ``;
  debugConsole.classList.toggle('small');
  debugConsole.classList.toggle('large');
  expandButton.textContent = debugConsole.classList.contains('large') ? '⬇' : '⬆';
});

// ドラッグ移動
let isDragging = false;
let offsetX, offsetY;

debugHeader.addEventListener('mousedown', (e) => {
  isDragging = true;
  offsetX = e.clientX - debugConsole.offsetLeft;
  offsetY = e.clientY - debugConsole.offsetTop;
  document.addEventListener('mousemove', dragDebugConsole);
  document.addEventListener('mouseup', stopDragDebugConsole);
});

function dragDebugConsole(e) {
  if (isDragging) {
    debugConsole.style.left = `${e.clientX - offsetX}px`;
    debugConsole.style.top = `${e.clientY - offsetY}px`;
  }
}

function stopDragDebugConsole() {
  isDragging = false;
  document.removeEventListener('mousemove', dragDebugConsole);
  document.removeEventListener('mouseup', stopDragDebugConsole);
}

// デバッグ表示
function logDebugMessage(message) {
  const timestamp = new Date().toLocaleString();

  // オブジェクトならJSON.stringify()を使って整形
  if (typeof message === 'object') {
      message = JSON.stringify(message, null, 2);
  }

  debugContent.innerHTML += `<strong>[${timestamp}]</strong> ${message}<br />`;
  debugContent.scrollTop = debugContent.scrollHeight; // 常に最新メッセージを表示
}

// ページ読み込み時にデバッグコンソールを表示
document.addEventListener('DOMContentLoaded', showDebugConsole);
