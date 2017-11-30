class Participation < ActiveRecord::Base
  belongs_to :race
  belongs_to :horse
end
