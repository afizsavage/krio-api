class DropTrails < ActiveRecord::Migration[7.0]
  def change
    drop_table :trails
  end
end
