define [
  "jquery"
  "bootstrap"
  "mustache"
  "text!InfoBarTemplate"
  "edwareDownload"
  "edwarePopover"
  "edwareYearDropdown"
  "edwareDataProxy"
  "edwareUtil"
], ($, bootstrap, Mustache, InfoBarTemplate, edwareDownload, edwarePopover, edwareYearDropdown, edwareDataProxy, edwareUtil) ->

  class ReportInfoBar

    constructor: (@container, @config, @contextSecurity) ->
      @initialize()
      @bindEvent()

    initialize: () ->
      $(@container).html Mustache.to_html InfoBarTemplate,
        title: @config.reportTitle
        subjects: @config.subjects
        labels: @config.labels
      years = edwareUtil.getAcademicYears @config.academicYears?.options
      @createAcademicYear(years)
      @createDownloadMenu()
      @render()

    bindEvent: () ->
      self = @
      $('.downloadIcon').click ->
        # show download menu
        self.edwareDownloadMenu.show()
      $('.reportInfoIcon').click ->
        $(this).popover('show')
      $('.academicYearInfoIcon').click ->
        $(this).popover('show')

    render: () ->
      # bind report info popover
      $('.reportInfoIcon').edwarePopover
        class: 'reportInfoPopover'
        labelledby: 'reportInfoPopover'
        content: @config.reportInfoText
        tabindex: 0

      # set report info text
      $('.reportInfoWrapper').append @config.reportInfoText

      # bind academic year info popover
      $('.academicYearInfoIcon').edwarePopover
        class: 'academicYearInfoPopover'
        labelledby: 'academicYearInfoPopover'
        content: 'placeholder'
        tabindex: 0

    createDownloadMenu: () ->
      @edwareDownloadMenu ?= new edwareDownload.DownloadMenu($('#downloadMenuPopup'), @config, @contextSecurity)

    createAcademicYear: (years) ->
      return if not years
      callback = @config.academicYears.callback
      @academicYear ?= $('#academicYearAnchor').createYearDropdown years, callback

  create = (container, config, contextSecurity) ->
    infoBar = new ReportInfoBar(container, config, contextSecurity)


  ReportInfoBar: ReportInfoBar
  create: create
