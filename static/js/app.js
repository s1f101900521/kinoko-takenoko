function update_bargraph(json_data) {
    console.log(json_data);

    let kinoko_element = document.getElementById('kinoko');
    let takenoko_element = document.getElementById('takenoko');

    let kinoko_percent = json_data.kinoko / (json_data.kinoko + json_data.takenoko) * 100;
    let takenoko_percent = json_data.takenoko / (json_data.kinoko + json_data.takenoko) * 100;

    kinoko_element.attributes['aria-volumenow'] = kinoko_percent + '%';
    takenoko_element.attributes['aria-volumenow'] = takenoko_percent + '%';
    kinoko_element.style.width = kinoko_percent + '%';
    takenoko_element.style.width = takenoko_percent + '%';
}

function periodic_callback() {
    fetch('/api/v1/votes')
    .then(response => response.json())
    .then(update_bargraph)
    .catch(console.log);
}

// periodic_callback関数を3秒おきに実行 (call periodic_callback function every 3 seconds)
setInterval(periodic_callback, 3000);
