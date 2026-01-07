/* ===============================
   Global App Script
   =============================== */

document.addEventListener("DOMContentLoaded", () => {

  /* ================= LOGIN FORM ================= */

  const loginForm = document.getElementById("loginForm");
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");

  if (loginForm && usernameInput && passwordInput) {

    loginForm.addEventListener("submit", (event) => {
      event.preventDefault();

      const username = usernameInput.value.trim();
      const password = passwordInput.value.trim();

      console.log("Username:", username);
      console.log("Password:", password);

      if (!username || !password) {
        alert("Please enter both username and password.");
        return;
      }

      // ✅ Simulated authentication (replace later with real auth)
      window.location.href = "feature_selection.html";
    });

  }


  /* ================= SIGNUP / LOGIN TOGGLE ================= */

  const showSignupBtn = document.getElementById("showSignup");
  const showLoginBtn = document.getElementById("showLogin");
  const loginContainer = document.querySelector(".form-container");
  const signupContainer = document.getElementById("signupContainer");

  if (showSignupBtn && showLoginBtn && loginContainer && signupContainer) {

    showSignupBtn.addEventListener("click", () => {
      loginContainer.style.display = "none";
      signupContainer.style.display = "block";
    });

    showLoginBtn.addEventListener("click", () => {
      signupContainer.style.display = "none";
      loginContainer.style.display = "block";
    });

  }

});
