class CreateDefinations < ActiveRecord::Migration[7.0]
  def change
    create_table :definations do |t|
      t.text :define
      t.string :example_statement
      t.binary :approval_status

      t.timestamps

      t.belongs_to :user, foreign_key: true
      t.belongs_to :word, index: { unique: true }, foreign_key: true
    end
  end
end
