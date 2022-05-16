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
    currentDate = new Date();
    timestamp = currentDate.getTime();

    lesson_id = lessons.lesson_id
    action = "enter page"
    content = lessons.letter
    content_type = "text"
    record_user_action(lesson_id, action, content, content_type, timestamp)

    $("#audio_image").click(function() {
        console.log("User clicked audio")
        action = "clicked"
        content_type = "audio"
        timestamp = currentDate.getTime();
        record_user_action(lesson_id, action, content, content_type, timestamp)
    })
})