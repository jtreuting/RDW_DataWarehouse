require ['jquery', 'bootstrap', 'mustache', 'edwareDataProxy', 'edwareHelpMenu', 'text!templates/LandingPage.html'], ($, bootstrap, Mustache, edwareDataProxy, edwareHelpMenu, landingPageTemplate) ->
  
  edwareDataProxy.getDatafromSource ['../data/common/en/labels.json', '../data/content/en/landingPage.json'], (data) ->
    output = Mustache.to_html landingPageTemplate, data
    $('body').html output
    helpMenu = edwareHelpMenu.create '.helpMenuContainer', data
    #bind events
    $('.helpMenu a').click (e)->
      target = $(this).attr('href')
      helpMenu.show target
    $('.btn-login').click ()->
      window.location.href = window.location.origin + "/assets/html/comparingPopulations.html?stateCode=NY"
    $('#about li').click ()->
      link = $(this).data('link')
      window.location.href = link