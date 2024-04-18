window.addEventListener("DOMContentLoaded", () => {
    const form_url = document.getElementById("form-url");
    const url_input = document.getElementById("url");

    const tabs = document.querySelectorAll('[role="tab"]');
    const form_preferences = document.getElementById("form-preferences");

    form_url.addEventListener('submit', handleInfo);
    form_preferences.addEventListener('submit', handleDownload);

    tabs.forEach((tab) => {
        tab.onclick = changeTabs;
    });
});

async function handleInfo(e) {
    e.preventDefault();

    const form = new FormData(e.target);

    await fetch('/select', { method: 'POST', body: form })
        .then(response => handleResponseErr(response))
        .then(json => displayInfo(json));
}

async function handleDownload(e) {
    e.preventDefault();

    const form = new FormData();

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

    await fetch('/download', { method: 'POST', body: form })
        .then(response => handleResponseErr(response))
        .then(json => {
            const container_dl = document.getElementById("container-dl");
            const link_dl = document.getElementById("link-dl");
            displayInfo({ 'undisplay': true });

            link_dl.href = link_dl.href + json.filename;
            container_dl.style.display = 'flex';

            var eventoClic = new MouseEvent('click', {
                'view': window,
                'bubbles': true,
                'cancelable': true
            });
            link_dl.dispatchEvent(eventoClic);
            // URL.revokeObjectURL(guardar.href);
        });

}

function displayInfo(info) {

    if (info.undisplay) {
        const container_res = document.getElementById("container-res");
        container_res.style.display = 'none';
    } else if (!info.msg_err) {

        const container_info = document.getElementById("container-info");
        container_info.style.display = 'flex';

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
    } else {
        console.log('ha habido un erro, comprueba la función display info, porque los datos no le llegan');
    }

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
        return { 'msg_err': 'el servidor ha devuelto una respuesta inesperada, no se han podido obtener los datos necesarios' };
    }
}

async function paste() {
    const text = await navigator.clipboard.readText();
    url_input.value = text;
}