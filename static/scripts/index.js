window.addEventListener("DOMContentLoaded", () => {
    const form_url = document.getElementById("form-url");

    const tabs = document.querySelectorAll('[role="tab"]');
    const form_preferences = document.getElementById("form-preferences");

    form_url.addEventListener('submit', handleInfo);
    form_preferences.addEventListener('submit', handleDownload);

    tabs.forEach((tab) => {
        tab.onclick = changeTabs;
    });
});

const nav_bar = document.getElementById("nav-bar");
const loader_url = document.getElementById("loader-url");
const loader_dl = document.getElementById("loader-dl");

async function handleInfo(e) {
    e.preventDefault();

    const form = new FormData(e.target);


    await fetch('/select', { method: 'POST', body: form })
        .then(response => handleResponseErr(response))
        .then(json => displayInfo(json))
}

async function handleDownload(e) {
    e.preventDefault();

    const form = new FormData();
    loader_dl.style.display = 'block';

    if (e.target.progressive_tab.checked) {
        form.append('format', 'progressive');
        form.append('res', e.target.progressive_res.value);
    } else if (e.target.audio_tab.checked) {
        form.append('format', 'audio');
        form.append('res', e.target.audio_res.value);
    } else if (e.target.video_tab.checked) {
        form.append('format', 'video');
        form.append('res', e.target.video_res.value);
    } else {
        alert('No hay ningún formato de descarga seleccionado. Seleccione un formato para descargar el video');
    }

    fetch('/download', { method: 'POST', body: form })
        .then(response => handleResponseErr(response))
        .then((json) => displayInfo(json))

}

function displayInfo(info) {

    if (info.filename) {

        const filename = info.filename;
        const container_res = document.getElementById("container-res");
        const container_dl = document.getElementById("container-dl");
        container_res.style.display = 'none';
        container_dl.style.display = 'flex';

        const link_dl = document.getElementById("link-dl");

        link_dl.href = `/static/downloads/${filename}`;

        var eventoClic = new MouseEvent('click', {
            'view': window,
            'bubbles': true,
            'cancelable': true
        });
        link_dl.dispatchEvent(eventoClic);

        loader_dl.style.display = 'none';
    } else if (!info.msg_err) {

        const container_info = document.getElementById("container-info");
        const container_dl = document.getElementById("container-dl");
        const container_res = document.getElementById("container-res");
        const loader_url = document.getElementById("loader-url");

        container_info.style.display = 'flex';
        container_dl.style.display = 'none';
        container_res.display = 'flex'

        const thumbnail = document.getElementById("thumbnail");
        thumbnail.setAttribute('src', info.thumbnail);
        const title = document.getElementById("title");
        title.innerText = info.title;

        const audio_select = document.getElementById('audio-select').children[0];
        const video_select = document.getElementById('video-select').children[0];

        for (res in info.resolutions) {
            if (info.resolutions[res]) {
                const option = document.createElement('option');
                option.setAttribute('class', 'res');
                option.value = res;
                option.append(res);
                video_select.appendChild(option);
            }
        }
        for (arb in info.vibrates) {
            if (info.vibrates[arb]) {
                const option = document.createElement('option');
                option.setAttribute('class', 'res');
                option.value = arb;
                option.append(arb);
                audio_select.appendChild(option);
            }
        }
        loader_url.style.display = 'none';
    } else {
        console.log('ha habido un erro, comprueba la función display info, porque los datos no le llegan');
    }

}

function displayMenu() {
    if (nav_bar.className === 'nav-bar') {
        nav_bar.className += " responsive";
    } else {
        nav_bar.className = 'nav-bar';
    }
}
function unDisplayMenu() {
    nav_bar.className = 'nav-bar';
}

function changeTabs(e) {
    const target = e.target;
    const parent = target.parentNode;
    const grandparent = parent.parentNode;

    // Remove all current selected tabs
    parent
        .querySelectorAll('[aria-selected="true"]')
        .forEach((t) => {
            t.setAttribute("aria-selected", false)
            t.previousSibling.previousSibling.checked = false;
        });

    // Set this tab as selected
    target.setAttribute("aria-selected", true);
    target.previousSibling.previousSibling.checked = true;

    // Hide all tab panels
    grandparent
        .querySelectorAll('[role="tabpanel"]')
        .forEach((p) => p.setAttribute("hidden", true));

    // Show the selected panel
    grandparent.parentNode
        .querySelector(`#${target.getAttribute("aria-controls")}`)
        .removeAttribute("hidden");
}

function handleResponseErr(response) {
    json = response.json()
    if (response.ok == true & !json.msg_err) {
        return json;
    } else if (json.msg_err) {
        return json;
    } else {
        return { 'msg_err': 'el servidor ha devuelto una respuesta inesperada, no se han podido obtener los datos necesarios' }
    }
}

async function paste() {
    const url_input = document.getElementById("url");
    const text = await navigator.clipboard.readText();
    url_input.value = text;
}
