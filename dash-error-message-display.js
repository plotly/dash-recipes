var errorId = 'error-message-container'
var body = document.getElementsByTagName('body')[0]
var newNode = document.createElement('div');
newNode.setAttribute('id', errorId);
body.appendChild(newNode);

console.warn('adding window.onerror');
window.onerror = function(msg, url, line, col, error) {
    var errorElement = document.getElementById(errorId);
    console.warn('window.onerror', msg);
    errorElement.innerHtml = ([
        '<div>',
            '<hr/>',
            '<div style="font-size: 14px;">Error occurred!</div>',
            '<pre style="color: #FF4136">',
            error,
            '</pre>',
        '</div>'
    ].join(''));
};
