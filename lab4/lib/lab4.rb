require 'lab4/version'
require 'lab4/parser/dom_parser'
require 'lab4/parser/sax_parser'
require 'lab4/parser/xsd_validator'

module Lab4
  xsd_validator = XsdValidator.new '../res/BeerSchema.xsd'

  input_file_path = '../res/BeerList.xml'
  xml = File.read input_file_path

  if xsd_validator.validate xml
    dom_parsed_xml = DomParser.parse xml

    count = dom_parsed_xml.beer_list.count
    dom_beer_list = dom_parsed_xml.beer_list
    puts "<DOM-PARSER> XML contain #{count} elements"
    puts '<DOM-PARSER> Sort by alcohol contention'
    dom_beer_list
      .sort_by { |beer| beer.chars.alcohol_contention }
      .each { |beer| puts "<DOM-PARSER> #{beer.name} --> #{beer.chars.alcohol_contention}" }

    puts('==================================================================')

    sax_parsed_xml = SaxParser.parse xml
    sax_beer_list = sax_parsed_xml.beer_list
    count = sax_beer_list.count
    puts("<SAX-PARSER> XML contain #{count} elements")
    puts('<SAX-PARSER> Sort by transparency')
    sax_beer_list
      .sort_by { |beer| beer.chars.transparency }
      .each { |beer| puts "<SAX-PARSER> #{beer.name} --> #{beer.chars.transparency}" }
  end
end
