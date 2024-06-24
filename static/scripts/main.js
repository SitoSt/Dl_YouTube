const REGEXP = /^https:\/\/(www\.)?youtube\.com\/watch\?/
let fetching = false




//#red
// -- DOM elements --

const nav_bar = document.getElementById('nav-bar');

const form_url = document.getElementById("form-url");
const input_url = document.getElementById("input-url");
const loader_url = document.getElementById("loader-url");

const container_info = document.getElementById("container-info");
const thumbnail = document.getElementById("thumbnail");
const title = document.getElementById("title");


const container_res = document.getElementById("container-res");
const form_preferences = document.getElementById("form-preferences");

const tabs = document.querySelectorAll(".format-radio");

const audio_select = document.getElementById('audio-select')
const video_select = document.getElementById('video-select')
const progressive_select = document.getElementById('progressive-select')

const container_dl = document.getElementById("container-dl");
const loader_dl = document.getElementById('loader-dl');

const link_dl = document.getElementById('link-dl');

const err_notification = document.getElementById("err-notification");
const err_msg = document.getElementById("err-msg");

const close_btn = document.querySelectorAll(".close-btn");

//#



//#blue
// -- events --

// Evento para capturar el envío del formulario con la url
// del video
form_url.addEventListener('submit', (e) => {
    e.preventDefault()

    if (!fetching) {
        fetching = true
        loader_url.hidden = false
        const form = new FormData(e.target)
        const url = e.target.url.value;

        console.log(form)

        console.log(url)
    
        if (REGEXP.test(url)) {
            console.log(url + ' es una url valida!!')
            form.append('url', url)
    
            FetchData('/get-video-info', form, HandleVideoInfo)
        } else {
            console.error(url + ' no es una url valida!!')
            throw new Error
        }
    } else {
        console.log('fetching')
    }
})

// Evento para cambiar el select de la resolución
// según el formato que se elija
tabs.forEach((tab) => {
    let format = tab.id.slice(0, -7);

    tab.addEventListener("change", () => {
        if (this.checked) {
            changeFormat(format, true);
        } else {
            changeFormat(format, false);
        }


    })
})


form_preferences.addEventListener('submit', (e) => {
    e.preventDefault()

    if (!fetching) {
        fetching = true
        loader_dl.hidden = false
        const form = new FormData()

        const format = e.target.format.value

        form.append('format', format)

        switch (format) {
            case 'progressive':
                form.append('res', e.target.progressive_res.value)
                FetchData('/download', form, HandleDownloadFetch)
                break
            case 'audio':
                form.append('res', e.target.audio_res.value)
                FetchData('/download', form, HandleDownloadFetch)
                break
            case 'video':
                form.append('res', e.target.video_res.value)
                FetchData('/download', form, HandleDownloadFetch)
                break
            default:
                console.log('fsdjfsñlk')
        }
    } else {
        console.log('fetching')
    }
})

close_btn.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        Close(e.target)
    })
})

//#

//#green
// -- helpers --

const FetchData = (url, form, callBack) => {

    let error = false

    fetch(url, {
        method: 'POST',
        body: form
    })
        // .catch(err => HandleError(err))
        .then(response => {
            if (response.status === 200) {
                return response.json()
            } else {
                error = true
                HandleError(response)
            }
        })
        .then(json => {
            if (json && !error) {
                callBack(json)
            }
        })
        .finally(() => {
            fetching = false
            loader_url.hidden = true
        })
}

//#


//#yellow
// 
const HandleVideoInfo = (data) => {
    console.log(data)

    thumbnail.setAttribute('src', data.thumbnail);
    title.innerHTML = data.title

    for (res in data.resolutions) {
        if (data.resolutions[res]) {
            const option = document.createElement('option');
            option.setAttribute('class', 'res');
            option.value = res;
            option.append(res);
            video_select.appendChild(option);
        }
    }
    for (arb in data.vibrates) {
        if (data.vibrates[arb]) {
            const option = document.createElement('option');
            option.setAttribute('class', 'res');
            option.value = arb;
            option.append(arb);
            audio_select.appendChild(option);
        }
    }

    container_info.style.display = 'flex';
    container_dl.style.display = 'none';
    container_res.style.display = 'flex';
}

const HandleDownloadFetch = (data) => {

    container_info.style.display = 'flex';
    container_dl.style.display = 'flex';
    container_res.style.display = 'none';

    link_dl.href = `downloads/${data.filename}`;

    var eventoClic = new MouseEvent('click', {
        'view': window,
        'bubbles': true,
        'cancelable': true
    });
    link_dl.dispatchEvent(eventoClic);

    fetching = false
    loader_dl.hidden = true
}

const HandleError = (response) => {
    let motivo = ''

    switch (response.status) {
        case 203:
            motivo = `No se ha podido acceder al video, puede que tenga restricción 
                de edad o sea un video con acceso premium`
            break;
        case 204:
            motivo = `No se ha podido acceder al video. Parece que no existe, 
                o te has equivocado al introducir la url`
            break;
        case 400:
            motivo = `Ha habido un problema con la petición. Parece que no se ha 
                podido enviar la url al servidor`
            break;
        default:
            motivo = `Ha habido un problema desconocido. Vuelve a intentarlo mas tarde`
            break
    }

    err_msg.innerHTML = motivo;

    err_notification.hidden = false;
}
//#


//#pink
// --interacción con la interfaz--

const Close = (btn) => {
    btn.parentNode.parentNode.hidden = true;
}

const changeFormat = (format, display) => {

    console.log(format)

    switch (format) {
        case 'progressive':
            progressive_select.removeAttribute('hidden');
            audio_select.setAttribute('hidden', 'true');
            video_select.setAttribute('hidden', 'true');
            break
        case 'audio':
            progressive_select.setAttribute('hidden', 'true');
            audio_select.removeAttribute('hidden');
            video_select.setAttribute('hidden', 'true');
            break;
        case 'video':
            progressive_select.setAttribute('hidden', 'true');
            audio_select.setAttribute('hidden', 'true');
            video_select.removeAttribute('hidden');
            break;
        default: 
            break
    }
}

async function paste() {
    const url_input = document.getElementById("url");
    const text = await navigator.clipboard.readText();
    url_input.value = text;
}

function displayMenu() {
    if (nav_bar.className === 'nav-bar') {
        nav_bar.className += " responsive";
    } else {
        nav_bar.className = 'nav-bar';
    }
}

//#