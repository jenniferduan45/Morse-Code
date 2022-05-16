function drawArray(){
    $('#imageAnswer').empty()
    $.each(user_answer, function(key,string){
        $.each(string, function(k, sym){
            let symbol = $("<img class='symbols'>")
        if (sym == DOT){
            symbol.attr("src","/static/dot.png")
            $("#imageAnswer").append(symbol)
        } else {
            symbol.attr("src","/static/dash.png")
            $("#imageAnswer").append(symbol)
        }
        })
        let space = $("<div class='space'>space</div>")
        $("#imageAnswer").append(space)
    })
}

$(document).ready(function(){

    console.log("quiz.js")

    user_answer = [[]]

    $("#clear_all").click( function(){
        user_answer = [[]]
        $('#imageAnswer').empty()
        console.log(user_answer)
    })

    $("#dot").click( function(){
        user_answer[user_answer.length-1].push(DOT)
        drawArray()
    })

    $("#dash").click( function(){
        user_answer[user_answer.length-1].push(DASH)
        drawArray()
    })

    $("#space").click(function(){
        if (user_answer.length > 0 && user_answer[user_answer.length-1].length!=0){
            user_answer.push([])
        }
        drawArray()
    })

    $("#submit").click( function(){
        // remove whitespace from text answer
        let text_answer = ""
        if ($("#answerInput").val()) {
            text_answer = $("#answerInput").val()
        }
        console.log("txt answer", text_answer)
        text_answer = text_answer.trim()

        // remove spaces from symbol answer
        let symbol_answer = []
        for (let i = 0; i < user_answer.length; i++) {
            if (user_answer[i].length > 0) {
                symbol_answer.push(user_answer[i])
            }
        }

        console.log("text answer: ", text_answer)
        console.log("symbol answer: ", symbol_answer)
        answer = {
            "quiz_id"       : quiz.quiz_id,
            "symbol_answer" : symbol_answer,
            "text_answer"   : text_answer
        }
        $.ajax({
            type: "POST",
            url: "/submit",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(answer),
            success: function(result){
                if (quiz.next_question > 0) {
                    document.location.href = "/quiz/" + quiz.next_question;
                } else {
                    document.location.href = "/result";
                }
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });

    })
})
