const toggleButton = document.querySelector('#container nav .toggle');

const navElement = document.querySelector('#container nav')

toggleButton.addEventListener('click', function() {
    navElement.classList.toggle('active');
})
