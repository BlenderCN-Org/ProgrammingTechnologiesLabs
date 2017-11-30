class CreateBets < ActiveRecord::Migration
  def change
    create_table :bets do |t|
      t.references :user, foreign_key: true
      t.references :participation, foreign_key: true
      t.float :rating
      t.float :bet
      t.boolean :approved
      t.boolean :win

      t.timestamps null: false
    end
  end
end
