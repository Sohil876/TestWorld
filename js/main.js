// JavaScript

// Vars

// Functions
class CreateUser {
  constructor(name, username, password, email, gitURL){
    this.name = name;
    this.username = username;
    this.password = password;
    this.email = email;
    this.gitURL = gitURL;
    this.skills = {}; // Skill object with json like stored skill data
  }
}

function getFormData() {
  this.username = document.getElementById('username').value;
  this.password = document.getElementById('password').value;
  console.log('getFormData function executed!');
  if (this.username.length === 0 || this.password.length === 0) {
    alert('Fields cannot be left empty!');
    document.getElementById('username').value = document.getElementById('password').value = null;
    throw new Error("ERROR: No login data provided!");
  }
  else {
    login(this.username, this.password);
  }
}

function login(username, password) {
  if (username.toLowerCase() === user.username.toLowerCase() && password === user.password) {
    alert('Logged in sucessfully!');
    let genWelcMsg = function() {
      return `Hello! ${user.name} (<a href="${user.gitURL}">${user.username}</a>)`;
    }
    document.querySelector('.userstuff').innerHTML = genWelcMsg();
    document.getElementById('username').value = document.getElementById('password').value = null;
    document.getElementById('loginForm').remove();
    console.log('login function executed!');
  }
  else {
    alert('Incorrect Username/Password!');
    document.getElementById('username').value = document.getElementById('password').value = null;
    throw new Error('ERROR: Incorrect Username/Password!');
  }
}

// Script
let user = new CreateUser('Arsh Khan', 'Sohil876', '12345', 'test@gmail.com', 'https://github.com/Sohil876');
console.log(user);
console.log(user['name']);
