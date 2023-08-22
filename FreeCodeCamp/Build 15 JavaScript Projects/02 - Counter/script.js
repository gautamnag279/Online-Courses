const displayElement = document.querySelector('h3');
const buttonsContainer = document.querySelector('.buttons');
let count = 0;

buttonsContainer.addEventListener('click', (event) => {
    const clickedButton = event.target;
    if (clickedButton.classList.contains('decrease')) {
        count--;
    } else if (clickedButton.classList.contains('reset')) {
        count = 0;
    } else if (clickedButton.classList.contains('increase')) {
        count++;
    }

    displayElement.textContent = count;
});
