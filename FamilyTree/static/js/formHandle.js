function handleResponse(response) {
    if (response.status === 200) {
        response.json().then(data => {
        
            // Сохранение полученных токенов в localStorage или куки
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            // Перенаправление пользователя или выполнение других действий
            window.location.replace("http://localhost:8000");
        });
    } else {
        console.log(response)
        console.log('Error')
    }
}


// Получение формы и добавление прослушивателя события submit
const form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    event.preventDefault();
    fetch('http://localhost:8000/login/api/token', {
        method: form.method,
        body: new FormData(form),
    })
    .then(handleResponse)
    .catch(error => console.error('Ошибка:', error));
});