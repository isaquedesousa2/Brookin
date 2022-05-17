function data_register() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var password_confirm = document.getElementById('password_confirm').value;
    var password = password.trim();
    var password_confirm = password_confirm.trim();

    return {
        'username': username,
        'email': email,
        'password': password,
        'password_confirm': password_confirm
    }

}

function data_login(){
    var login = document.getElementById('login').value;
    var password = document.getElementById('password').value;

    return {
        'login': login,
        'password': password
    }
    
}

