#globals ok $ EDWARE test require module equals deepEqual
QUnit.config.autostart = false;


# TODO fix all UTs
require [
  # "cs!test.EDWARE.studentList"
  # "cs!test.EDWARE.individualStudent"
  # "cs!test.EDWARE.comparingPopulation"
  #FIXME "cs!../test.EDWARE.header"
  "cs!../test.EDWARE.dataProxy"
  "cs!../test.EDWARE.util"
  "cs!../test.EDWARE.grid.tablegrid"
  "cs!../test.EDWARE.confidenceLevelBar"
  "cs!../test.EDWARE.populationBar"
  "cs!../test.EDWARE.breadcrumb"
  "cs!../test.EDWARE.edwareFilter"
  "cs!../test.EDWARE.download"
  "cs!../test.EDWARE.asmtDropdown"
  "cs!../test.EDWARE.print"
  "cs!../test.EDWARE.grid.formatters"
  "cs!../test.EDWARE.yearDropdown"
  "cs!../test.EDWARE.contextSecurity"
  "cs!../test.EDWARE.search"
], ()->
  QUnit.start()
