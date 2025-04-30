/* Work by Iqra Shah (1973224)*/

// Typing Effect Code
const texts = ["Welcome to your dashboard!"];
const typingTarget = document.getElementById("typing-text");
const cursor = document.getElementById("cursor");
let index = 0;
let textIndex = 0;
let isDeleting = false;

function typeLoop() {
    const currentText = texts[textIndex];
    if (!isDeleting && index <= currentText.length) {
        typingTarget.textContent = currentText.substring(0, index);
        index++;
        setTimeout(typeLoop, 100);
    } else if (isDeleting && index >= 0) {
        typingTarget.textContent = currentText.substring(0, index);
        index--;
        setTimeout(typeLoop, 50);
    } else {
        isDeleting = !isDeleting;
        if (!isDeleting && index === 0) {
            textIndex = (textIndex + 1) % texts.length;
        }
        setTimeout(typeLoop, 1000);
    }
}
setInterval(() => {
    cursor.style.opacity = cursor.style.opacity === '0' ? '1' : '0';
}, 500);
window.onload = typeLoop;



// Button Star Animation Code
const button = document.querySelector(".left-container button");
let stars = [];
button.addEventListener("mouseover", () => {
    removeStars();
    for (let i = 0; i < 5; i++) {
        let star = document.createElement("div");
        star.classList.add("stars");
        if (Math.random() > 0.5) star.classList.add("large");
        document.body.appendChild(star);

        let buttonRect = button.getBoundingClientRect();
        let startX = Math.random() * buttonRect.width + buttonRect.left;
        let startY = Math.random() * buttonRect.height + buttonRect.top;
        
        star.style.left = `${startX}px`;
        star.style.top = `${startY}px`;

        setTimeout(() => {
            let angle = Math.random() * 2 * Math.PI;
            let distance = Math.random() * 150 + 50;
            let moveX = Math.cos(angle) * distance;
            let moveY = Math.sin(angle) * distance;

            star.style.transition = "transform 1s ease-out, opacity 1s ease-in-out";
            star.style.transform = `rotate(45deg) translate(${moveX}px, ${moveY}px)`;
            star.style.opacity = "0";
        }, 50);
        stars.push(star);
    }
});
button.addEventListener("mouseleave", () => {
    removeStars();
});
function removeStars() {
    stars.forEach(star => {
        star.style.opacity = "0";
        setTimeout(() => star.remove(), 1000);
    });
    stars = [];
}
