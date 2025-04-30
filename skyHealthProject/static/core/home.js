//Work by Iqra Shah (1973224)
const text = "Health Check!";
const typingTarget = document.getElementById("typing-text");
const cursor = document.getElementById("cursor");
let index = 0;
let isDeleting = false;

function typeLoop() {
    if (!isDeleting && index <= text.length) {
        typingTarget.textContent = text.substring(0, index);
        index++;
        setTimeout(typeLoop, 100);
    } else if (isDeleting && index >= 0) {
        typingTarget.textContent = text.substring(0, index);
        index--;
        setTimeout(typeLoop, 50);
    } else {
        isDeleting = !isDeleting;
        setTimeout(typeLoop, 1000);
    }
}

setInterval(() => {
    cursor.style.opacity = cursor.style.opacity === '0' ? '1' : '0';
}, 500);

window.onload = typeLoop;
