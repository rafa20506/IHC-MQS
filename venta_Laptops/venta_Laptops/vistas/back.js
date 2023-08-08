function showLoginForm() {
    const loginSection = document.getElementById('login-section');
    const registerSection = document.getElementById('register-section');
    loginSection.classList.add('active');
    registerSection.classList.remove('active');
  }
  
  function showRegisterForm() {
    const loginSection = document.getElementById('login-section');
    const registerSection = document.getElementById('register-section');
    loginSection.classList.remove('active');
    registerSection.classList.add('active');
  }

  