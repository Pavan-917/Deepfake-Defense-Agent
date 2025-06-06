document.addEventListener("keydown", function(e) {
    // Block Print Screen
    if (e.key === "PrintScreen") {
        navigator.clipboard.writeText("");
        alert("Screenshot blocked!");
        e.preventDefault();
    }
});

// Disable right click
document.addEventListener("contextmenu", function(e) {
    e.preventDefault();
});

// Blur when tab is inactive
document.addEventListener("visibilitychange", function() {
    if (document.hidden) {
        document.body.style.filter = "blur(10px)";
    } else {
        document.body.style.filter = "none";
    }
});
