root = exports ? this
# !!!! Hotpoor root object
root.Hs or= {}
Hs = root.Hs
root.num = 0
$ ->
    console.log "local demo puco"
    add_tr = (content_json)->
        kol = content_json["data"]
        try 
            redId = kol["redId"]
        catch error
            console.log "error",kol
            return
        if $("#xhs_#{redId}").length < 1
            root.num = root.num + 1
            $(".a").append """
            <tr style="margin:10px;" id="xhs_#{redId}">
                <td>#{num}</td>
                <td>#{kol["redId"]}</td>
                <td>#{kol["name"]}</td>
                <td>#{kol["currentLevel"]}</td>
                <td>#{(parseInt(kol["likeCollectCountInfo"])/parseInt(kol["totalNoteCount"])).toFixed(2)}</td>
                <td>#{kol["likeCollectCountInfo"]}</td>
                <td>#{kol["totalNoteCount"]}</td>
                <td>#{kol["fansCount"]}</td>
                <td>#{kol["businessNoteCount"]}</td>
                <td>#{kol["userId"]}</td>
                <td>
                    <div><a target="_blank" href="https://www.xiaohongshu.com/user/profile/#{kol["userId"]}">#{kol["userId"]}</a></div>
                </td>
                <td>
                    <div><a target="_blank" href="https://pgy.xiaohongshu.com/solar/advertiser/kol/#{kol["userId"]}">#{kol["userId"]}</a></div>
                </td>
                <td>#{kol["picturePrice"]}</td>
                <td>#{kol["videoPrice"]}</td>
            </tr>
            """

    load_comments = (chat_id=null,comment_id=null)->
        if chat_id == null
            return
        $.ajax
            url:"https://www.qianshanghua.com/api/page/comment/load"
            data:
                chat_id:chat_id
                comment_id:comment_id
            dataType:"json"
            type:"GET"
            success:(data)->
                # console.log data
                comments = data.comments
                for one in comments
                    if one[4] == "v"
                        continue
                    add_tr_next = false
                    try
                        content_json = JSON.parse(one[4])
                        
                        add_tr_next = true
                    catch error
                        add_tr_next = false
                    if add_tr_next
                        add_tr(content_json)
                console.log chat_id,comment_id,data.last_comment_id
                last_comment_id = data.last_comment_id
                if data.last_comment_id != null
                    load_comments(chat_id,last_comment_id)
            error:(data)->
                console.log data
    $(window).on "load",(e)->
        $(".a").append """
        <tr style="margin:10px;">
            <th>编号</th>
            <th>小红书号</th>
            <th>昵称</th>
            <th>level</th>
            <th>均篇点赞收藏</th>
            <th>点赞收藏</th>
            <th>笔记数</th>
            <th>粉丝数</th>
            <th>商业笔记</th>
            <th>userId</th>
            <th>个人主页</th>
            <th>蒲公英主页</th>
            <th>笔记图文一口价</th>
            <th>视频图文一口价</th>
        </tr>
        """
        load_comments("a7afbb1de4b94c42af2ace6374005b07")