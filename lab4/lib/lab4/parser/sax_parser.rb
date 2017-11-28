require 'sax-machine'

module SaxParser
  class Ingredients; end
  class Chars; end
  class Beer; end

  class BeerList
    include SAXMachine
    elements :Beer, class: Beer, as: :beer_list
  end

  class Beer
    include SAXMachine

    attribute :name
    element :BeerType, as: :beer_type
    element :Alcohol, as: :alcohol
    element :Manufacture, as: :manufacture
    element :Chars, class: Chars, as: :chars
    element :Ingredients, class: Ingredients, as: :ingredients_list
  end

  class Chars
    include SAXMachine
    element :AlcoholContention, as: :alcohol_contention
    element :Transparency, as: :transparency
    element :Filtered, as: :filtered
    element :NutritionalValue, as: :nutritional_value
    element :DispensingMethod, class: String, as: :dispensing_method
  end

  class DispensingMethod
    include SAXMachine
    attribute :volume
    attribute :containerMaterial, as: :container_material

  end

  class Ingredients
    include SAXMachine
    elements :Ingredient, as: :ingredients
  end


  def self.parse(input)
    BeerList.parse input
  end

end