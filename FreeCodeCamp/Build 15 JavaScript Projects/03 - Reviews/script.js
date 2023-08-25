const reviews = [
    {
        id: 1,
        name: "Leslie Jones",
        job: "Fashion Model",
        img: "images/person1.jpg",
        text: "This is the best Models agency . The time I have spent there just changed my life in the best way of it. Met a lot of people there who came from all over the world."
    },
    {
        id: 2,
        name: "Mason Blush",
        job: "Software Engineer",
        img: "images/person2.jpg",
        text: "Best place to work. Awesome work environment, good company culture and benefits (free cabs & 1 time meals). Supportive management and colleagues. Flexible and good work life balance."
    },
    {
        id: 3,
        name: "Geroge Brown",
        job: "Prison Inmate",
        img: "images/person3.jpg",
        text: "Over 2 decades of gospel driven work to serve the destitute, feed, equip and enable them to save this fallen world"
    },
    {
        id: 4,
        name: "Eva Jacobs",
        job: "Masseuse",
        img: "images/person4.jpg",
        text: "I had a relaxed and a rejuvenating time at the Tattva Spa. Highly recommend the staff as they are well spoken and trained. Correct guidance is given along with a warm treatment."
    },
    {
        id: 5,
        name: "Tyrell Hanna",
        job: "Drug Dealer",
        img: "images/person5.jpg",
        text: "Almost all types of Drugs are available and the owner is very polite, helpful and experience. The drug store is just close to my kids play school and bus stop."
    },
]

const img = document.querySelector("#person-img");
const author = document.querySelector("#author");
const job = document.querySelector("#job");
const info = document.querySelector("#info");

const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
const randomBtn = document.querySelector(".random-btn");

let currItem = 0

window.addEventListener('DOMContentLoaded', function () {
    updatePage();
})

function updatePage() {
    const item = reviews[currItem];
    img.src = item.img;
    author.textContent = item.name;
    job.textContent = item.job;
    info.textContent = item.text;
}

prevBtn.addEventListener('click', function () {
    currItem--;
    if (currItem < 0) {
        currItem = 4;
    }
    updatePage();

})

nextBtn.addEventListener('click', function () {
    currItem++;
    if (currItem > 4) {
        currItem = 0;
    }
    updatePage();
})

randomBtn.addEventListener('click', function () {
    currItem = Math.floor(Math.random() * 5);
    updatePage();
})