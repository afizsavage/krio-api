class AddLetterRefToWords < ActiveRecord::Migration[7.0]
  def change
    add_reference :words, :letter, null: false, foreign_key: true
  end
end
