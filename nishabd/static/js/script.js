document.addEventListener('DOMContentLoaded', function() {
    // Initialize the slider
    initSlider();

    // Language Change (if applicable)
    // Add event listener here if you have a language change button, for example:
    // document.getElementById("hindi_btn").addEventListener("click", changeLanguageToHindi);
});

// Slider Functionality
function initSlider() {
    let slideIndex = 1;
    showSlides(slideIndex);

    document.querySelector(".prev").addEventListener("click", function() {
        plusSlides(-1);
    });

    document.querySelector(".next").addEventListener("click", function() {
        plusSlides(1);
    });

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    window.currentSlide = function(n) {
        showSlides(slideIndex = n);
    };

    function showSlides(n) {
        let i;
        let slides = document.getElementsByClassName("mySlides");
        let dots = document.getElementsByClassName("dot");
        if (n > slides.length) {
            slideIndex = 1;
        }
        if (n < 1) {
            slideIndex = slides.length;
        }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " active";
    }
}

// Function to change language to Hindi (optional, if required)
/* function changeLanguageToHindi() {
    let title = document.getElementById("title");
    let home = document.getElementById("home");
    let shop = document.getElementById("shop");
    let categories = document.getElementById("categories");
    let contact = document.getElementById("contact");
    let welcome_user = document.getElementById("welcome_user");
    let chatbot = document.getElementById("chatbot");
    let your_account = document.getElementById("your_account");
    let signin = document.getElementById("signin");
    let aboutus = document.getElementById("aboutus");
    let yourshoppingcart = document.getElementById("yourshoppingcart");

    title.innerText = "निशब्द";
    home.innerText = "होम";
    shop.innerText = "दुकान ";
    categories.innerText = "श्रेणियाँ ";
    contact.innerText = "संपर्क";
    welcome_user.innerText = "उपयोगकर्ता का स्वागत है";
    chatbot.innerText = "सारथि";
    your_account.innerText = "खाता";
    signin.innerText = "संकेत";
    aboutus.innerText = "हमारा परिचय";
    yourshoppingcart.innerText = "आपकी खरीदारी";
} */
