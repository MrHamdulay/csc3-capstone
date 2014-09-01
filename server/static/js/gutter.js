setTimeout(function() {

    var height = $($('pre')[0]).height()
      , h_left = $('.left .line-highlight')
      , h_right = $('.right .line-highlight')
      , $gap = $('.gap')
      , width = $gap.width()
      , paths = [];

    var top_l, top_r, bot_r, bot_l, $el_r, $el_l;
    for (var i = 0; i < h_left.length; i++) {
        $el_l = $(h_left[i]);
        $el_r = $(h_right[i]);

        top_l = $el_l.position().top;
        top_r = $el_r.position().top;
        bot_l = top_l + $el_l.height();
        bot_r = top_r + $el_r.height();

        paths.push('<path d="M -1 ' + top_l + ' C ' + (width/2) + ' ' + top_l + ' ' + (width/2) + ' ' + top_r + ' ' + width + ' ' + top_r + ' L ' + width + ' ' + bot_r + ' C ' + (width/2) + ' ' + bot_r + ' ' + (width/2) + ' ' + bot_l + ' -1 ' + bot_l + ' Z" />');

    }

    var svg = '<svg width="' + width + '" height="' + height + '">';
    for (var i = 0; i < paths.length; i++) {
        svg += paths[i];
    }
    svg += '</svg>';
    $gap.append(svg);

}, 1);
