window.onload = function () {
    console.log('cargando...');
}

const video_area = document.getElementById("video_preferences");

const format = document.getElementById("format_tracker");

const btn_progressive = document.getElementById("progressive_tab");
const btn_video = document.getElementById("video_tab");
const btn_audio = document.getElementById("audio_tab");

const progressive_select = document.getElementById("progressive_res");
const video_select = document.getElementById("video_res");
const audio_select = document.getElementById("audio_res");

const url_input = document.getElementById("form-url");

const link_descarga = document.getElementById("link_descarga");
const retry_msg = document.getElementById("retry_msg");
const close_btn = document.getElementById("close_btn");

btn_progressive.addEventListener('click', function () {
    format.value = "progressive";
    progressive_select.hidden = false;
    video_select.hidden = true;
    audio_select.hidden = true;
});

btn_video.addEventListener('click', function(){
    format.value = "video";
    progressive_select.hidden = true;
    video_select.hidden = false;
    audio_select.hidden = true;
});

btn_audio.addEventListener('click', function() {
    format.value = "audio";
    progressive_select.hidden = true;
    video_select.hidden = true;
    audio_select.hidden = false;
});


function handleDownload() {
    retry_msg.hidden = false;
    link_descarga.textContent = 'Volver a descargar';
    close_btn.hidden = false;
}

function close() {
    video_area.hidden = true;
    close.log('penes');
}