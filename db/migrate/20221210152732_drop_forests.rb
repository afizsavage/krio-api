class DropForests < ActiveRecord::Migration[7.0]
  def change
    drop_table :forests
  end
end
