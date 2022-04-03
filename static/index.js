/*songs = ["1", "2", "3", "4", "5"];
song = {
    "5s8a3reYfth5IIqIJMtx40": {
        id: "5s8a3reYfth5IIqIJMtx40",
        artist_name: "Rod Wave",
        track_name: "Dark Clouds",
    },
};*/

// DOES NOT FUCKING WORK!!!
function generate_songs(zip) {
    $.ajax({
        type: "POST",
        url: String.format("../generate_songs{0}", ""),
        context: document.body,
    }).done(function () {
        alert("finished python script");
    });
}

String.format = function () {
    var s = arguments[0];
    for (var i = 0; i < arguments.length - 1; i += 1) {
        var reg = new RegExp("\\{" + i + "\\}", "gm");
        s = s.replace(reg, arguments[i + 1]);
    }
    return s;
};

async function parse_songs(zip) {
    let promise = await fetch(String.format("../jsons/{0}_tracks.json", zip));
    response = await promise.json();

    return response;
}

function format_songs(songs) {
    // get all keys of the object
    const song_list = [];
    const keys = Object.keys(songs);

    // getting value of the keys in array
    for (let i = 0; i < keys.length; i++) {
        const { id, artist_name, track_name } = songs[keys[i]];
        song_name = String.format("{0} - {1}", artist_name, track_name);

        song_list.push(song_name);
    }
    console.log(song_list);
    return song_list;
}

function remove_old_songs() {
    const songs = document.querySelectorAll(".song");

    songs.forEach((song) => {
        song.remove();
    });
}

function create_songs(songs_list) {
    const list_el = document.querySelector("#songs");

    for (let i = 0; i < songs_list.length; i++) {
        var song = songs_list[i];
        var song_el = document.createElement("div");
        song_el.classList.add("song");

        var song_content_el = document.createElement("div");
        song_content_el.classList.add("content");

        song_el.appendChild(song_content_el);

        var song_input_el = document.createElement("input");
        song_input_el.classList.add("text");
        song_input_el.type = "text";
        song_input_el.value = song;
        song_input_el.setAttribute("readonly", "readonly");

        song_content_el.appendChild(song_input_el);

        list_el.appendChild(song_el);
    }
}

window.addEventListener("load", () => {
    const form = document.querySelector("#new-playlist-form");
    const input = document.querySelector("#new-zip-input");
    // const list_el = document.querySelector("#songs");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        // generate_songs(input.value);
        songs = await parse_songs(input.value);
        // console.log("testing");
        // console.log(songs);
        songs_list = format_songs(songs);
        remove_old_songs();
        create_songs(songs_list);
        input.value = "";
    });
});
