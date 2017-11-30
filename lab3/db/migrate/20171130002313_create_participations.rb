class CreateParticipations < ActiveRecord::Migration
  def change
    create_table :participations do |t|
      t.references :race, foreign_key: true
      t.references :horse, foreign_key: true
      t.float :rate
      t.integer :place

      t.timestamps null: false
    end
  end
end
