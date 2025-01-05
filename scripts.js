
// scripts.js
let currentSlideIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

// Function to move to the next or previous slide
function moveSlide(direction) {
    // Remove active class from the current slide
    slides[currentSlideIndex].classList.remove('active');
    slides[currentSlideIndex].classList.add('inactive'); // Make current slide inactive

    // Update the current slide index
    currentSlideIndex = (currentSlideIndex + direction + totalSlides) % totalSlides;

    // Add active class to the new slide
    slides[currentSlideIndex].classList.remove('inactive');
    slides[currentSlideIndex].classList.add('active');
}

// Initialize the first slide as active
window.onload = function() {
    slides[currentSlideIndex].classList.add('active');
};
