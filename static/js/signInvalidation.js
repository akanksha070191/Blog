document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("signinForm");
    const passwordField = document.getElementById("userpassword");
    const confirmPasswordField = document.getElementById("confirm-password");
    const errorMessage = document.getElementById("error-message");
    const useremail = document.getElementById("useremail");

    form.addEventListener("submit", function (event) {
        console.log('password:', passwordField.value)
        console.log('confirm_password:', confirmPasswordField.value)

        if (passwordField.value !== confirmPasswordField.value) {
            errorMessage.style.display = "block";
            event.preventDefault(); // Stop form submission
        } else {
            errorMessage.style.display = "none";
        }
    });

    // Check in real-time while typing
    passwordField.addEventListener("input", validatePasswords);
    confirmPasswordField.addEventListener("input", validatePasswords);


    function validatePasswords() {
        console.log('password:', passwordField.value)
        console.log('confirm_password:', confirmPasswordField.value)
        if (passwordField.value === confirmPasswordField.value) {
            errorMessage.style.display = "none"; // Hide error message if passwords match
        }
    }

    useremail.addEventListener("input", function(){
        const email = this.value;
        console.log('email', email)
        const email_error = document.getElementById("email-message");

        if(email.length > 5){
            fetch(`/check_email/?email=${email}`)
            .then(response => response.json())
            .then(data => {
                if(data.exists){
                    email_error.style.display="block";
                }
                else{
                    email_error.style.display="none";
                }
            })
            .catch(error => console.error('"Error:", error'));
        }
        else{
            email_error.style.display("none");
        }

    });
});

setTimeout(function() {
    let alertMessages = document.querySelectorAll('.alert');
    alertMessages.forEach(function(alert) {
        alert.style.transition = "opacity 0.5s";
        alert.style.opacity = "0";
        setTimeout(() => alert.remove(), 500); 
    });
}, 3000);