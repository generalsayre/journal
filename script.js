function showTime() {
	document.getElementById('currentTime').innerHTML = new Date().toUTCString();
}
showTime();
setInterval(function () {
	showTime();
}, 1000);

const button = document.getElementById('myButton');
const background = document.getElementById('myBackground');

button.addEventListener('click', () => {
  background.style.backgroundImage = 'url(\'https://wallpapers.com/images/hd/plain-black-desktop-2560-x-1440-ugpl0479gu0vuwnl.jpg\')'; // 
});