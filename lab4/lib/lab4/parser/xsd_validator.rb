require 'nokogiri'

class XsdValidator
  def initialize(xsd_path)
    @xsd = Nokogiri::XML::Schema(File.read(xsd_path))
  end

  def validate(row_xml)
    xml = Nokogiri::XML(row_xml)

    @xsd.validate(xml).each do |error|
      puts("Invalid xml. Error: #{error.message}")
      return false
    end
    true
  end
end
