require 'happymapper'
require 'ruby-enum'

module DomParser
  class Beer; end
  class Ingredients; end
  class Chars; end
  class DispensingMethod; end
  class BeerType; end
  class ContainerMaterial; end

  class BeerList
    include HappyMapper
    tag 'BeerList'

    attribute :xmlns, String
    has_many :beer_list, Beer, tag: 'Beer'
  end

  class Beer
    include HappyMapper

    def initialize()
      super()
      @beer_types = %w(dark light lager live)
    end

    tag 'Beer'
    attribute :name, String

    element :beer_type, String, tag: 'BeerType'
    element :alcohol, Boolean, tag: 'Alcohol'
    element :manufacture, String, tag: 'Manufacture'
    element :chars, Chars, tag: 'Chars'
    has_many :ingredients, String, tag: 'Ingredients'

    def beer_type=(value)
      unless @beer_types.include? value
        raise 'Illegal beer_type'
      end
      @beer_type = value
    end
  end

  class Chars
    include HappyMapper
    tag 'Chars'

    element :alcohol_contention, Integer, tag: 'AlcoholContention'
    element :transparency, String, tag: 'Transparency'
    element :filtered, Boolean, tag: 'Filtered'
    element :nutritional_value, String, tag: 'NutritionalValue'
    element :dispensing_method, DispensingMethod, tag: 'DispensingMethod'

    def transparency=(value)
      unless /[0-9]+\.?[0-9]+%/ =~ value
        raise 'Illegal transparency'
      end
      @transparency = value
    end

    def nutritional_value=(value)
      raise 'Illegal nutritional_value' unless /[0-9]+cal/ =~ value
      @nutritional_value = value
    end


  end

  class DispensingMethod
    include HappyMapper

    def initialize()
      super()
      @container_materials = %w(plastic glass metal)

    end
    tag 'DispensingMethod'

    attribute :volume, Float
    attribute :container_material, String, tag: 'containerMaterial'

    def container_material=(value)
      unless @container_materials.include? value
        raise 'Illegal container_material'
      end
      @container_material = value
    end

  end

  def self.parse(input)
    BeerList.parse input
  end
end
