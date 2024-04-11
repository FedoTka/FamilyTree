function check_auth(token, check_refresh = false){
    fetch('http://localhost:8000/api/v1/profile',{
        method: 'GET',
        headers: {'Content-Type': 'application/json; charset=UTF-8',
                  'Authorization':`JWT ${token}`,},
      })
      .then(response => {
        let element = document.getElementById('User').querySelector('a');

        
        if(response.ok){
            response.json().then(data =>{
                element.href = '#';
                let user = element.querySelector('span');
                user.innerText = data.nickname;
            })
        } 
        else if (response.status === 401 & check_refresh === false) {
            update_access_token(localStorage.getItem('refresh_token'))
            .then(token => check_auth(token, true))
            .catch(error =>{
                console.log('Unauthorized');
            })
        }
        else
        {
            console.log('Authorization Error');
        }
      })
      .catch(function(error){
        console.log(`Server Error:${error}`)
      })
}


function update_access_token(token){ 
    return fetch('http://localhost:8000/login/api/token/refresh',{
            method: 'POST',
            headers: {'Content-Type': 'application/json',},
            body: JSON.stringify({'refresh': token})
        })
        .then(response =>{
            if (response.ok){
                return response.json()
            }
            else if (response.status === 401){
                throw new Error('Unathorized')
            }
        })
        .then(data=>{
            
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            return data.access    
        })
        .catch(error =>{
            throw error;
        })

        }

