const form = document.querySelector('form')

form.addEventListener('submit', (e) => {
    e.preventDefault()
    const formData = new FormData(form)

    let long_url = formData.get('long_url')

    const URL = '/'

    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({long_url:long_url})
    }

    fetch(URL, requestOptions)
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
    .catch(error => console.log(error))

    console.log('Hello')
})