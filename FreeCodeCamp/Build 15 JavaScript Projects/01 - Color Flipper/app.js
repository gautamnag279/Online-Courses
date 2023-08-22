function getRandomnColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function onClick() {
  document.body.style.backgroundColor = getRandomnColor();
  color.textContent = getRandomnColor();
}

const color = document.querySelector(".color");
btn.addEventListener("click", onClick);
