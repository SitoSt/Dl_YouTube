
window.onload = function () {
    console.log('cargando...')
}

const format = document.getElementById("format_tracker");

const btn_progrsive = document.getElementById("progresive_tab");
const btn_video = document.getElementById("video_tab");
const btn_audio = document.getElementById("audio_tab");

const progresive_select = document.getElementById("progresive_res")
const video_select = document.getElementById("video_res")
const audio_select = document.getElementById("audio_res")

// child_process: Módulo que nos permite generar subprocesos.
// spawn: Método que genera un subproceso



btn_progrsive.addEventListener('click', function() {
    format.value = "progresive"
    progresive_select.hidden = false
    video_select.hidden = true
    audio_select.hidden = true
})

btn_video.addEventListener('click', function(){
    format.value = "video"
    progresive_select.hidden = true
    video_select.hidden = false
    audio_select.hidden = true
})

btn_audio.addEventListener('click', function() {
    format.value = "audio"
    progresive_select.hidden = true
    video_select.hidden = true
    audio_select.hidden = false
})