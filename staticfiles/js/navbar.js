const navList = document.querySelectorAll('.item');

function activeNav(event) {
    navList.forEach((item) => {item.classList.remove('active')});
    event.currentTarget.classList.add('active');
    console.log(event.currentTarget);
}

navList.forEach((item) => item.addEventListener('click', activeNav));
