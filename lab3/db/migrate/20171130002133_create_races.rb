class CreateRaces < ActiveRecord::Migration
  def change
    create_table :races do |t|
      t.string :track
      t.references :organization, foreign_key: true
      t.datetime :date

      t.timestamps null: false
    end
  end
end
