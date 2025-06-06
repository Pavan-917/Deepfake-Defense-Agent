document.addEventListener("keydown", function(e) {
    if (e.key === "PrintScreen") {
        navigator.clipboard.writeText("");
        alert("Screenshot blocked!");
        e.preventDefault();
    }
});

document.addEventListener("contextmenu", function(e) {
    e.preventDefault();
});

document.addEventListener("visibilitychange", function() {
    if (document.hidden) {
        document.body.style.filter = "blur(10px)";
    } else {
        document.body.style.filter = "none";
    }
});