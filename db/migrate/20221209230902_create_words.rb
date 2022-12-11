class CreateWords < ActiveRecord::Migration[7.0]
  def change
    create_table :words do |t|
      t.string :title

      t.timestamps

      t.belongs_to :user, foreign_key: true
      t.belongs_to :letter, foreign_key: true
    end
  end
end
