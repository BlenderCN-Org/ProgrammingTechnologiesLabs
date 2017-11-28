require 'happymapper'

module DomParser
  class Beer; end
  class Ingredients; end
  class Chars; end
  class DispensingMethod; end

  class BeerList
    include HappyMapper
    tag 'BeerList'

    attribute :xmlns, String
    has_many :beer_list, Beer, tag: 'Beer'
  end

  class Beer
    include HappyMapper
    tag 'Beer'
    attribute :name, String

    element :beer_type, String, tag: 'BeerType'
    element :alcohol, Boolean, tag: 'Alcohol'
    element :manufacture, String, tag: 'Manufacture'
    element :chars, Chars, tag: 'Chars'
    has_many :ingredients, String, tag: 'Ingredients'
  end

  class Chars
    include HappyMapper
    tag 'Chars'

    element :alcohol_contention, Integer, tag: 'AlcoholContention'
    element :transparency, String, tag: 'Transparency'
    element :filtered, Boolean, tag: 'Filtered'
    element :nutritional_value, String, tag: 'NutritionalValue'
    element :dispensing_method, DispensingMethod, tag: 'DispensingMethod'
  end

  class DispensingMethod
    include HappyMapper
    tag 'DispensingMethod'

    attribute :volume, Float
    attribute :container_material, String, tag: 'containerMaterial'
  end

  def self.parse(input)
    BeerList.parse input
  end
end
