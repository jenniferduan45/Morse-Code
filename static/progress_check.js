function record_user_action(lesson_id, action, content, content_type, time) {
    user_record = {
        "lesson_id" : lesson_id,
        "action" : action,
        "content" : content,
        "content_type" : content_type,
        "time" : time
    } 
    $.ajax({
        type: "POST",
        url: "/learnaction",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(user_record),
        success: function(result){
            console.log("User action recorded")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function() {
    currentDate = new Date()
    timestamp = currentDate.getTime()

    lesson_id = progress_check.lesson_id
    action = "enter page"
    content = "progress_check" + progress_check.letter
    content_type = "text"
    record_user_action(lesson_id, action, content, content_type, timestamp)

    $("#option1").click(function() {
        console.log("User clicked option")

        var user_answer = progress_check.options[0]
        $("#option1").disabled = true
        $("#option2").disabled = true
        $("#option3").disabled = true
        result = ""
        if (user_answer == progress_check.letter) {
            result = "Correct"
        }
        else {
            result = "Wrong"
        }
        $("#progress_check_result").html(result)

        action = "clicked"
        content = "user chooses" + user_answer + ": " + result
        content_type = "option"
        timestamp = currentDate.getTime();
        record_user_action(lesson_id, action, content, content_type, timestamp)
    })

    $("#option2").click(function() {
        console.log("User clicked option")

        var user_answer = progress_check.options[1]
        $("#option1").disabled = true
        $("#option2").disabled = true
        $("#option3").disabled = true
        result = ""
        if (user_answer == progress_check.letter) {
            result = "Correct"
        }
        else {
            result = "Wrong"
        }
        $("#progress_check_result").html(result)

        action = "clicked"
        content = "user chooses" + user_answer + ": " + result
        content_type = "option"
        timestamp = currentDate.getTime();
        record_user_action(lesson_id, action, content, content_type, timestamp)
    })

    $("#option3").click(function() {
        console.log("User clicked option")

        var user_answer = progress_check.options[2]
        $("#option1").disabled = true
        $("#option2").disabled = true
        $("#option3").disabled = true
        result = ""
        if (user_answer == progress_check.letter) {
            result = "Correct"
        }
        else {
            result = "Wrong"
        }
        $("#progress_check_result").html(result)

        action = "clicked"
        content = "user chooses" + user_answer + ": " + result
        content_type = "option"
        timestamp = currentDate.getTime();
        record_user_action(lesson_id, action, content, content_type, timestamp)
    })

})