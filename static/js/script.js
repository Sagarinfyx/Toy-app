function toggleNavbar() {
    var navbar = document.querySelector(".navbar");
    navbar.classList.toggle("responsive");
}
// Pseudocode for password reset functionality

// Step 1: Generate Secure Token
const crypto = require('crypto');

const generateSecureToken = () => {
  return crypto.randomBytes(20).toString('hex'); // Generate a random secure token
};

// Step 2: Send Email with Reset Link
// Add the token to the reset link and send it to the user's email

// Step 3: Verify Token and Process Password Reset
// On the server side, when the user clicks the link:
const resetPassword = (token, newPassword) => {
  // Check if the token is valid and not expired
  // If valid, find the user associated with the token in the database
  // Update the user's password with the new hashed password
  // Invalidate or delete the used token from the database
};

