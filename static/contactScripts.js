let enrollDiv = document.querySelector(".enroll");
let enrollP = enrollDiv.querySelector('p');
let enquireDiv = document.querySelector(".enquire");
let enquireP = enquireDiv.querySelector('p');
let enrollForm = document.querySelector(".form1");
let enquireForm = document.querySelector(".form2");

enrollDiv.addEventListener('click', function () {
    console.log(enrollP);
    if (!enrollDiv.classList.contains('clicked')) {
        enrollDiv.classList.add('clicked');
        enrollP.style.color = 'var(--linear-green2)';
        enrollForm.style.display = 'grid';
    } 
    enquireDiv.classList.remove('clicked');
    enquireP.style.color = 'white';
    enquireForm.style.display = 'none';
});

enquireDiv.addEventListener('click', function () {
    if (!enquireDiv.classList.contains('clicked')) {
        enquireDiv.classList.add('clicked');
        enquireP.style.color = 'var(--linear-green2)';
        enquireForm.style.display = 'grid';
    } 
    enrollDiv.classList.remove('clicked');
    enrollP.style.color = 'white';
    enrollForm.style.display = 'none';
});