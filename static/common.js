const TIME_BETWEEN_SYMBOLS = 200
const TIME_BETWEEN_LETTERS = 1000

function playLetters(letter_symbol_list) {
    let playNext = function(i) {
        if (i < letter_symbol_list.length) {
            playSymbols(letter_symbol_list[i], function() {
                // sleep before playing the next audio
                setTimeout(function() {
                    playNext(i+1)
                }, TIME_BETWEEN_LETTERS)
            })
        }
    }

    playNext(0)
}

function playSymbols(symbols_list, on_end) {
    let sources = []
    let audio_array = []
    for (let i = 0; i < symbols_list.length; i++) {

        let cur_audio = symbols_list[i] == DOT ? dot_audio : dash_audio
        let audio = $("<audio>")

        sources.push(cur_audio)
        audio_array.push(audio)

        audio_array[i].on('ended', function() {
            if (i < symbols_list.length - 1) {
                audio_array[i+1].on("canplay", function() {
                    setTimeout(function() {
                        audio_array[i+1][0].play()
                    }, TIME_BETWEEN_SYMBOLS)
                })
                audio_array[i+1].attr("src", sources[i+1])
            } else {
                on_end()
            }
        })
    }

    audio_array[0].on("canplay", function(){
        audio_array[0][0].play()
    })
    audio_array[0].attr("src", sources[0])
}

$(document).ready(function () {
    $("#audio_image").click(function() {
        playLetters(letter_symbols)
    })

    $(".transition_button").click(function() {
        console.log("button pressed", $(this).data("href"))
        if ($(this).data("href")) {
            $(location).attr('href', $(this).data("href"))
        }
    })
})
