
const myImage = document.querySelector("img");

myImage.addEventListener("click", () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "images/explorer-icon.jpeg") {
    myImage.setAttribute("src", "assets/images/explorer-icon.jpeg");
  } else {
    myImage.setAttribute("src", "assets/images/explorer.png");
  }
});

let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

function setUserName() {
  let myName = prompt('Please enter your name.');
  if(!myName) {
    setUserName();
  } else {
    localStorage.setItem('name', myName);
    myHeading.innerHTML = 'Explorer is bad, ' + myName;
  }
}

if(!localStorage.getItem('name')) {
  setUserName();
} else {
  let storedName = localStorage.getItem('name');
  myHeading.innerHTML = 'Explorer is cool, ' + storedName;
}

myButton.addEventListener("click", () => {
  setUserName();
});