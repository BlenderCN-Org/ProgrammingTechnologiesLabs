require 'sax-machine'
require 'ruby-enum'

module SaxParser
  class Ingredients; end
  class Chars; end
  class Beer; end
  class DispensingMethod; end

  class BeerList
    include SAXMachine
    elements :Beer, class: Beer, as: :beer_list
  end

  class Beer
    include SAXMachine

    def initialize
      super()
      @beer_types = %w[dark light lager live]
    end

    attribute :name
    element :BeerType, class: String, as: :beer_type
    element :Alcohol, as: :alcohol
    element :Manufacture, as: :manufacture
    element :Chars, class: Chars, as: :chars
    element :Ingredients, class: Ingredients, as: :ingredients_list

    def beer_type=(value)
      raise 'Illegal beer_type' unless @beer_types.include? value
      instance_variable_set('@beer_type', value)
    end
  end

  class Chars
    include SAXMachine
    element :AlcoholContention, as: :alcohol_contention
    element :Transparency, as: :transparency
    element :Filtered, as: :filtered
    element :NutritionalValue, as: :nutritional_value
    element :DispensingMethod, class: DispensingMethod, as: :dispensing_method

    def transparency=(value)
      raise 'Illegal transparency' unless /[0-9]+\.?[0-9]+%/ =~ value
      instance_variable_set('@transparency', value)
    end

    def nutritional_value=(value)
      raise 'Illegal nutritional_value' unless /[0-9]+cal/ =~ value
      instance_variable_set('@nutritional_value', value)
    end

  end

  class DispensingMethod
    include SAXMachine

    def initialize
      super()
      @container_materials = %w[plastic glass metal]
    end

    attribute :volume
    attribute :containerMaterial, class: String, as: :container_material

    def container_material=(value)
      unless @container_materials.include? value
        raise 'Illegal container material'
      end
      instance_variable_set('@container_material', value)
    end
  end

  class Ingredients
    include SAXMachine
    elements :Ingredient, as: :ingredients
  end

  def self.parse(input)
    BeerList.parse input
  end
end
