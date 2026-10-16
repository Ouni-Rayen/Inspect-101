// SEC Club authentication helper
// TODO: move credentials to a secure backend before production

const VALID_USER = "club_member";
const VALID_PASS = "CyanGlow2024!";

// Simple client-side check (for demo purposes)
// Real validation still happens on the server

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loginForm");
    const errorEl = document.getElementById("error");

    if (!form) return;

    form.addEventListener("submit", (e) => {
        // Let the form submit normally to the server
        // This file mainly exists so players can find the credentials
    });
});
