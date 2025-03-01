
function toggleDropdown() {
    document.querySelector('.user-info').classList.toggle('active');
}

document.addEventListener('click', function(event) {
    var userInfo = document.querySelector('.user-info');
    if (!userInfo.contains(event.target)) {
        userInfo.classList.remove('active');
    }
});
