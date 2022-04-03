songs = ["1", "2", "3", "4", "5"];
song = {
    "5s8a3reYfth5IIqIJMtx40": {
        id: "5s8a3reYfth5IIqIJMtx40",
        artist_name: "Rod Wave",
        track_name: "Dark Clouds",
    },
};

async function parse_songs() {
    fetch("./songs_tracks.json").then((response) => {
        return response.json();
    });
    //.then((jsondata) => console.log(jsondata));
}

function format_songs(songs) {
    // get all keys of the object
    const keys = Object.keys(songs);

    // getting value of the keys in array
    for (let i = 0; i < keys.length; i++) {
        console.log(person[keys[i]]);
    }
}

function remove_old_songs() {
    const songs = document.querySelectorAll(".song");

    songs.forEach((song) => {
        song.remove();
    });
}

function create_songs(songs) {
    const list_el = document.querySelector("#songs");

    for (let i = 0; i < songs.length; i++) {
        var song = "test";
        var song_el = document.createElement("div");
        song_el.classList.add("song");

        var song_content_el = document.createElement("div");
        song_content_el.classList.add("content");

        song_el.appendChild(song_content_el);

        var song_input_el = document.createElement("input");
        song_input_el.classList.add("text");
        song_input_el.type = "text";
        song_input_el.value = song;
        //song_input_el.setAttribute("readonly", "readonly");

        song_content_el.appendChild(song_input_el);

        list_el.appendChild(song_el);
    }
}

window.addEventListener("load", () => {
    const form = document.querySelector("#new-playlist-form");
    const input = document.querySelector("#new-zip-input");
    // const list_el = document.querySelector("#songs");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        // songs = parse_songs();
        // console.log(songs);
        // format_songs(songs);
        remove_old_songs();
        create_songs(songs);
        input.value = "";
    });
});
