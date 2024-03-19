function check_auth(token){
    fetch('http://localhost:8000/api/v1/profile',{
        method: 'GET',
        headers: {'Content-Type': 'application/json; charset=UTF-8',
                    'Authorization':`JWT ${token}`,},
      })
      .then(res => res.json())
      .then(function(data){
         user_name = document.getElementById('UserNickname');
         user_name.innerHTML = data.nickname; 
      })
}