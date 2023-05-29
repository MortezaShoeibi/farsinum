console.log("JavaScript Connected...");

function convert(number) {
    fetch(`/api/converter?number=${number}`)
     .then(response => response.json())
     .then(data => show(data));
}

function cleanResult(data) {
    let cleaned_data =
`{
    'status': ${data['status']},
    'number': ${data['number']},
    'integers': ${data['integers']},
    'decimals': ${data['decimals']},
    'text': "${data['text']}"
}`;
    return cleaned_data;
}

function cleanError(data) {
    let cleaned_data = 
`{
    'status': ${data['status']},
    'error': ${data['error']},
    'description': ${data['description']}
}`;
    return cleaned_data;
}

function show(data) {
    let element = document.getElementById('result');
    document.getElementById('result-box').removeAttribute('hidden');
    if (data['text'] === undefined) {
        element.innerText = cleanError(data);
    } else {
        element.innerText = cleanResult(data);
    }
}
