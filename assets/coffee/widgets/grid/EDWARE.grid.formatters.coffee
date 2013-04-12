define [
  'jquery'
  'jqGrid'
  'EDWARE'
  'edwareUtil'
  'edwarePopulationBar'
  'edwareConfidenceLevelBar'
  'edwareLOSConfidenceLevelBar'  
], ($, jqGrid, EDWARE, edwareUtil, edwarePopulationBar, edwareConfidenceLevelBar, edwareLOSConfidenceLevelBar) ->
  #
  # * EDWARE grid formatters
  # * Handles all the methods for displaying cutpoints, link in the grid
  # 
    
  showlink = (value, options, rowObject) ->
    link = options.colModel.formatoptions.linkUrl
    cssClass = options.colModel.formatoptions.style
    unless rowObject.header
      params = ""
      i = 0 
      for k, v of rowObject.params
        if (i != 0)
          params = params + "&"
        if k == "id"
          k = options.colModel.formatoptions.id_name
        params = params + k + "=" + v
        i++
      "<a class="+cssClass+" href=\"" + link + "?" + params + "\">" + $.jgrid.htmlEncode(value) + "</a>"
    else
      "<div class="+cssClass+"><span class=summarySubtitle>" + rowObject.subtitle + ":</span><br/><span class='summaryTitle'>"+value+"</span></div>"
  
  showOverallConfidence = (value, options, rowObject) ->
    names = options.colModel.name.split "."
    subject = rowObject[names[0]][names[1]]
    
    if subject
      "<div>P" + subject.asmt_perf_lvl + " [" + subject.asmt_score_range_min + "] " + value + " [" + subject.asmt_score_range_max + "]</div>"
    else
      ""
  
  showConfidence = (value, options, rowObject) ->
    names = options.colModel.name.split "."
    subject = rowObject[names[0]][names[1]]
    if subject
      confidence = subject[names[2]][names[3]]['confidence']
      "<div><strong>" + value + "</strong> (&#177;" + confidence + ")</div>"
    else
      ""
    
  performanceBar = (value, options, rowObject) ->
    asmt_type = options.colModel.formatoptions.asmt_type
    subject = rowObject.assessments[asmt_type]
    
    if subject
      results =  edwareLOSConfidenceLevelBar.create subject, 120
      "<div class='asmtScore' style='background-color:"+ subject.score_bg_color + "; color: "+ subject.score_text_color + ";'>" + subject.asmt_score + "</div><div class = 'confidenceLevel'>" + results + "</div>"      
    else
      ""   

  populationBar = (value, options, rowObject) ->
    asmt_type = options.colModel.formatoptions.asmt_type
    subject = rowObject.results[asmt_type]
    
    if subject
      results = edwarePopulationBar.create subject
      "<div class = 'populationBar'>" + results + "</div>"
    else
      ""
 
  showlink: showlink
  showOverallConfidence: showOverallConfidence
  showConfidence: showConfidence
  performanceBar: performanceBar
  populationBar: populationBar
