document.addEventListener('DOMContentLoaded', function() {
    // Typing effect
    var typeEffect = new Typed(".multiText", {
        strings: ["Where Language Meets No Barrier", "जहां भाषा की कोई बाधा नहीं", "જ્યાં ભાષા કોઈ અવરોધ સાથે મળે છે", "ਜਿੱਥੇ ਭਾਸ਼ਾ ਕੋਈ ਰੁਕਾਵਟ ਨਹੀਂ ਮਿਲਦੀ"],
        loop: true,
        typeSpeed: 30,
        backSpeed: 50,
        backDelay: 2000
    });

    // Slider
    let slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

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

    // Language Change
    let hindi_btn = document.getElementById("hindi_btn");
    hindi_btn.addEventListener("click", () => {
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
    });
});
console.log('Script loaded'); // Before problematic code
