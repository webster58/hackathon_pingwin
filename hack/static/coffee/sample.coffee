$ ->

  $html = $('html')
  _date = new Date()
  $('#footer').find('span.curr_year').text(_date.getFullYear())


  ## recognize device
  $html.addClass categorizr()

  ## IMPORTANT: remove unnecessary code depending on device type
  if app.isMobileDevice()
    # remove desktop specific elements
    $('.desktop-elem').remove()
  else
    # remove mobile specific elements
    $('.mobile-elem').remove()
