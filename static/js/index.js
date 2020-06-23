var taskId;
var uniqueId;
var statusInterval;
var url;
var siteUrl = {
    1: 'https://news.daum.net/breakingnews/digital/internet',
    2: 'https://news.daum.net/breakingnews/digital/science'
};

var selectedCategory;

$(document).ready(function(){
    $(document).on('click', '#start-crawl', function(){
        selectedCategory = $('#site-select option:selected').val();
        for(k in siteUrl){
            console.log(k)
            console.log(selectedCategory)
            if(k === selectedCategory){
                url = siteUrl[k]
            }
        }
        console.log(url)
        $('#progress').attr("class", "alert alert-secondary");
        $('#progress').html('crawler is working...');
        $.ajax({
            url: '/api/crawl/',
            type: 'POST',
            data: {
                'url': url,
            },
            success: crawlSuccess,
            error: crawlFail,
        })
    });

    $(document).on('click', '#show-data', function(){
        selectedCategory = $('#site-select option:selected').val();
        $.ajax({
            url: '/api/showdata/',
            type: 'GET',
            data: {
                'category': selectedCategory
            },
            success: showData,
            error: showDataFail
        })
    });
});

function checkCrawlStatus(taskId, uniqueId){
    console.log("Log 정보1")
    $.ajax({
        url: '/api/crawl/?task_id='+taskId+'&unique_id='+uniqueId+'/',
        type: 'GET',
        success: showCrawledData,
        error: showCrawledDataFail,
    })
}

function crawlSuccess(data){
    console.log("Log 정보2")
    taskId = data.task_id;
    uniqueId = data.unique_id;
    statusInterval = setInterval(function() {checkCrawlStatus(taskId, uniqueId);}, 2000);
}

function crawlFail(data){
    console.log("Log 정보3")
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}

function showCrawledData(data){
    console.log("Log 정보4")
    if (data.status){
        $('#progress').attr("class", "alert alert-secondary");
        $('#progress').html('crawler is ' + data.status + ' ... ' + 'After crawling, the results are returned');
    }else{
        clearInterval(statusInterval);
        $('#progress').attr("class", "alert alert-primary");
        $('#progress').html('crawling is finished!');
        var list = data.data;
        var html = '';
        for(var i=0; i<list.length; i++){
            html += `
                <tr>
                    <th scope="row">`+ (i + 1) +`</th>
                    <td width="20%"><a href="`+ list[i].news_url +`">`+ list[i].news_headline +`</td>
                    <td>`+ list[i].news_contents +`</td>
                    <td>`+ list[i].news_topic +`</td>
                    <td>`+ list[i].news_topic_detail +`</td>
                    <td>`+ list[i].news_company +`</td>
                </tr>
            `;
        }
        $('#board').html(html);
    }
}

function showCrawledDataFail(data){
    $('#progress').html(data.responseJSON.error);
    $('#progress').attr("class", "alert alert-danger");
}

function showData(data){
    var list = data.data;
    var html = '';
    for(var i=0; i<list.length; i++){
        html += `
            <tr>
                <th scope="row">`+ (i + 1) +`</th>
                <td width="20%"><a href="`+ list[i].news_url +`">`+ list[i].news_headline +`</td>
                <td>`+ list[i].news_contents +`</td>
                <td>`+ list[i].news_topic +`</td>
                <td>`+ list[i].news_topic_detail +`</td>
                <td>`+ list[i].news_company +`</td>
            </tr>
        `;
    }
    $('#progress').attr("class", "");
    $('#progress').empty();
    $('#board').html(html);
}

function showDataFail(data){
    $('#progress').attr("class", "alert alert-danger");
    $('#progress').html(data.responseJSON.error);
    $('#board').empty();
}
