
// Show welcome alert
window.onload = function () {
    console.log("Institute Website Loaded Successfully");
};

// Scroll to Courses Section
function scrollToCourses() {
    document.querySelector(".courses").scrollIntoView({
        behavior: "smooth"
    });
}

// Course button click alert
const courseButtons = document.querySelectorAll(".course-card button");

courseButtons.forEach(button => {
    button.addEventListener("click", () => {
        alert("Course details page coming soon!");
    });
});

// Navbar active link effect
const navLinks = document.querySelectorAll("nav a");

navLinks.forEach(link => {
    link.addEventListener("click", () => {
        navLinks.forEach(l => l.classList.remove("active"));
        link.classList.add("active");
    });
});

