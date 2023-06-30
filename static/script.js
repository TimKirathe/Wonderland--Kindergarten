let slides = document.querySelector("[data-slides]")
const arrayOfSlides = [...slides.children]
let index = 0


setInterval(function () {
    changePhotos();
}, 2000);

function changePhotos() {
    let activeSlide = slides.querySelector("[data-active]")
    index = index + 1;
    console.log(index)

    if (index > arrayOfSlides.length - 1) {
        console.log("hi");
        index = 0;
    }

    delete activeSlide.dataset.active
    slides.children[index].dataset.active = true;
}

