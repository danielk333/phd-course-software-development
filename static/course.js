function open_zoom(image) {
    var zoom = document.getElementById("image_zoom");
    var zoom_img = document.getElementById("zoom_img");
    zoom.style.display = "flex";
    zoom_img.src = image.src; // Set the clicked image as the zoom image
    image.classList.forEach(className => {
        if (className !== "expandable") {
            zoom_img.classList.add(className);
        }
    });
}

function close_zoom() {
    var zoom = document.getElementById("image_zoom");
    zoom.style.display = "none";
    zoom_img.src = "";
    zoom_img.classList.forEach(className => {
        zoom_img.classList.remove(className);
    });
}


document.addEventListener("DOMContentLoaded", function() {
    // Any click outside image closes it
    var zoom = document.getElementById("image_zoom");
    zoom.addEventListener('click', (event) => {
        if (event.target === zoom) {
            close_zoom()
        }
    });

    // Add zoom to all .expandable images on load
    const images = document.querySelectorAll(`img.expandable`);
    images.forEach(function(image) {
        image.onclick = function() { open_zoom(this) };
    });
});