let cancelBtn = document.getElementById('cancel-btn');
cancelBtn.addEventListener("click", overrideWTF);

function overrideWTF(e) {
    e.preventDefault();
    
    if (window.location.href.includes("/songs/add")) {
        window.location.replace("/songs");
    } else {
        window.location.replace("/playlists");
    }
    
}