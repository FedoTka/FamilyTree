window.onload = function(){
    token = localStorage.getItem('access_token');
    refresh_token = localStorage.getItem('refresh_token');
    
    
    if(token != undefined){
        check_auth(token);
    }
    
}









