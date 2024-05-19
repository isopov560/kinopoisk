let theme = false

const btnChangeTheme = document.querySelector('.btnChangeTheme')
const body = document.querySelector('body')
btnChangeTheme.addEventListener('click', function () {
	if (theme == false) {
		btnChangeTheme.setAttribute('src', '/static/Core/img/sun.png');
		body.setAttribute('data-bs-theme', 'light');
		theme = true
	}
	else {
		btnChangeTheme.setAttribute('src', '/static/Core/img/moon.png');
		body.setAttribute('data-bs-theme', 'dark');
		theme = false
	}
	localStorage.setItem('theme', theme);
});
const loadTheme = localStorage.getItem('theme');
if ( loadTheme === 'true' ) {
	btnChangeTheme.setAttribute('src', '/static/Core/img/sun.png');
	body.setAttribute('data-bs-theme', 'light');
	theme = true
}