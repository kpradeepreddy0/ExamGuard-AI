const form = document.querySelector("form");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const username = document.querySelector('input[name="username"]').value;
  const password = document.querySelector('input[name="password"]').value;

  if (username !== "" && password !== "") {
    // Login success → go to exam page
    window.location.href = "/exam";
  } else {
    alert("Please enter username and password");
  }
});
